#!/bin/bash
FILE=$1
OUTPUT_DIR=`dirname $FILE`
OUTPUT_FILE_BASE=`basename $FILE .mp4`
OUTPUT_FILE=$OUTPUT_DIR/$OUTPUT_FILE_BASE.gif
# ffmpeg -y -i $FILE $OUTPUT_FILE
# python3 /home/pi/motion/upload_slack.py $OUTPUT_FILE
python3 /home/pi/motion/upload_slack_mp4.py $FILE
rm -f $FILE
# rm -f $OUTPUT_FILE
