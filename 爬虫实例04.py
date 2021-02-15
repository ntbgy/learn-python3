#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

def 获取图片(url, 目录):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        print(r.raise_for_status())
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
    url = 'https://python123.io/images/nav_logo_v2.png'
    目录 = '/home/ntbgy/图片/'
    print(获取图片(url, 目录))

