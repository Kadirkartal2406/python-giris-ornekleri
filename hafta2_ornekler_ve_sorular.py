# 1. Kullanıcıdan Alınan Metni Ekranda Gösterme
metin = input("Bir metin girin: ")
print("Girilen metin:", metin)

# 2. Kullanıcının Girdiği İki Sayıyı Toplama
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
print("Toplam:", sayi1 + sayi2)

# 3. Girilen Sayının Tek veya Çift Sayı Olduğunu Belirleme
sayi = int(input("Bir sayı girin: "))
print("Tek" if sayi % 2 != 0 else "Çift")

# 4. İki Sayı ile İşlem Yapan Basit Hesap Makinesi
a = float(input("Bir sayı girin: "))
b = float(input("Bir sayı girin: "))
islem = input("İşlem seçin (+, -, *, /): ")
if islem == '+':
    print(a + b)
elif islem == '-':
    print(a - b)
elif islem == '*':
    print(a * b)
elif islem == '/':
    if b != 0:
        print(a / b)
    else:
        print("Hata: Sıfıra bölünemez!")
else:
    print("Geçersiz işlem!")

# 5. Hesap Makinesinde Kullanıcı Hatalarını Önleme
while True:
    try:
        x = float(input("Bir sayı girin: "))
        y = float(input("Bir sayı girin: "))
        break
    except ValueError:
        print("Hatalı giriş! Lütfen sayı girin.")

# 6. +/- İşaretine Her Basıldığında Sayıyı Arttırma/Azaltma
sayi = 0
for i in range(3):
    islem = input("+/- girin: ")
    if islem == '+':
        sayi += 1
    elif islem == '-':
        sayi -= 1
    print("Güncel sayı:", sayi)

# 7. +10 ile -10 Arasındaki Sayıları Ekrana Yazma
for i in range(-10, 11):
    print(i, end=" ")
print()

# 8. Metindeki Her Harfin Arasına Virgül Koyma
metin = "Python"
print(",".join(metin))

# 9. 1 ile 100 Arasında Rastgele 10 Tam Sayı Üretip Dizi İçine Ekleme
import random
liste = [random.randint(1, 100) for _ in range(10)]
print(liste)

# 10. -100 ile +100 Arasındaki 5’e Tam Bölünen Sayıları Yan Yana Gösterme
for i in range(-100, 101):
    if i % 5 == 0:
        print(i, end=" ")
print()

# 11. Üç Adet Sayıyı Karşılaştırıp Sıralama
nums = [int(input(f"{i+1}. sayıyı girin: ")) for i in range(3)]
nums.sort()
print("Sıralı:", nums)

# 12. Faktöriyel Hesaplama ve Açılımını Yazdırma
n = int(input("Bir sayı girin: "))
faktoriyel = 1
aciklama = ""
for i in range(1, n+1):
    faktoriyel *= i
    aciklama += f"{i}*" if i != n else f"{i}"
print(f"{n}! = {aciklama} = {faktoriyel}")

# 13. Metindeki İlk Kelime ile Son Kelimeyi Bulma
metin = input("Bir cümle girin: ")
kelimeler = metin.split()
print("İlk kelime:", kelimeler[0], "Son kelime:", kelimeler[-1])

# 14. Girilen Sayıların Toplamını ve Ortalamasını Bulma
sayilar = list(map(float, input("Sayıları aralarında boşlukla girin: ").split()))
print("Toplam:", sum(sayilar))
print("Ortalama:", sum(sayilar)/len(sayilar))

# 15. Büyük Harfleri Küçük Harflere, Küçük Harfleri Büyük Harflere Dönüştürme
metin = input("Bir metin girin: ")
print(metin.swapcase())

# 16. Personel Maaşından Yüzdesel Zam Hesaplama
maas = float(input("Maaşı girin: "))
zam = float(input("Zam yüzdesini girin: "))
print("Yeni maaş:", maas * (1 + zam/100))

# 17. Sayı Değerlerinin Toplamını Hesaplama
sayilar = [1, 2, 3, 4, 5]
print("Toplam:", sum(sayilar))

# 18. Kullanıcının Sonsuz Sayıda Girdiği Değerlerin Yanına Tek/Çift Yazma
while True:
    try:
        s = input("Sayı girin (çıkmak için q): ")
        if s.lower() == 'q':
            break
        s = int(s)
        print(s, "Çift" if s % 2 == 0 else "Tek")
    except ValueError:
        print("Hatalı giriş!")

# 19. 1 ile 300 Arasındaki Sayılardan 11 Sayısına Bölünenleri Bulma
print([i for i in range(1, 301) if i % 11 == 0])

# 20. Mutlak Sistemde Sınıfı Geçmek İçin Gereken Final Notunu Hesaplama
vize = float(input("Vize notu: "))
ortalama_gereken = 50
final_gereken = (ortalama_gereken - 0.4*vize)/0.6
print("Geçmek için final notu:", final_gereken)

# 21. Üç Kenarı Girilen Üçgenin Alanını Hesaplama
a = float(input("a kenarı: "))
b = float(input("b kenarı: "))
c = float(input("c kenarı: "))
s = (a+b+c)/2
alan = (s*(s-a)*(s-b)*(s-c))**0.5
print("Üçgenin alanı:", alan)

# 22. Metindeki Sesli Harf Sayısını Hesaplama
metin = input("Metin girin: ")
sesli = "aeıioöuüAEIİOÖUÜ"
print("Sesli harf sayısı:", sum(1 for harf in metin if harf in sesli))

# 23. Her Sayıyı Kendisi Kadar Yan Yana Yazdırma
n = int(input("Bir sayı girin: "))
for i in range(1, n+1):
    print(str(i)*i)

# 24. Tekrarsız Rastgele Sayı Üretme
liste = random.sample(range(1, 101), 10)
print(liste)

# 25. Asal Çarpanlarını Bulma
sayi = int(input("Bir sayı girin: "))
i = 2
asal_carpanlar = []
while i <= sayi:
    if sayi % i == 0:
        asal_carpanlar.append(i)
        sayi //= i
    else:
        i += 1
print("Asal çarpanlar:", asal_carpanlar)

# 26. Metindeki En Uzun Kelimeyi Bulma
metin = input("Bir cümle girin: ")
kelimeler = metin.split()
uzun_kelime = max(kelimeler, key=len)
print("En uzun kelime:", uzun_kelime)

# 27. Girilen Bir Notun Harf Karşılığını Bulma
notu = float(input("Notu girin: "))
if notu >= 90:
    harf = "AA"
elif notu >= 85:
    harf = "BA"
elif notu >= 80:
    harf = "BB"
elif notu >= 75:
    harf = "CB"
elif notu >= 70:
    harf = "CC"
elif notu >= 65:
    harf = "DC"
elif notu >= 60:
    harf = "DD"
elif notu >= 50:
    harf = "FD"
else:
    harf = "FF"
print("Harf notu:", harf)

# 28. Cümledeki Her Kelimeyi Tersten Yazdırma
metin = input("Bir cümle girin: ")
print(" ".join(k[::-1] for k in metin.split()))

# 29. Metni Mors Alfabesine Çevirme
mors = {
    "A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..",
    "J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.",
    "S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
    "1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----",
    " ":"/"
}
metin = input("Metin girin: ").upper()
print(" ".join(mors.get(harf, "") for harf in metin))

# 30. Kümülatif Toplam Hesaplama
sayilar = list(map(int, input("Sayıları aralarında boşlukla girin: ").split()))
kumulatif = []
toplam = 0
for s in sayilar:
    toplam += s
    kumulatif.append(toplam)
print("Kümülatif toplam:", kumulatif)
