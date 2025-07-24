from datetime import datetime
import time
import traceback
from convert import convert_to_glucose_data_list
from libreview.libreview_client import LibreViewClient
from nightscout.nightscout_client import NightscoutClient


def init_from_environment_variables():
    import os
    global LIBREVIEW_EMAIL, LIBREVIEW_PASSWORD, NIGHTSCOUT_URL, NIGHTSCOUT_API_SECRET, LIBREVIEW_URL

    LIBREVIEW_EMAIL = os.getenv("LIBREVIEW_EMAIL")
    LIBREVIEW_PASSWORD = os.getenv("LIBREVIEW_PASSWORD")
    LIBREVIEW_URL = os.getenv("LIBREVIEW_URL")
    TIMEZONE = os.getenv("TIMEZONE", "America/Montreal")
    NIGHTSCOUT_URL = os.getenv("NIGHTSCOUT_URL")
    NIGHTSCOUT_API_SECRET = os.getenv("NIGHTSCOUT_API_SECRET")
    NIGHTSCOUT_REFRESH_MINUTES = os.getenv("NIGHTSCOUT_REFRESH_MINUTES", 2)


def init():
    global LIBRE_VIEW_CLIENT, NIGHTSCOUT_CLIENT

    init_from_environment_variables()
    LIBRE_VIEW_CLIENT = LibreViewClient(LIBREVIEW_URL)
    NIGHTSCOUT_CLIENT = NightscoutClient(NIGHTSCOUT_URL, NIGHTSCOUT_API_SECRET)

def main():
    init()
    auth_info = None

    while True:
        if auth_info is None or auth_info.expires <= datetime.now():
            auth_info = LIBRE_VIEW_CLIENT.librelink_login(LIBREVIEW_EMAIL, LIBREVIEW_PASSWORD)

        if auth_info.success:
            try:
                glucose_data = LIBRE_VIEW_CLIENT.get_glucose_data(auth_info)
                if glucose_data:
                    NIGHTSCOUT_CLIENT.send_glucose_data_list(convert_to_glucose_data_list(glucose_data))
                else:
                    print("⚠️ Aucune donnée CGM disponible.")
            except Exception as e:
                print(f"❌ Erreur : {e}")
                traceback.print_exc()
        time.sleep(120)  # 2 minutes

if __name__ == "__main__":
    main()
