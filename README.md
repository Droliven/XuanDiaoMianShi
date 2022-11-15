# 公务员选调面试话题北宋面试公众号推文收录
> 北宋面试公众号整理发布了国家公务员选调面试中有可能涉及到的一些话题，本项目借助代码自动化获取该公众号下全部面试推文并保存到 Word

## How to run

+ 登录个人微信公众号后台，创建草稿，插入链接，来源选择“北宋面试”公众号，F12 打开控制台，检查 Network, 选择以 "appmsglist_action" 开头的请求，保存 cookie, user_agent, fakeid, token, url;
+ 获取该公众号下全部文章的列表，主要是其 url: `python page_list.py`
+ 根据 url 列表，逐一获取推文正文，并用 BeautifulSoap 解析 HTML 保存关键字段：`python body.py`
+ 将 csv 写到 docx：`python to_docx.py`
+ 在 word 中根据爱好，适当调整样式
