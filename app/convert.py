from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo
from app.nightscout.glucose_data import GlucoseData
from app.libreview.glucose_data_result import GlucoseDataResult

def convert_to_glucose_data_list(glucose_data: GlucoseDataResult, timezone: ZoneInfo) -> List[GlucoseData]:
    result:List[GlucoseData] =[]

    for item in glucose_data.glucose_values:
        timestamp_str = item.timestamp
        format_str = "%m/%d/%Y %I:%M:%S %p"
        dt_naive = datetime.strptime(timestamp_str, format_str)
        dt_timezone = dt_naive.replace(tzinfo=timezone)

        result.append(
            GlucoseData(
                sgv=item.valueInMgPerDl,
                timestamp=item.timestamp,
                date=int(dt_timezone.timestamp() * 1000),
                date_string=dt_timezone.isoformat(),
                type="sgv",
                device="librelink-python"
            )
        )

        #print(f"📊 Donnée CGM : {item.valueInMgPerDl} mg/dL à {dt_timezone.isoformat()}")  # Fixed dt_montreal to dt_timezone
    
    return result