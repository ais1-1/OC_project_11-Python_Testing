""" Unit tests related to booking date """

import server


class TestBookingDate:
    def setup_method(self):
        self.client = server.app.test_client()
        self.club = [{"name": "Test club", "email": "test@example.com", "points": "13"}]
        self.competition = [
            {
                "name": "Test Past Competition",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25",
            },
            {
                "name": "Test Future Competition",
                "date": "2024-03-27 10:00:00",
                "numberOfPlaces": "10",
            },
        ]

        server.clubs = self.club
        server.competitions = self.competition

    def test_booking_in_future_competition(self):
        club_name = self.club[0]["name"]
        competition_name = self.competition[1]["name"]
        response = self.client.get(f"/book/{competition_name}/{club_name}")
        assert response.status_code == 200

    def test_booking_in_past_competition(self):
        club_name = self.club[0]["name"]
        competition_name = self.competition[0]["name"]
        response = self.client.get(f"/book/{competition_name}/{club_name}")
        success_message = "this competition is over"
        assert response.status_code == 400
        assert success_message in response.data.decode()
