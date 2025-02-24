class Hayvan():
    def __init__(self,isim,yas):
        print("init edildi")
        self.isim=isim
        self.yas=yas

class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self,"Esek",3)
        print("Merhava Kedi")

kedi1=Kedi()
print(f"Ad {kedi1.isim},,yas {kedi1.yas}")