from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo
from nightscout.glucose_data import GlucoseData
from libreview.glucose_data_result import GlucoseDataResult

def convert_to_glucose_data_list(glucose_data: GlucoseDataResult) -> List[GlucoseData]:
    result:List[GlucoseData] =[]

    for item in glucose_data.glucose_values:
        timestamp_str = item.timestamp
        format_str = "%m/%d/%Y %I:%M:%S %p"
        dt_naive = datetime.strptime(timestamp_str, format_str)
        dt_montreal = dt_naive.replace(tzinfo=ZoneInfo("America/Montreal"))

        result.append(
            GlucoseData(
                sgv=item.valueInMgPerDl,
                timestamp=item.timestamp,
                date=int(dt_montreal.timestamp() * 1000),
                date_string=dt_montreal.isoformat(),
                type="sgv",
                device="librelink-python"
            )
        )

        print(f"📊 Donnée CGM : {item.valueInMgPerDl} mg/dL à {dt_montreal.isoformat()}")

    return result