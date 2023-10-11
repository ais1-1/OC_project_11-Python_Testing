""" Unit tests related to booking """

import server
import utilities


class TestBooking:
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

    

    def test_utilities_update_booking_details(self):
        club_name = self.club[0]["name"]
        competition_name = self.competition[0]["name"]
        places_booked = 12
        expected_booking_details = {
            "Test Festival": {
                "Test club": self.booking_details[competition_name][club_name]
                + places_booked
            }
        }
        result = utilities.update_booking_details(
            self.booking_details, club_name, competition_name, places_booked
        )
        assert result == expected_booking_details
