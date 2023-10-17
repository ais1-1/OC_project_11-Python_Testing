""" Unit tests for app routes """

import server


class TestRoutes:
    def setup_method(self):
        self.client = server.app.test_client()
        self.club = [{"name": "Test club", "email": "test@example.com", "points": "13"}]
        self.competition = [
            {
                "name": "Test Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25",
            }
        ]
        self.booking_details = {"Test Festival": {"Test club": 7}}

        server.clubs = self.club
        server.competitions = self.competition
        server.booking_details = self.booking_details

    def test_base_route(self):
        url = "/"
        response = self.client.get(url)
        assert "Registration Portal" in response.data.decode()
        assert response.status_code == 200

    def test_logout_root(self):
        response = self.client.get("/logout")
        assert response.status_code == 302

    def test_view_club_points_route(self):
        url = "/viewClubPoints"
        response = self.client.get(url)
        assert "Points Display Board" in response.data.decode()
        assert response.status_code == 200
