#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 13:26:55 2023

@author: yagmursahin
"""
while True:
    
         
     metin=input("Bir metin giriniz.. ")

     print("metindeki harf sayısı: ",len(metin))
     print("metindeki kelime sayısı: " ,len(metin.split()))
     print("metindeki boşluk sayısı:", metin.count(' '))
     print("Çıkış için 'çıkış' yazınız.. ")
     if metin=="çıkış":
         break
