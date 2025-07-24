import requests # type: ignore
import hashlib
from datetime import datetime
from zoneinfo import ZoneInfo

from nightscout.glucose_data import GlucoseData

class NightscoutClient:
    def __init__(self, nightscout_url, api_secret):
        self.nightscout_url = nightscout_url
        self.api_secret = api_secret

    def send_glucose_data_list(self, glucose_data_list: list[GlucoseData]) -> None:
        for glucose_data in glucose_data_list:
            self.send_glucose_data(glucose_data)

    def send_glucose_data(self, glucose_data: GlucoseData)-> None:
        print(f"🔄 Envoi des données CGM à Nightscout : {glucose_data.sgv} mg/dL")

        hashed_secret = hashlib.sha1(self.api_secret.encode('utf-8')).hexdigest()

        entry = {
            "type": glucose_data.type,
            "date": glucose_data.date,
            "dateString": glucose_data.date_string,
            "sgv": glucose_data.sgv,
            "device": glucose_data.device
        }

        response = requests.post(
            f"{self.nightscout_url}/api/v1/entries.json",
            json=[entry],
            headers={
                "API-SECRET": hashed_secret,
                "Content-Type": "application/json"
            }
        )
        response.raise_for_status()
        print(f"✅ Donnée envoyée : {entry['sgv']} mg/dL à {entry['dateString']}")
