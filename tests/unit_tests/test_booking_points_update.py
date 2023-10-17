""" Unit tests for club points updates after booking """

import server


class TestBookingPointsUpdate:
    def setup_method(self):
        self.client = server.app.test_client()
        self.club = [{"name": "Test club", "email": "test@example.com", "points": "8"}]
        self.competition = [
            {
                "name": "Test Festival",
                "date": "2024-03-27 10:00:00",
                "numberOfPlaces": "25",
            }
        ]
        self.booking_details = {"Test Festival": {"Test club": 0}}

        server.clubs = self.club
        server.competitions = self.competition
        server.booking_details = self.booking_details

    def test_subtract_points_on_purchasing_places(self):
        places_required = 4
        club_name = self.club[0]["name"]
        club_points = int(self.club[0]["points"])
        competition_name = self.competition[0]["name"]
        self.client.post(
            "/purchasePlaces",
            data={
                "competition": competition_name,
                "club": club_name,
                "places": places_required,
            },
        )
        assert int(self.club[0]["points"]) == club_points - places_required

    def test_deduct_more_points_than_available(self):
        places_required = 9
        club_name = self.club[0]["name"]
        competition_name = self.competition[0]["name"]
        response = self.client.post(
            "/purchasePlaces",
            data={
                "competition": competition_name,
                "club": club_name,
                "places": places_required,
            },
        )
        error_message = "have enough points to do this"
        assert response.status_code == 400
        assert int(self.club[0]["points"]) >= 0
        assert error_message in response.data.decode()
