#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def 判断闰年(年份):
    if 年份 % 400 == 0 or (年份 % 4 == 0 and 年份 % 100 != 0):
        return "是"
    else:
        return "不是"
def main():
    try:
        年份 = eval(input("请输入年份："))
    except:
        print("输入格式错误，仅支持输入数字，例如：2020 或者 -1080 （公元前）")
    print(判断闰年(年份))
if __name__ == '__main__':
    main()