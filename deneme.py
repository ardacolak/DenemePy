#Kullanıcıdan değer alma ve yazdırma
"""vize=int(input("Lütfen vize notunuzu giriniz:"))
final=int(input("Lütfen final notunuzu giriniz:"))
ortalama=(vize+final)/2

print("*0"*30)
print(f"Vize puaniniz: {vize}\n final puaniniz: {final}\n ortalamaniz: {int(ortalama)}")
 """  # shift alt a


#Listeler
"""listeler=["Arda","Colak","Kimdir",22]
listeler.append("Emre")

print(listeler)

listeler[3]=23
print(listeler)

listeler[0:2]=[]
print(listeler)
"""

#Demetler listelerden tek farkı güncellenemez olmasıdır.
"""deneme=("Arda","Çolak","Kimdir",22)
print(deneme[0])

# deneme[0]="Emre"  Hatalı kod  // Demetler güncellenemez.
"""
"""
for i in range(3):
    sifre=input("Bir sifre giriniz:")
    if not sifre:
        print("Bu alan bos birakilamaz")
    elif len(sifre) in range(3,8):
        print("Yeni sifreniz ",sifre)
        break
    elif i==2:
        print("Şifreyi 3 kez yanlış girdiniz , 15 dakika bekleyiniz")
    else:
        print("Sifreniz 3 den kısa veya 8 den uzun")
"""

"""metin = input("Bir şeyler yaz:")
print(metin)

for i in metin.split():
   print(i)
"""

#Fonksiyonlar

"""def kullanici(isim,soyisim="Ardadadada",yas="25"):
    print(f"İsim:{isim}\n Soyisim:{soyisim}\n Yas:{yas}")

kullanici("Arda")
"""

#Telefon Rehberi

telefon_Rehberi=dict()

def kisiEkle(x):
    numara_isim=input("Lütfen bir isim giriniz:")
    numara_no=input("Lütfen bir telefon numarasi giriniz:")
    x=telefon_Rehberi.setdefault(numara_isim,numara_no)
    print(f"{numara_isim} adli kişi telefon listesine eklendi")

def kisiSil(x):
    print("Kisi silme ekrani")
    silinecekKisi=input("Silinecek kisinin adini giriniz:")
    x=telefon_Rehberi.pop(silinecekKisi)
    input("Devam edilsin mi?")

def rehberGöster(x):
    kisi_Sayisi=len(x)
    print(f"Telefondaki kişi sayisi {kisi_Sayisi}")
    for i,j in x.items():
        print(i, ":" ,j)
    input("Devam edilsin mi?")


kisiEkle(telefon_Rehberi)
rehberGöster(telefon_Rehberi)
kisiEkle(telefon_Rehberi)
kisiSil(telefon_Rehberi)
rehberGöster(telefon_Rehberi)
