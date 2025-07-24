from datetime import datetime
import requests # type: ignore

from libreview.constants import Constants

class AuthInfoResult:
    def __init__(self, response: requests.Response):
        self.response = response
        self.success = response.status_code == 200
        try:
            data = response.json()["data"]
            self.token = data["authTicket"]["token"]
            self.user_id = data["user"]["id"]
            self.expires = datetime.fromtimestamp(int(data["authTicket"]["expires"]))
            self.success = True
        except ValueError:
            self.user_id = None
            self.token = None
            self.expires = None
            self.success = False