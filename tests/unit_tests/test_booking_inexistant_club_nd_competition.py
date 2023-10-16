""" Unit tests for inexistant clubs and competitions """

import server


class TestBookingInexistantEntities:
    def setup_method(self):
        self.client = server.app.test_client()
        self.club = [{"name": "Test club", "email": "test@example.com", "points": "13"}]
        self.competition = [
            {
                "name": "Test Competition",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25",
            }
        ]

        server.clubs = self.club
        server.competitions = self.competition

    def test_booking_in_non_existant_competition(self):
        club_name = self.club[0]["name"]
        competition_name = "Inexistant competition"
        response = self.client.get(f"/book/{competition_name}/{club_name}")
        error_message = "Something went wrong-please try again"
        assert response.status_code == 500
        assert error_message in response.data.decode()

    def test_booking_by_non_existant_club(self):
        club_name = "Inexistant club"
        competition_name = self.competition[0]["name"]
        response = self.client.get(f"/book/{competition_name}/{club_name}")
        error_message = "Something went wrong-please try again"
        assert response.status_code == 500
        assert error_message in response.data.decode()
