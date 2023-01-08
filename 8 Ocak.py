#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:07:56 2023

@author: yagmursahin
"""

#OS (işletim sistemi)
'''
import os
print(os.name)

print(dir(os))
'''
'''
#zaman modülleri

from datetime import datetime
#print(dir(datetime))#alt fonksiyonları görmek için


simdi=datetime.now()
print(simdi)


if simdi.month ==1:
    print("Ocak")
else:
    print(" ")
print("Yıl :", simdi.year)
print(simdi.hour, ":", simdi.minute)

if simdi.day==8:
    print("Pazar")
else:
    print(" ")
'''
#Calendar modülü

'''
import calendar
takvim= calendar.TextCalendar(calendar.MONDAY)
print(takvim.prmonth(2023,1))
print(takvim.pryear(2023))

#Örnek -1: Son_odeme_tarihi:31.11.2022, ürünü ödeyen kişinin ödeme bilgilerini getiren program.
#Normal tarihte ödedi,ödemedi,geç ödedi

import subprocess
#print(dir(subprocess))
print(dir(subprocess))
'''


#hata mesajları
#1 kullanıcı/programcı Hataları(error)
#2 Program mantık hataları(bug)
#istisnalar(exception)
'''
try:
    sayi1= int(input("Bir sayı giriniz: "))
    sayi2= int(input("İkinci sayıyı giriniz: "))
    sonuc=(sayi1/sayi2)
    print(sonuc)
except ValueError:
    print("sayı giriniz..")
except ZeroDivisionError:
    print("Sıfır Girdiniz....")
finally:
    print(" ")
'''
'''
while True:
    sayi1=int(input("Birinci sayı giriniz..: "))
    if sayi1==0:
        print("Sıfır girdiniz..")
        break
    sayi2=int(input("İkinci sayıyı giriniz..:"))
    if sayi2==0:
        print("Sıfır girdiniz..")
        break
    else:
        ort=(sayi1+sayi2)/2
        print("Sonuç: ",ort)
'''
'''
#Önemli numara tanımla
onemlinumaralar={"112":"Hızır Acil",
                 "110":"İtfaiye",
                 "155":"Polis İmdat",
                 "156":"Jandarma İmdat",
                 }
#aradığımız bilgi
anahtar=input("Numarayı yazın")
deger=onemlinumaralar.get(anahtar, "Numara bulunamadı")
print(deger)
'''
'''
import turtle

turtle.setup(450,450)
turtle.title("Görsel Programlama")
turtle.bgcolor("yellow")
kalem=turtle.Turtle()
for x in range(8):
    
   kalem.forward(80)
   kalem.left(360/8)
turtle.done()
'''
import turtle
turtle.setup(450,450)
turtle.title("Geometrik Şekiller")
def geometriksekiller(kenarsayisi,birim=300,pensize=1):
    kalem.pensize(pensize)
    for i in range(kenarsayisi):
        kalem.forward(birim)
        kalem.left(360/kenarsayisi)
kalem=turtle.Turtle()
geometriksekiller(3,200,3)
turtle.done()
