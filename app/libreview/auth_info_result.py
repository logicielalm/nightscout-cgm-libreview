from datetime import datetime
import requests  # type: ignore
from app.libreview.constants import Constants

class AuthInfoResult:
    def __init__(self, response):

        
        self.response = response
        self.success = response.status_code == 200
        try:
            data = response.json()["data"]
            self.token = data["authTicket"]["token"]
            self.user_id = data["user"]["id"]
            self.expires = datetime.fromtimestamp(int(data["authTicket"]["expires"]))
            print(f"🔑 AuthInfoResult initialized with response: {data['authTicket']['expires']}")
        except ValueError:
            self.user_id = None
            self.token = None
            self.expires = None
            self.success = False