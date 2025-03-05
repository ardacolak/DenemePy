import numpy as np

"""print(np.eye(10))
print("************************************************************************")
print(np.arange(2,10))
print(np.arange(2,10,3))
print("************************************************************************")

print(np.ones(5))
print(np.zeros(6))
print(np.zeros((2,2)))

print(np.ones((9,8)))
print("************************************************************************")

print(np.linspace(0,20,4))
print(np.linspace(0,100,50))
print("************************************************************************")

print(np.random.randn(5))
print(np.random.randn(3,3))

# 10 dahil değil
print(np.random.randint(0,10))     
print(np.random.randint(0,10,4))  

print()

benimDizim = np.arange(30)
print(benimDizim)

print()

benimRandomDizim= np.random.randint(0,30,20)
print(benimRandomDizim)

print()

#Dizinin uzunluğu ile orantilidir. Mesela 30 uzunluğundaki dizi 6 ya 5 veya 5 e 6 reshape olabilir veya 3 e 10 gibi
print(benimDizim.reshape(6,5))
print()
print(benimRandomDizim.reshape(4,5))
print()
print()
print()
#MAX MIN

print(benimRandomDizim.max())
print(benimRandomDizim.min())
#Max ve minimum değerlerin kaçıncı satırda olduğunu gösterir.
print(benimRandomDizim.argmax())
print(benimRandomDizim.argmin())
print()
#Dizinin şeklini belirtir. Mesela bir matris için 5 e 6 olabilir.
print(benimRandomDizim.shape)


baskaDizi= np.arange(0,15)
print(baskaDizi) 

print(baskaDizi[5])

print(baskaDizi[3:5])

baskaDizi[3:8]=-5
print(baskaDizi)


#Biz eğer bir dizinin belli bir parcasını değistirirsek,dizinin kendide 
#değisir bunun için kopyası üstünde uygulama yapmalıyız.
DenemeDizi=np.arange(0,10)
DenemeDiziKopya=DenemeDizi
print(DenemeDiziKopya)
denemeDiziKopyaSlicing=DenemeDiziKopya[3:7]
print(denemeDiziKopyaSlicing)
denemeDiziKopyaSlicing[:]=99
print(denemeDiziKopyaSlicing)
print(DenemeDiziKopya)

"""
#MATRIX

benimListem = [[10,20,30],[20,30,40],[40,50,60]]
benimMatrixDizim=np.array(benimListem)
print()
print(benimMatrixDizim)
print()
print(benimMatrixDizim[0])

#Alttaki iki gösterim aynı sonucu verir.
print(benimMatrixDizim[1][2])
print(benimMatrixDizim[1,2])

#Birinci satirdan itibaren geri kalan satirlarin 2. indexini getirir.
print(benimMatrixDizim[1:,2])
#0. indexten itibaren tüm satirların 1.sütun indexinden sonraki tüm değerler
print(benimMatrixDizim[0:,1:])
print()
print(benimMatrixDizim[[0,2]])

#OPERASYONLAR 
dizi = np.random.randint(0,100,20)
print(dizi)
sonucDizi=dizi>24
print(sonucDizi)
print(dizi[sonucDizi])
print(dizi[dizi>24])

yeniDizi=np.arange(0,10)
print(yeniDizi)
print(yeniDizi+yeniDizi)
print(yeniDizi-yeniDizi)
print(yeniDizi*yeniDizi)
print(yeniDizi/yeniDizi)
print(np.sqrt(yeniDizi))
print()

