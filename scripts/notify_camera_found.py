import requests, json

WEB_HOOK_URL = "https://hooks.slack.com/services/xxxxxx"
requests.post(WEB_HOOK_URL, data = json.dumps({
    "text": "*!!!CAMERA Detect!!!*",
    'username': "motion_detect",
    'icon_emoji': ":robot_face:",
    'link_names': 1,
}))
