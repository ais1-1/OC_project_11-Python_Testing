from locust import HttpUser, task, between

from server import clubs, competitions


class ProjectPerfTest(HttpUser):

    """Make the simulated users wait between 1 and 5 seconds after each task is executed"""

    wait_time = between(1, 5)

    def on_start(self):
        self.client.post(
            "/showSummary", data=dict({"email": clubs[0]["email"]}), name="/showSummary"
        )

    @task
    def index(self):
        self.client.get("/", name="/")

    @task
    def book(self):
        self.client.get(
            (f"/book/{competitions[0]['name']}/{clubs[0]['name']}"),
            name=(f"/book/{competitions[0]['name']}/{clubs[0]['name']}"),
        )

    @task
    def purchase_places(self):
        self.client.post(
            "/purchasePlaces",
            {
                "competition": competitions[0]["name"],
                "club": clubs[0]["name"],
                "places": 0,
            },
            name="/purchasePlaces",
        )

    @task
    def points_display(self):
        self.client.get("/viewClubPoints", name="/viewClubPoints")

    @task
    def logout(self):
        self.client.get("/logout", name="/logout")
