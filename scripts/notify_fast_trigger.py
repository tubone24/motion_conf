import datetime
import json
import requests

WEB_HOOK_URL = "https://hooks.slack.com/services/xxxxx
dt_now = datetime.datetime.now()
requests.post(WEB_HOOK_URL, data = json.dumps({
    "text": "Alarm triggered. Check out the attached video! {}".format(dt_now.strftime("%Y/%m/%d %H:%M:%S")),
    'username': "motion_detect",
    'icon_emoji': ":robot_face:",
    'link_names': 1,
}))
