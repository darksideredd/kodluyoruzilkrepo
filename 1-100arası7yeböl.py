#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:44:08 2023

@author: yagmursahin
"""
toplam=0
ort=0
for i in range(1,22):
    if i%7==0:
        toplam+=i
        #ort=toplam
        print(i)
        print()
print("toplamı: ",toplam)
#print("ortalaması: ", ort)
