#!/usr/bin/env python3

import time
import datetime
import subprocess
import os 

pwd = os.getenv("EZVIZ_PASS", "")
addr = os.getenv("EZVIZ_ADDR", "")

dir = "/output"
if not os.path.exists(f"{dir}"):
  os.makedirs(f"{dir}")

while True:
  now = datetime.datetime.now()
  subdir =  f"/{now.year}-{now.month:02d}-{now.day:02d}-{now.hour:02d}"
  name = f"/{now.year}{now.month:02d}{now.day:02d}{now.hour:02d}{now.minute:02d}{now.second:02d}"
  if not os.path.exists(f"{dir}{subdir}"):
    os.makedirs(f"{dir}{subdir}")
  subprocess.run(["ffmpeg", "-rtsp_transport", "tcp", "-i", f"rtsp://admin:{pwd}@{addr}/h264_stream", "-f", "image2", "-vframes", "1", "-pix_fmt", "yuvj420p", f"{dir}{subdir}{name}.jpg"])
  time.sleep(55)
