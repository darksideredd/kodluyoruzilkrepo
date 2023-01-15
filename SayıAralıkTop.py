#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:35:34 2023

@author: yagmursahin
"""

toplam=0
sayi1=int(input("bir sayı giriniz: "))
sayi2=int(input("bir sayı giriniz: "))

for c in range(sayi1,sayi2+1):
    toplam+=c
print(toplam)
    