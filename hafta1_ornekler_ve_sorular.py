# -*- coding: utf-8 -*-
# ==========================================================
#  VERİ BİLİMİNE GİRİŞ - 1. HAFTA
#  Python Giriş - Örnek Kodlar ve Test Soruları
#  Hazırlayan: Kadir Kartal
# ==========================================================


# ---- 1. PRINT FONKSİYONU ----
print("sinan")
print("sinan", "başarlan", "T", "B", "M", sep='.')

# ---- 2. DEĞİŞKENLER VE VERİ TİPLERİ ----
a = "ali"
b = 5
print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>

# ---- YORUM SATIRLARI ----
# Tek satırlık yorum
"""
Çoklu
yorum satırı
"""

# ---- VERİ TİPLERİ ----
a = 5       # integer
b = "sinan" # string
c = 3.5     # float
d = 'k'     # karakter

# ---- 3. VERİ YAPILARI (LIST, TUPLE, DICTIONARY, SET) ----
liste1 = [1, 3, 3, 5, 4, 5, 4, "ali", "canan"]
print(liste1[0])  # index 0'dan başlar
print(len(liste1))
print(dir(liste1))

liste2 = [1, 3, 3, 5, 4, 5, 4]
liste2.sort()
print(liste2)
liste2[0] = 100000  # mutable yapı
print(liste2)

liste2.pop()
liste2.append(25)
liste2.insert(2, "25")
print(liste2)

demet = ("ali", "ayşe")  # tuple immutable
print(demet)
print(len(demet))
print(demet.count("ali"))
print(demet.index("ali"))

# ---- 4. FONKSİYON TANIMLAMA ----
def selam():
    print("selam")

def selamGotur(isim):
    print("selam", isim)

selam()
selamGotur("sinan")

def topla(a, b):
    c = a + b
    return c

print("Toplam:", topla(3, 5))

def kareal(a):
    return a * a

print("4 sayısının karesi:", kareal(4))

# ---- 5. LAMBDA FONKSİYONU ----
kare = lambda x: x * x
print(kare(6))

toplama = lambda x, y: x + y
print(toplama(5, 5))

# ---- 6. MATH, RANDOM VE TIME MODÜLLERİ ----
import math
import random
import time

print(math.pow(2, 3))
print(math.sqrt(16))
print(math.sin(60))

rastgele = random.randint(1, 100)
print("Rastgele sayı:", rastgele)

# ---- 7. BASİT TAHMİN OYUNU ----
rastgele = random.randint(1, 20)
hak = 5

while hak > 0:
    tahmin = int(input("1-20 arası bir sayı tahmin et: "))
    if tahmin == rastgele:
        print("Tebrikler, doğru tahmin!")
        break
    elif tahmin < rastgele:
        print("Daha büyük sayı gir.")
    else:
        print("Daha küçük sayı gir.")
    hak -= 1
    if hak == 0:
        print("Hak bitti! Sayı:", rastgele)

# ---- 8. SINIFLAR (OOP) ----
class Calisan:
    pass

calisan1 = Calisan()

# ---- 9. ATTRIBUTES (NİTELİKLER) ----
class Arac:
    renk = "sarı"
    model = "jeep"
    marka = "kia"

a1 = Arac()
print(a1.marka)
a1.marka = "BMW"
print(a1.marka)

# ---- 10. METOTLAR ----
class Kare:
    kenar = 10

    def alan(self):
        print("Alan:", self.kenar * self.kenar)

k1 = Kare()
k1.alan()

# ---- 11. YAPICI (CONSTRUCTOR) ----
class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def getYas(self):
        return self.yas

    def getAd(self):
        return self.isim

h1 = Hayvan("dog", 2)
print("h1:", h1.getAd(), h1.getYas())

# ---- 12. OOP İLE BASİT HESAP MAKİNESİ ----
class Makine:
    def __init__(self, a, b):
        self.deger1 = a
        self.deger2 = b

    def topla(self):
        return self.deger1 + self.deger2

    def carp(self):
        return self.deger1 * self.deger2

    def cikar(self):
        return self.deger1 - self.deger2

    def bol(self):
        return self.deger1 / self.deger2

m = Makine(5, 2)
print("Toplama:", m.topla(), "Çarpma:", m.carp())

# ---- 13. KAPSÜLLEME (ENCAPSULATION) ----
class Banka:
    def __init__(self, isim, para, adres):
        self.__isim = isim
        self.__para = para
        self.__adres = adres

    def getPara(self):
        return self.__para

    def setPara(self, miktar):
        self.__para = miktar

hesap1 = Banka("Sinan", 1000, "İstanbul")
print("Para:", hesap1.getPara())
hesap1.setPara(500)
print("Yeni para:", hesap1.getPara())

# ---- 14. MİRAS ALMA (INHERITANCE) ----
class Animal:
    def __init__(self):
        print("Hayvan sınıfı")

    def sesCikar(self):
        print("hav, miyav, vak...")

class Kedi(Animal):
    def __init__(self):
        super().__init__()
        print("Kedi sınıfı oluşturuldu")

    def sesCikar(self):
        print("Miyav")

k = Kedi()
k.sesCikar()

# ---- 15. SOYUT SINIF (ABSTRACT CLASS) ----
from abc import ABC, abstractmethod

class Animal2(ABC):
    @abstractmethod
    def yurume(self): pass

    @abstractmethod
    def kosma(self): pass

class Kus(Animal2):
    def yurume(self):
        print("Kuşlar pek yürümez")

    def kosma(self):
        print("Kuşlar pek koşmaz da")

b = Kus()
b.yurume()
b.kosma()

# ---- 16. POLYMORPHISM (ÇOK BİÇİMLİLİK) ----
class Hayvanlar:
    def __init__(self, isim):
        self.isim = isim
    def tepki(self):
        raise NotImplementedError("Hata")

class Kedi2(Hayvanlar):
    def tepki(self):
        return "Miyav!"

class Kopek(Hayvanlar):
    def tepki(self):
        return "Hav! Hav!"

hayvanlar = [Kedi2("Boncuk"), Kopek("Karabaş")]
for h in hayvanlar:
    print(h.isim, ":", h.tepki())

# ==========================================================
#  TEST / KLASİK SORULAR - CEVAPLAR
# ==========================================================
# 1) Hangi keyword ile sınıf tanımlanır? → B) class
# 2) Hangisi ile python kodu yazılamaz? → E) chromepy
# 3) Nesneye dayalı programlama ile ilgili değildir? → C) Bir sınıftan birden çok nesne türetilemez.
# 4) Python dosya uzantısı hangisidir? → B) .py
# 5) Fonksiyon oluşturmak için kullanılan anahtar kelime? → B) def
# 6) Yeni nesne oluşturmak için gerekli yapı? → C) constructors
# 7) Encapsulation tanımı? → C) Veri ve metotların dış erişime kapatılmasıdır.
# 8) A sınıfı B’den mi miras alır? → B) B sınıfı A’dan miras alır.
# 9) Soyut sınıf (abstract class) tanımı? → B) OOP'de nesnesi olmayan sınıflara verilen isimdir.
# 10) a.sesVer() çıktısı → ses çıkarırlar
#     k.sesVer() çıktısı → miyav
# ==========================================================
