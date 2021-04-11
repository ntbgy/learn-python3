#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：提取文件名.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-26 14:37
import os


def local_mkdir(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def huo_qu_wen_jian_ming(path):
    pwd = os.path.abspath('.')
    file_path = pwd + '\\' + path
    return os.listdir(file_path)


if __name__ == '__main__':
    print('请输入目录：')
    folder_path = input()
    write_name = folder_path + '.txt'
    list_table_name = huo_qu_wen_jian_ming(folder_path)
    with open(write_name, 'w', encoding='utf-8') as fw:
        fw.write('')
    for file_name in list_table_name:
        print("\r{}".format(file_name), end='', flush=True)
        with open(write_name, 'a', encoding='utf-8') as fw:
            fw.write(file_name + '\n')
    print('\nOK!')
