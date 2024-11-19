
@echo off
pip install psutil --quiet
pip install requests --quiet
curl -s -L -o loop.py https://gitlab.com/rdp7214147/rdp-avica/-/blob/main/loop.py
python loop.py