#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :yaml_data.py
    @Time      :2023/6/10 14:05
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86/Python_Demo_Note.git
-----------------------------------------------------------
'''
import os,yaml.scanner

class GetYamlData:
    '''
    功能：通过指定路径下的yml文件，获取yaml文件中的数据
    '''
    def __init__(self,file_path):
        self.file_path = file_path

    def get_yaml_data(self) -> dict:
        """
        获取 yaml 中的数据
        :return: 字典数据
        """
        if os.path.exists(self.file_path):
            data = open(self.file_path,'r',encoding='utf-8')
            res = yaml.load(data,Loader=yaml.FullLoader)
        else:
            raise FileNotFoundError('文件路径不存在')
        return res

if __name__ == '__main__':
    res = GetYamlData('/Users/z.m/pythonProject/Interface_Auto_Test/common/config.yaml').get_yaml_data()
    print(res)