#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


def getHTMLText(url, 浏览器):
    try:
        r = requests.get(url, headers=浏览器, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[-500:]
    except:
        return "产生异常"


if __name__ == "__main__":
    url = 'https://m.ip138.com/iplookup.asp?ip='
    ip = '202.204.80.112'
    浏览器 = {'user-agent': 'Mozilla/5.0'}
    print(getHTMLText(url + ip, 浏览器))
