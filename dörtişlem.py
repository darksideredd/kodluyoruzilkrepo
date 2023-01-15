#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:07:08 2023

@author: yagmursahin
"""

sayi1=int(input("Bir sayı giriniz:"))
sayi2=int(input("Bir sayı giriniz:"))
islem=str(input("Bir işlem giriniz"))





if islem == "+":
    islem1=sayi1+sayi2
    print("Toplama işlemi: ", islem1)
    
if islem== "*":
    islem2=sayi1*sayi2
    print("Çarpma işlemi: ", islem2)

if islem== "-":
    islem3=sayi1-sayi2
    print("Çıkarma İşlemi: ", islem3)
    
if islem== "/":
    islem4=sayi1/sayi2
    print("Bölme İşlemi: ", islem)