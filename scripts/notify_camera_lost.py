import requests, json, os

WEB_HOOK_URL = "https://hooks.slack.com/services/xxxxxxx"
requests.post(WEB_HOOK_URL, data = json.dumps({
    "text": "*!!!CAMERA LOST!!!* Try to reboot",
    'username': "motion_detect",
    'icon_emoji': ":robot_face:",
    'link_names': 1,
}))

os.system("shutdown /r /t 1")
