# -*- coding: utf-8 -*-
#author:jiayanzi
import os
import xml.etree.ElementTree as ET
import sys

dir=os.getcwd()
xmldir=os.path.join(dir,"data")

#遍历xml文件
class Exception(object):
    pass


def print(param, ex):
    pass


def AnalyseXml(name):
    xmlFilePath = os.path.abspath(xmldir+"\path.xml")
    try:
        tree = ET.parse(xmlFilePath)
        # 获得根节点
        root=tree.getroot()
        menu_find = root.find("webmenu/[name='%s']" % name)
        return menu_find.find("path_value").text
    except Exception as ex:
        print("Xml parse is Fail",ex)