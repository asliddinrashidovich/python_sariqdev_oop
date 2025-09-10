class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil, pul):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__pul = pul
    
    def get_pul(self):
        return self.__pul

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Talaba(Shaxs):
    """Talaba klassi"""
    univer = 0
    talabalar_soni = 10
    def __init__(self, ism, familiya, passport, tyil, pul):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil, pul)
        self.fanlar=[]
        Talaba.univer += 1

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni
    def get_fanlar(self):
        return self.fanlar
    
    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            return 'tugri'
        else:
            print('siz bu fanga royxatdan otmagansiz') 
class Fan:
    def __init__(self, nom, uquvchi, yil):
        self.uquvchi = uquvchi
        self.nom = nom 
        self.yil = yil
    

class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)
        self.ism = ism
    def get_name(self):
        return self.ism
    def get_info(self):
        info = f"{self.ism} {self.familiya}. bu professorniki "
        return info
    
class Admin(Professor):
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)
    def ban_user(self):
        return f"{self.ism} foydalanuvchi bloklandi"
    
matem = Fan('matematika', 'asliddin', 2006)
mirshod = Talaba('Mirshod', 'Normurodov', 'AD234234', 2006, 111)
mirshod2 = Talaba('Mirshod', 'Normurodov', 'AD234234', 2006, 111)
# sharof = Professor('Sharofiddin', 'Normurodov', 12323131, 1993)
# adminka = Admin('shahzoda', 'Normuhammedova', 12313232, 2008)

asliddin = Shaxs('asliddin', 'norboyev', 12333231, 2006, 1000)

mening_pulim = asliddin.get_pul()

# print(asliddin.__pul)
print(mening_pulim)
print(mirshod.get_talabalar_soni())
# print(matem.nom)
# # mirshod.fanga_yozil(matem)
# mirshod.remove_fan(matem)
# print(mirshod.get_fanlar())