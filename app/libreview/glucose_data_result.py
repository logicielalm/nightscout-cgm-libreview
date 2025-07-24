from typing import List
import requests # type: ignore
from libreview.glucose_data_result_item_result import GlucoseDataResultItemResult

class GlucoseDataResult:
    def __init__(self, response: requests.Response):
        self.response = response
        self.success = response.status_code == 200
        self.glucose_values:List[GlucoseDataResultItemResult] = []  # List[GlucoseDataResultItemResult]

        try:
            data = response.json()["data"]
            if "connection" in data and "glucoseMeasurement" in data["connection"]:
                self.glucose_values.append(GlucoseDataResultItemResult(
                    valueInMgPerDl=data["connection"]["glucoseMeasurement"]["ValueInMgPerDl"],
                    timestamp=data["connection"]["glucoseMeasurement"]["Timestamp"]
                ))

            if data["graphData"]:
                for item in data["graphData"]:
                    print(f"📊 Donnée CGM : {item}")
                    self.glucose_values.append(GlucoseDataResultItemResult(
                        valueInMgPerDl=item["ValueInMgPerDl"],
                        timestamp=item["Timestamp"]
                    ))
        except ValueError:
            self.response = None
            self.success = False