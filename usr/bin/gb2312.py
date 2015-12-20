#!/usr/bin/env python 
#coding=utf-8 
s="中文" 

if isinstance(s, unicode): 
#s=u"中文" 
    s = s.encode('gb2312') + "in if"
    print s
else: 
#s="中文" 
    s = s.decode('utf-8').encode('gb2312') + "in else"
    print s


import win32api  
import win32con  
win32api.MessageBox(win32con.NULL, s , 'Hello', win32con.MB_OK)  
