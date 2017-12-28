#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : xtrdb.net
# File   : 匿名函数.py
# Time   : 2017/12/21


import psutil
import pprint

mem_info = {}
date = psutil.virtual_memory()
mem_info["total"] = date[0]/1024/1024/1024
mem_info["available"] = date[1]/1024/1024/1024

#print(mem_info)
html_str= "<table border='1'><tr><td>status</td><td>data</td></tr>"

for i,j in mem_info.items():
    html_str += "<tr><td>%s</td><td>%.2f</td></tr>" %(i,j)

html_str +="</table>"

with open("mem_info.html",'w') as f:
    f.write(html_str)

