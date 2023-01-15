#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 14:57:08 2023

@author: yagmursahin
"""
'''
sayi1=int(input("Not giriniz.."))
sayi2=int(input("Not giriniz.."))
sayi3=int(input("Not giriniz.."))
sayi4=int(input("Not giriniz.."))
sayi5=int(input("Not giriniz.."))

def toplama():
    toplama=0
    ort=0
    toplama=sayi1+sayi2+sayi3+sayi4+sayi5
    ort=toplama/5
    print(ort)
toplama()
'''
#5 değerin  ortalamasını bulma

sinav=0
sinav= int(input("Not giriniz: "))
sinav1= int(input("Not giriniz: "))
sinav2= int(input("Not giriniz: "))
sinav3= int(input("Not giriniz: "))
sinav4= int(input("Not giriniz: "))
liste=[sinav,sinav1,sinav2,sinav3,sinav4]
    
def ortalama():
         ortalama= sum(liste)/len(liste)
         return ortalama
#print("Ortalama: ", ortalama())



