from ota import OTAUpdater
from autoConnectWifi import WIFI


wifiConnect = WIFI()
wifiConnect.autoConnectWifi()
ota_updater = OTAUpdater("main.py")


