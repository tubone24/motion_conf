import requests, json
import netifaces

ip_address = netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']

WEB_HOOK_URL = "https://hooks.slack.com/services/xxxxx"
requests.post(WEB_HOOK_URL, data = json.dumps({
    "text": "*!!!Reboot!!!* \n\nNew IP:" + ip_address,
    'username': "motion_detect",
    'icon_emoji': ":robot_face:",
    'link_names': 1,
}))
