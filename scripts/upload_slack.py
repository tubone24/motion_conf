import sys
import json
import requests

FILENAME = sys.argv[1]
TOKEN = "xoxb-3xxxxxx"
CHANNEL = "xxxxxx"

print(FILENAME)
with open("{}".format(FILENAME), "rb") as f:
    files = {"file": f.read()}
    param = {
        "token": TOKEN,
        "channels" :CHANNEL,
        "filename" :FILENAME,
        "title": FILENAME
        }
    resp = requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
    print(resp.text)
    
