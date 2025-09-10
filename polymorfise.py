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
        self.pul = pul
        Talaba.univer += 1

    def __repr__(self):
        return 'this is the mirshodning clasi'

    def __eq__(self, value):
        return self.pul == value.pul
    
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
        self.students = []
    
    def __setitem__(self, index, name):
        self.students[index] = name

    def __getitem__(self, index):
        self.students[index]

    def add_fan(self, *qiymat):
        for sub in qiymat:
            if isinstance(sub, Talaba):
                self.students.append(sub)
            else:
                print('iltimow kiriting')
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
english = Fan('english', 'asliddin', 2006)


mirshod = Talaba('Mirshod', 'Normurodov', 'AD234234', 2006, 111)
mirshod2 = Talaba('Mirshod2', 'Normurodov', 'AD234234', 2006, 1111)
mirshod3 = Talaba('Mirshod3', 'Normurodov', 'AD234234', 2006, 1111)

matem.add_fan(mirshod, mirshod2, mirshod3)
matem.__setitem__(0, mirshod)
matem.__setitem__(1, mirshod2)
print(matem.__getitem__(1))

# sharof = Professor('Sharofiddin', 'Normurodov', 12323131, 1993)
# adminka = Admin('shahzoda', 'Normuhammedova', 12313232, 2008)

# asliddin = Shaxs('asliddin', 'norboyev', 12333231, 2006, 1000)

# mening_pulim = asliddin.get_pul()

# print(asliddin.__pul)
# print(mening_pulim)
# print(mirshod.get_talabalar_soni())
# print(matem.nom)
# # mirshod.fanga_yozil(matem)
# mirshod.remove_fan(matem)
# print(mirshod.get_fanlar())