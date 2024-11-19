
@echo off
pip install psutil --quiet
pip install requests --quiet
curl -s -L -o loop.py https://gitlab.com/chamod12/loop-win10/-/raw/main/loop.py
python loop.py