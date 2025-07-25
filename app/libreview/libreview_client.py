import requests
from app.libreview.auth_info_result import AuthInfoResult
from app.libreview.glucose_data_result import GlucoseDataResult


class LibreViewClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def librelink_login(self, email: str, password: str) -> AuthInfoResult:
        url = f"{self.base_url}/llu/auth/login"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "version": "4.7.0",
            "Product": "llu.ios",
            "User-Agent": "nightscout-connect, nightscout-connect@0.0.12, LibreView@4.7.0, https://github.com/nightscout/nightscout-connect",
            }
        
        print(f"🔑 Tentative de connexion avec l'email : '{email}' - '***'")
        payload = {"email": email, "password": password}
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        return AuthInfoResult(response)
    
    def get_glucose_data(self, auth_info: AuthInfoResult) -> GlucoseDataResult:
        url = f"{self.base_url}/llu/connections/{auth_info.user_id}/graph"

        headers = {
            "Accept": "application/json",
            "version": "4.7.0",
            "Product": "llu.ios",
            "User-Agent": "nightscout-connect, nightscout-connect@0.0.12, LibreView@4.7.0, https://github.com/nightscout/nightscout-connect",
            "Authorization": f"Bearer {auth_info.token}"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return GlucoseDataResult(response)
