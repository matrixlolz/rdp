
@echo off
pip install psutil --quiet
pip install requests --quiet
curl -s -L -o loop.py https://github.com/voidxmatrix/rdp/blob/main/loop.py
python loop.py
