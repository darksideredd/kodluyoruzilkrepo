#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:40:56 2023

@author: yagmursahin
"""
toplam=0
sayi1=int(input("Birinci Sayıyı Giriniz: "))
sayi2=int(input("İkinci Sayıyı Giriniz: "))
for x in range(sayi1,sayi2+1):
    toplam+=x
print(toplam)