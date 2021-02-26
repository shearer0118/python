# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 00:10:48 2021

@author: shear
"""

number = int(input("請輸入次數:"))

print("偶數:",end="" )
for i in range(1,number+1):
    if i%2 == 0:
        print(i,end=" ")
        
print("\n")

print("奇數:",end="")    
for i in range(1,number+1):       
    if i%2 == 1:
       print(i,end=" ")


        
