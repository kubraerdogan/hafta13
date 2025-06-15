class hesap:
    def __init__(self,say1,say2):
        self.say1=say1
        self.say2=say2

    def topla(self):
        sonuc1= self.say1+self.say2
        return sonuc1

    def cikar(self):
        sonuc2= self.say1-self.say2
        return sonuc2

    def carp(self):
        sonuc3= self.say1*self.say2
        return sonuc3

    def bol(self):
        sonuc4= self.say1/self.say2
        return sonuc4

    def yazdir(self):
        print("say1",self.say1, "say2",self.say2,"sayıların toplamı:",self.topla(),"sayıların çıkar:", self.cikar(),"sayların carbımı", self.carp(),"sayıların bölmesi:", self.bol())

A =hesap(5,3)
A.yazdir()