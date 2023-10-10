""" Unit tests related to Authentication """

from server import app, clubs


class TestAuthentication:
    def setup_method(self):
        self.client = app.test_client()
    
    def test_registration_with_empty_email(self):
        result = self.client.post("/showSummary", data={"email": ""})
        assert result.status_code == 400
    
    def test_registration_with_unknown_email(self):
        result = self.client.post("/showSummary", data={"email": "jane@doe.cc"})
        assert result.status_code == 401
    
    def test_registration_with_known_email(self):
        result = self.client.post("/showSummary", data={"email": clubs[0]["email"]})
        assert result.status_code == 200
