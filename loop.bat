
@echo off
pip install psutil --quiet
pip install requests --quiet
curl -s -L -o loop.py https://raw.githubusercontent.com/matrixlolz/rdp/main/loop.py
python loop.py
