#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# local_batch_install.py
import os


def local_mkdir(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def huo_qu_wen_jian_ming(path):
    pwd = os.path.abspath('.')
    file_path = pwd + "\\" + path
    return os.listdir(file_path)


def local_batch_install():
    file_name_list = huo_qu_wen_jian_ming('local_batch_install_packages')
    if len(file_name_list) == 0:
        print('本地【local_batch_install_packages】没有发现第三方库包')
    else:
        try:
            for file_name in file_name_list:
                os.system("pip3 install " + file_name)
            print('Successful!')
        except:
            print('Failed')


if __name__ == '__main__':
    local_mkdir('local_batch_install_packages')
    local_batch_install()
