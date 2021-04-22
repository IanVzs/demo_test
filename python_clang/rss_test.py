# -*-coding: utf-8-*-
import requests
import xmltodict

headers = {'User-Agent': 'Mozilla/5.0'}
aaa = requests.get("https://www.zhihu.com/rss", headers=headers).content
import ipdb; ipdb.set_trace()

bbb = xmltodict.parse(aaa)
ddd = bbb["rss"]["channel"]["item"][0]
ddd = {k:v for k,v in ddd.items() if k != "description"}

"""
{'title': '开拓@北极光', 'link': 'http://zhuanlan.zhihu.com/p/270640698?utm_campaign=rss&utm_medium=rss&utm_source=rss&utm_content=title', 'dc:creator': OrderedDict([('@xmlns:dc', 'http://purl.org/dc/elements/1.1/'), ('#text', '安柏霖')]), 'pubDate': 'Sun, 01 Nov 2020 23:30:11 +0800', 'guid': 'http://zhuanlan.zhihu.com/p/270640698'}
"""

作者, 标题, link, 日期