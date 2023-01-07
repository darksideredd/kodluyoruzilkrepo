#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 13:35:13 2023

@author: yagmursahin
"""
#continue atla
'''
for x in range(1,6):
    if x==2 or x==4:
        continue
    print("sayılar :",x)
''' 
'''
x=0   
while x<6:
    x=x+1
    if x==2 or x==4:
        continue
    print("sayılar: ",x)
'''
'''
for x in range(1,20):
    if x%2==0:
        continue#kurala göre atla(2'ye bölünenleri atla..)
    print("Sayılar: ",x)
'''
#dosya işlemleri
#1 dosya okuma
#py dosyası ve txt aynı klasörde olması gerekiyor.
'''
dosya= open("deneme.txt") #dosyayı açtı
belge=dosya.read() #dosyayı okudu
print(belge) #dosyayı yazdırdı
dosya.close() #dosyayı kapattı
dosya=open("deneme.txt","w")
dosya.write("Veri girdim")
dosya.close()
print("okunuyor..")


dosya=open("deneme.txt","r")
print(dosya.read())
dosya.close()
'''
'''
dosya=open("deneme.txt","w")
dosya.write("SAYILAR alt alta")
for x in range(1,11):
    dosya.write("\n" +str(x))
print(dosya)
dosya.close()
'''
dosya=open("deneme.txt","w")
dosya.write("SAYILAR yan yana")
for x in range(1,11):
    dosya.write(" " +str(x))
print(dosya)
dosya.close()

#1-100 arasındaki tek sayları yazdıran py yi txt e yaz
dosya=open("deneme.txt","w")
dosya.write("sayılar 1-100 arası tekler")
for x in range(1,100):
    if x%2==0:
        continue#kurala göre atla(2'ye bölünenleri atla..)
    dosya.write(" " +str(x))
print(dosya) 
dosya.close()        
'''
dosya=open("deneme.txt","w")
dosya.write("sayılar")
sayi1=int(input("başlangıç sayısını giriniz: "))
sayi2=int(input("bitiş sayısını giriniz: "))
artis=int(input("artış miktarını giriniz: "))

for x in range(sayi1,sayi2,artis):
    dosya.write("\n " +str(x))
print(dosya)
dosya.close()
''' 

import socket;
check= input("Ip adresini öğrenmek istiyor musunuz? (y/n): ");
if check== "n":
    exit();
else:
    print("\nIP adresiniz: ",end="");
    print(socket.gethostbyname(socket.gethostname()));

from socket import*


x=gethostbyname(gethostname())
print(x)

