import sys
import datetime
import json
import requests

FILENAME = sys.argv[1]
TOKEN = "xoxb-xxxxxx"
CHANNEL = "xxxxxxxx"

print(FILENAME)
with open("{}".format(FILENAME), "rb") as f:
    dt_now = datetime.datetime.now()
    files = {"file": f.read()}
    param = {
        "token": TOKEN,
        "channels" :CHANNEL,
        "filename" :FILENAME,
        "title": "MP4 file"
        }
    resp = requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
    print(resp.text)
