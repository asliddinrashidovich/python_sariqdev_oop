# class Talaba:
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#     def getInfo(self):
#         print(f"ismim {self.name}, familiyam {self.lastname}, yoshim {self.age} da")

#     def getname(self):
#         return self.name
    
#     def getYear(self,yil):
#         return yil - self.age

# talaba1 = Talaba('asliddin', 'norboyev', 19)
# talaba2 = Talaba('asliddi2n', 'norboyev', 19)

# print(talaba2.name)
# print(talaba2.getYear(2025))

class Avto:
    def __init__(self, model, rang, karobka, narh):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.kilometr = 2000

    def get_info(self):
        return f"mening orzuyimdagi mashina {self.model}, {self.rang} dagisini yoqtiraman, karobka {self.karobka} bo'lsa yaxshi, narxi {self.narh}"
    
    def update_km(self, klm): 
        self.kilometr += klm
        return self.kilometr

class Avtosalon:
    def __init__(self, nomi, manzil, avtomobillar):
        self.nomi = nomi
        self.manzil = manzil
        self.avtomobillar = avtomobillar
        self.avtomobillarsoni = 0
    def set_cars(self, mashina):
        self.avtomobillar.append(mashina)
        self.avtomobillarsoni += 1


bydhan = Avto('BYD Han plus', 'black', 'avtomat', 24000)
rentcar = Avtosalon('Rentcar', 'Toshkent', ['damas', 'kobalt', 'ravon'])

# print(bydhan.get_info())
# print(bydhan.update_km(1000))

rentcar.set_cars('malibu')
print(rentcar.avtomobillar)

print(bydhan.__dict__)