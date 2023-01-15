#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:20:17 2023

@author: yagmursahin
"""
sekil= str(input("Alan hesabı için geometrik şekil seçiniz: "))
if sekil== "çember":
    pi=3
    r=int(input("yarı çap değeri giriniz: "))
    cember_alan=pi*(r*r)
    print("çember alanı: ", cember_alan)
    
if sekil== "üçgen":
    taban=int(input("taban değeri giriniz: "))
    h=int(input("yükseklik değeri giriniz: "))
    ucgen_alan=(taban*h)/2
    print("üçgen alanı: ", ucgen_alan)
    
if sekil== "kare":
    kenar=int(input("kenar değeri giriniz: "))
    kare_alan=kenar*kenar
    print("kare alanı: ", kare_alan)
    
if sekil== "dikdörtgen":
    k_kenar=int(input("kısa kenar değeri giriniz: "))
    u_kenar=int(input("uzun kenar değeri giriniz: "))
    dik_alan=k_kenar*u_kenar
    
