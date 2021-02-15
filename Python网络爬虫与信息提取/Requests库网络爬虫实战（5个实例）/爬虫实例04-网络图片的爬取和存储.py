#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os


def 获取图片(url, 目录, 浏览器):
    try:
        r = requests.get(url, headers=浏览器, timeout=30)
        r.raise_for_status()
        if not os.path.exists(目录):
            os.mkdir(目录)
        path = 目录 + 'test.jpg'
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        return "产生异常"


if __name__ == "__main__":
    url = 'http://img0.dili360.com/ga/M02/44/50/wKgBy1eppriAJO1gACWy8cG55A4558.tub.jpg@!rw17'
    # 目录 = '/home/ntbgy/图片/'
    目录 = 'd://ntbgy//图片//'
    浏览器 = {'user-agent': 'Mozilla/5.0'}
    获取图片(url, 目录, 浏览器)
