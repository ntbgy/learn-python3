#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编写一个程序，要求能够将元素为任意 Python 支持的类型（包括含有半角逗号的字符串）的列表转储为 CSV ，并能够重新解析为列表。
"""
def InputAndSave_csv(ls,Name):
    value = input('请向列表添加第1个元素')
    ls.append(value)
    num = 1
    while value != '':
        num += 1
        value = input('请向列表添加第{}个元素（如需结束输入，请输入空格）'.format(num))
        ls.append(value)
    print('列表已输入完毕，您输入的列表为:\n{}'.format(ls))

    #将逗号的点换为点
    for i in range(len(ls)):
        if ',' in ls[i]:
            ls[i] = ls[i].replace(',','.')

    f = open('/Users/denglinzhe/Documents/{}.csv'.format(Name),'w',encoding = 'utf-8')
    f.write(','.join(ls)+'\n')
    f.close()
    print('\n恭喜你~，已成功保存为{}.csv文件'.format(Name))

def Read_csv(Name):
    f = open('/Users/denglinzhe/Documents/{}.csv'.format(Name),'r',encoding = 'utf-8')
    fo = f.read().strip('\n').split(',')
    #将替换的点换为逗号
    for i in range(len(fo)):
        if '.' in fo[i]:
            fo[i] = fo[i].replace('.',',')
    print('\n文件{}.csv读取中....请稍后\n'.format(Name))
    print(fo)
    f.close()

def main():
    ls = []
    Name = input('请输入您将要保存的csv文件名称:')
    InputAndSave_csv(ls,Name)
    Read_csv(Name)

main()
