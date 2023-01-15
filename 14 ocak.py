#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 12:58:34 2023

@author: yagmursahin
"""
#fonksiyonlar

def mesaj1():
    print("Hoş Geldiniz...")
    
#mesaj1()
a=5
b=6
c=a+b
def topla(a,b):
    print(c)
    
#topla(a, b)


'''
x= int(input("bir sayı giriniz: "))
def carp(x):
    return x*2
    print(x)

carp(x)
'''
#İç içe fonksiyon
def uclecarp(a):
    print("Fonksiyon çalıştı..")
    return a*3
def ikiyle_topla(a):
    return a+2
    
#print(ikiyle_topla(uclecarp(10)))
#global alan local alan açıklama örneği:
a=10
def fonksiyon():
    a=2
    #print(a)
    
fonksiyon()
#print(a)
'''
#4 işlemi fonksiyon kullanarak yazınız..
print("..Hesap Makinesi..")
sayi1=int(input("Birinci sayiyı giriniz: "))
sayi2=int(input("İkinci sayiyı giriniz: "))
islem=input("işlem seçiniz: ")


def top():
        top=0  
        top=sayi1+sayi2
        print(top)
        
if islem=="+":
   print("Toplamı: ")
   top()

'''
#5 adet notun ortalamasını ve toplamanı bulan phyton prog fonk ile yaz.

s
    
    
    
    
    
    

