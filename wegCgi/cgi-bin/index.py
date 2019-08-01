#!/usr/bin/python3
# -*- coding: utf-8 -*-
import cgi, cgitb
cgitb.enable()

print("Content-Type: text/html")
print()


fs = cgi.FieldStorage()
inputs = {}
#将cgi从web获取到的数据存入字典inputs
for key in fs.keys():
    inputs[key] = fs[key].value
for k,v in inputs.items():
    print(k,'-->',v)
    print('<br/>')