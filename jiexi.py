#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project: beisong
@file   : jiexi.py
@author : levondang
@contact: levondang@163.com
@time   : 2022-11-13 01:42:59
@version: 1.0.0
"""
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag


def jiexi_html(data):
    soup = BeautifulSoup(data, "lxml")

    miaoshu_soup = soup.select("div#js_content > section > section > strong > span")
    miaoshu = ""
    for i in range(len(miaoshu_soup)):
        s = miaoshu_soup[i].contents
        if len(s) == 1 and isinstance(s[0], NavigableString):
            miaoshu += s[0]

    yaoqiu_soup = soup.select("div#js_content > p > strong > span") #[-1].contents[0]
    yaoqiu = ""
    for i in range(len(yaoqiu_soup)):
        s = yaoqiu_soup[i].contents
        if len(s) == 1 and isinstance(s[0], NavigableString):
            yaoqiu += s[0]

    daan_duanluo = []
    daan = soup.select("div#js_content > section[data-support][data-style-id] > section > section")[1].contents
    for i in range(len(daan)):
        curr = ""
        if isinstance(daan[i], Tag):
            span_list = daan[i].select("span")
            for j in range(len(span_list)):
                s = span_list[j].contents
                if len(s) == 1 and isinstance(s[0], NavigableString):
                    curr += s[0]
            daan_duanluo.append(curr.replace("\n", "").replace("\r", ""))

    daan_duanluo = "\n".join(daan_duanluo)
    return miaoshu, yaoqiu, daan_duanluo

if __name__ == '__main__':
    data = r"./test.html"
    with open(data, "r", encoding="utf-8") as f:
        data = f.read()

    miaoshu, yaoqiu, daan_duanluo = jiexi_html(data)
    pass