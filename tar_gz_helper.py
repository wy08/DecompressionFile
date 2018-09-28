#!/usr/bin/env python
# encoding: utf-8
# @Author  :   WYY
# @License :   (C) Copyright 2016-2018
# @Contact :   1123231279@qq.com
# @IpAdd   :   localhost:9080
# @Software:   PyCharm
# @File    :   tar_gz_helper.py
# @Time    :   2018/9/21 下午4:47
# @Desc    :


import os


import gzip
def un_gz(file_name):
    """解压gz包"""
    f_name = file_name.replace(".gz", "")
    #获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    #创建gzip对象
    f =open(f_name, "w+").write(g_file.read())
    #gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()

import tarfile
def un_tar(file_name):
    """解压tar"""
    print(file_name)
    tar = tarfile.open(file_name)
    names = tar.getnames()
    temp_file_path = ''
    if os.path.isdir(file_name + "_files"):
        print('文件已存在')
        temp_file_path = os.path.isdir(file_name + "_files")
    else:
        temp_file_path = os.mkdir(file_name + "_files")
        print('创建一个新的文件名')
    #因为解压后是很多文件，预先建立同名目录
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()
    return temp_file_path


import zipfile
def un_zip(file_name):
    """解压zip"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
    zip_file.close()


import rarfile
import os
def un_rar(file_name):
    """unrar zip file"""
    rar = rarfile.RarFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    if os.chdir(file_name + "_files"):
        rar.extractall()
        rar.close()

