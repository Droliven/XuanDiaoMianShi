#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# appmsglist_action_3240281391=card; pgv_pvid=7776552235; RK=+vMYcw0RE9; ptcz=d2f483adf216980b5b42c374b8057f89ad76da68418857c87afcc90f177a4f69; rewardsn=; wxtokenkey=777; wwapp.vid=; wwapp.cst=; wwapp.deviceid=; ua_id=upgmAz75D44mt8lIAAAAAIW-wtb1mZJ2qCCVgzLFkSk=; wxuin=68270205036076; mm_lang=zh_CN; _clck=3240281391|1|f6i|0; uuid=e79605a3a8977458b924882a3894c35e; rand_info=CAESIMfzsrmf9I8ZRJgNAk0HFI1fBF+0i9m47iGIcGvox6yN; slave_bizuin=3240281391; data_bizuin=3240281391; bizuin=3240281391; data_ticket=PyzW1cF9Awj3St9xRWNPfDbMqaafl9/O7jIT6u2JWv+9mjZd+jpZ/U1kNEByIovn; slave_sid=Z0dkMUNJbGhDSWp2b0ZsdTV3Xzd5ajduYW9yTHR3Y0xMTHRTbUpzc1FKeXJFNXV5OXBCYjBpbHN4RElibTQydjNRc2NoSnFnc1BBaDJYV3Mxb2lKWkYxYXJ6eW9TZUk2SmdLT2dfQklDMXVJYUdnSjAycURnYmFkaGNSN0V0Wkk5NVJ5OTJjYTd5NEZSSGVS; slave_user=gh_61791c15b2e0; xid=1bddba02363dd253c6d0d5cea226b085

import json
import requests
import time
import random

import yaml

with open("cfg.yaml", "r", encoding="utf-8") as file:
    file_data = file.read()
config = yaml.safe_load(file_data)

headers = {
    "Cookie": config['cookie'],
    "User-Agent": config['user_agent']
}

# 请求参数
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"
begin = "0"
params = {
    "action": "list_ex",
    "begin": begin,
    "count": "4",
    "fakeid": config['fakeid'],
    "type": "9",
    "need_author_name": 1,
    "token": config['token'],
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
}

# 存放结果
app_msg_list = []
# 在不知道公众号有多少文章的情况下，使用while语句
# 也方便重新运行时设置页数
with open("app_msg_list.csv", "w", encoding='utf-8') as file:
    file.write("文章标识符aid,标题title,链接url,时间time\n")
i = 0
while True:
    begin = i * 5
    params["begin"] = str(begin)
    # 随机暂停几秒，避免过快的请求导致过快的被查到
    time.sleep(random.randint(2, 6))
    resp = requests.get(url, headers=headers, params=params, verify=False)
    # 微信流量控制, 退出
    if resp.json()['base_resp']['ret'] == 200013:
        print("frequencey control, stop at {}".format(str(begin)))
        time.sleep(3600)
        continue

    # 如果返回的内容中为空则结束
    if len(resp.json()['app_msg_list']) == 0:
        print("all ariticle parsed")
        break

    msg = resp.json()
    if "app_msg_list" in msg:
        for item in msg["app_msg_list"]:
            info = '"{}","{}","{}","{}"'.format(str(item["aid"]), item['title'], item['link'], str(item['create_time']))
            with open("app_msg_list.csv", "a", encoding='utf-8') as f:
                f.write(info + '\n')
        print(f"第{i}页爬取成功\n")
        print("\n".join(info.split(",")))
        print("\n\n---------------------------------------------------------------------------------\n")

    # 翻页
    i += 1