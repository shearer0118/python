# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 00:04:43 2021

@author: shear
"""
a=0
b=0
number = int(input("請輸入次數:"))
for i in range(1,number+1):
    if i%2 == 0:
        a+=i
    if i%2 == 1:
        b+=i
print("偶數總和:",a,"奇數總和:",b)