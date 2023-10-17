""" Integration tests """

import server


class TestServer:
    def setup_method(self):
        self.client = server.app.test_client()
        self.club = [{"name": "Test club", "email": "test@example.com", "points": "13"}]
        self.competition = [
            {
                "name": "Test1 Competition",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25",
            },
            {
                "name": "Test2 Competition",
                "date": "2024-03-27 10:00:00",
                "numberOfPlaces": "10",
            },
        ]
        self.booking_details = {"Test1 Competition": {"Test club": 7}}

        server.clubs = self.club
        server.competitions = self.competition
        server.booking_details = self.booking_details

    def test_logout_redirect(self):
        response = self.client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        assert "Registration Portal" in response.data.decode()

    def test_points_update(self):
        places_required = 4
        club_name = self.club[0]["name"]
        club_points = int(self.club[0]["points"])
        competition_name = self.competition[0]["name"]
        response = self.client.post(
            "/purchasePlaces",
            data={
                "competition": competition_name,
                "club": club_name,
                "places": places_required,
            },
        )
        club_points_after = int(self.club[0]["points"])
        points_board_response = self.client.get("/viewClubPoints")
        assert response.status_code == 200
        assert "Great-booking complete" in response.data.decode()
        assert points_board_response.status_code == 200
        assert club_points_after == club_points - places_required
        assert b"<td>9</td>" in points_board_response.data
