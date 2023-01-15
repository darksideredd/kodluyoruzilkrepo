#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:59:27 2023

@author: yagmursahin
"""

not1=int(input("Birinci notu giriniz: "))
not2=int(input("İkinci notu giriniz: "))
ort=(not1+not2)/2
print("Ortalama",ort)
if 0>=ort<30:
    
    print("FF")    
if 30<=ort<50:
    print("DD")
if 50<= ort<70:
    print("CC")
if 70<=ort<85:
    print("BB")
if 85<=ort<100:
    print("AA")

if ort>=50:
    print("GEÇTİ!")
if ort<50:
    print("KALDI!")
    