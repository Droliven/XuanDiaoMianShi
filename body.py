#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project: beisong
@file   : body.py
@author : levondang
@contact: levondang@163.com
@time   : 2022-11-13 01:06:11
@version: 1.0.0
"""

# here put the import lib
import re
import yaml
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
import random

from jiexi import jiexi_html

with open("cfg.yaml", "r") as file:
    file_data = file.read()
config = yaml.safe_load(file_data)

headers = {
    "Cookie": config['cookie'],
    "User-Agent": config['user_agent']
}

with open("app_msg_list.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
n = len(data)

# with open("beisong_pages.csv", "w", encoding='utf-8') as file:
#     file.write("datetime,url,title,miaoshu,yaoqiu,daan\n")

# for i in range(1, n):
for i in range(221, n):
    mes = data[i].strip("\n").split(",")
    if len(mes) != 4:
        continue
    aid, title, url, unix_time = [item[1:-1] for item in mes]
    dt = datetime.fromtimestamp(int(unix_time))

    if title[:2] != "面试":
        continue

    # todo: sleep
    time.sleep(random.randint(1, 5))
    r = requests.get(url, headers=headers)
    print(f"{i}/{n}, {dt}, {r.status_code}, {url}")
    if r.status_code == 200:
        text = r.text
        miaoshu, yaoqiu, daan_duanluo = jiexi_html(text)
        info = '"{}","{}","{}","{}","{}","{}"'.format(dt, url, title, miaoshu, yaoqiu, daan_duanluo)
        with open("beisong_pages.csv", "a", encoding='utf-8') as f:
            f.write(info + '\n')


