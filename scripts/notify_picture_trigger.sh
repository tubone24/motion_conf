#!/bin/bash
FILE=$1
python3 /home/pi/motion/upload_slack.py $FILE
rm -f $FILE
