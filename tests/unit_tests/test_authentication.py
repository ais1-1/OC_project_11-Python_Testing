""" Unit tests related to Authentication """

import server


class TestAuthentication:
    def setup_method(self):
        self.client = server.app.test_client()
        self.club = [{"name": "Test club", "email": "test@example.com", "points": "13"}]

        server.clubs = self.club

    def test_registration_with_empty_email(self):
        result = self.client.post("/showSummary", data={"email": ""})
        assert result.status_code == 400

    def test_registration_with_unknown_email(self):
        result = self.client.post("/showSummary", data={"email": "jane@doe.cc"})
        assert result.status_code == 401

    def test_registration_with_known_email(self):
        result = self.client.post("/showSummary", data={"email": self.club[0]["email"]})
        assert result.status_code == 200
