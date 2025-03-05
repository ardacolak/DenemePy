import numpy as np
import pandas as pd

"""benimSozlugum = {"Arda" : "Colak", "Emre" : 40 , "Fatih" : "Pasa"}

print(pd.Series(benimSozlugum))
print()

benimYasim=[10,20,30,40]
benimAdim=["Arda","Emre","Fatih","Ertan"]
print(pd.Series(benimYasim,benimAdim))
print(pd.Series(data=benimYasim,index=benimAdim))

birinciDizi=pd.Series([10,20,30,40,50,],["a","b","c","d","e"])
ikinciDizi=pd.Series([2,3,4,5,6],["a","b","c","d","e"])
print(birinciDizi+ikinciDizi)

#Eger iki dizi birbirinde karşiligi yoksa nan döndürür.
birinciDizi=pd.Series([10,20,30,40,50,],["a","b","q","s","g"])
ikinciDizi=pd.Series([2,3,4,5,6],["a","b","c","d","e"])
print(birinciDizi+ikinciDizi)

#DATAFRAME

data=np.random.randn(4,3)
print(data)

print()

dataframe=pd.DataFrame(data=data)
print(dataframe)
print(dataframe[1])
print()
yeniDataFrame=pd.DataFrame(data=data,index=["Arda","Emre","Fatih","Neriman"],columns=["Yas","Maas","Saat"])
print(yeniDataFrame)
print()
print(yeniDataFrame["Yas"])
print()
#Satira erişmek için locate 
print(yeniDataFrame.loc["Arda"])
#Index bazlı erişim
print(yeniDataFrame.iloc[1])

yeniDataFrame["Yasin Karesi"]=yeniDataFrame["Yas"]+yeniDataFrame["Yas"]
print(yeniDataFrame)
print()
print(yeniDataFrame.drop("Maas",axis=1))
print(yeniDataFrame)
print("AYRIM")

#inplace true yapinca cikarma islemini direkt seriesten yapar,diğer türlü liste güncellenmez.Üstteki gibi
print(yeniDataFrame.drop("Maas",axis=1,inplace=True))
print(yeniDataFrame)

print(yeniDataFrame.drop("Fatih",axis=0))
print(yeniDataFrame)
print()
print(yeniDataFrame.loc["Fatih","Yas"])

print(yeniDataFrame[yeniDataFrame<0])

yeniDatatatatattaFrame=yeniDataFrame<0
print(yeniDataFrame<0)
print(yeniDataFrame[yeniDatatatatattaFrame])
print(yeniDatatatatattaFrame)
print(yeniDataFrame[yeniDataFrame["Yas"]<0])
print()
print()

print(yeniDataFrame)
print(yeniDataFrame.reset_index())
yeniDataFrame["Yeni Index"]=["Ard","Emr","Fat","Ner"]
print(yeniDataFrame)
print(yeniDataFrame.set_index("Yeni Index"))
print(yeniDataFrame)

print(yeniDataFrame["Yas"])
print()
print(yeniDataFrame.loc["Arda"])


sozlukVerisi={"Istanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"Izmir":[40,20,39]}
havaDurumuDataFrame=pd.DataFrame(sozlukVerisi)

print(havaDurumuDataFrame)
print()
print(havaDurumuDataFrame.dropna())
print(havaDurumuDataFrame.dropna(axis=1))

yenisözlük={"Istanbul":[30,29,np.nan],"Ankara":[20,np.nan,25],"Izmir":[40,20,39],"Fatsa":[98,np.nan,np.nan]}
yeniDataFrame=pd.DataFrame(yenisözlük)
print(yeniDataFrame)
print()
#Axis 1 de yani y ekseninde yani colonlarda 2 ve 2 den fazla nan olanları sil
print(yeniDataFrame.dropna(axis=1,thresh=2))

print(yeniDataFrame.fillna(123123123))
"""

maasSozluk={"Departman" : ["Yazilim","Pazarlama","Hukuk","Yazilim","Pazarlama","Hukuk"],
"Calisan Ismi":["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
"Maas": [100,100,200,300,400,500]
}
maasDataFrame=pd.DataFrame(maasSozluk)
print(maasDataFrame)
yeniGruplanmisDataFrame=maasDataFrame.groupby("Departman")
print(yeniGruplanmisDataFrame)
print(yeniGruplanmisDataFrame.describe())
print()
print(yeniGruplanmisDataFrame.count())
print()

print()
yeniGruplanmisDataFrameYas=maasDataFrame.groupby("Maas")
print()
print(yeniGruplanmisDataFrameYas.describe())