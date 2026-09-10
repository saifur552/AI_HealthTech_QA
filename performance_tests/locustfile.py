from locust import HttpUser, task, between

class CuraHealthcareUser(HttpUser):
    wait_time = between(1, 3)
    host = "https://katalon-demo-cura.herokuapp.com"

    @task(2)
    def load_homepage(self):
        self.client.get("/")

    @task(1)
    def login_and_access_appointment(self):
        self.client.post("/authenticate.php", {
            "username": "John Doe",
            "password": "ThisIsNotAPassword"
        })
        self.client.get("/appointment.php")