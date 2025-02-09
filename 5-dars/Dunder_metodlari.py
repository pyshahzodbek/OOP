"""
8.02.2025
Mavzu: DUNDER METODLAR
"""
from uuid import uuid4
class Avto:
    __num_avto=0
    """ Avtomobil class"""
    def __init__(self,make,model,rang,yil,narh):
        """ Avtomobil xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        Avto.__num_avto+=1
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} ,{self.model},{self.rang}"
    def __eq__(self,boshqa_avto):
        return self.narh==boshqa_avto.narh
    def __lt__(self,boshqa_avto):
        """ Kichik"""
        return self.narh<boshqa_avto.narh
    def __le__(self,boshqa_avto):
        """ Kichik yoki teng """
        return self.narh<=boshqa_avto.narh



class AvtoSalon:
    """ Avtomobil salon class"""
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def add_avto(self,*qiymat):
        for avto in qiymat:
         if isinstance(avto,Avto):
            self.avtolar.append(avto)
        else:
            print("Avto kiriting.")
    def __len__(self):
        return len(self.avtolar)
    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self, index, qiymat):
        if isinstance(qiymat, Avto):
            self.avtolar[index] = qiymat
    # def __add__(self, qiymat):
    #     if isinstance(qiymat, AvtoSalon):
    #         yangi_salon=AvtoSalon(f"{self.name}  {qiymat.name}")
    #         yangi_salon.avtolar=self.avtolar+qiymat.avtolar
    #         return yangi_salon
    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon=AvtoSalon(f"{self.name}  {qiymat.name}")
            yangi_salon.avtolar=self.avtolar+qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat,Avto):
            self.add_avto(qiymat)
        else:
            print(f"Avtosalon ga {type(qiymat)} qo'shib bulmaydi")

    def __call__(self,*param):
        if param:
            for avto in param:
                self.add_avto(avto)
        else:
             return [avto for avto in self.avtolar]

class Fan:
    def __init__(self,fan):
        self.fan=fan
        self.fanga_yizilgan=[]
    def __getitem__(self, index):
        return self.fanga_yizilgan[index]
    def add_student(self,talaba):
        if isinstance(talaba,Talaba):
            return self.fanga_yizilgan.append(talaba)
        else:
            print("Talaba kiriting.")
    def __repr__(self):
        return f"Fanga yozilgan talabalar:{self.fanga_yizilgan}"
    def __setitem__(self, index,talaba):
        if isinstance(talaba,Talaba):
            self.fanga_yizilgan[index]=talaba
        else:
            print("Talaba kiriting.")
    def __add__(self, other):
        if isinstance(other,Talaba):
          self.fanga_yizilgan.append(other)
        return self
    def __sub__(self, other):
        if isinstance(other,Talaba):
            self.fanga_yizilgan.remove(other)
        return self
    def __call__(self,*parametr ):
        if parametr:
            for i in parametr:
                self.add_student(i)
        else:
            return [i for i in self.fanga_yizilgan]




class Talaba:
    """ Talaba nomli klass yaratamiz"""
    __talabalar_soni=0
    def __init__(self, ism, familiya, tyil,bosqich):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__idraqam=uuid4()
        self.bosqich=bosqich
        Talaba.__talabalar_soni+=1
    def get_talabalar_soni(self):
        return self.__talabalar_soni
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}.{self.tyil} yilda tug'ilgan."
    def get_name(self):
        return self.ism
    def get_lestname(self):
        return self.familiya
    def get_Fulname(self):
        return f"{self.ism} {self.familiya}"
    def get_age(self,yil):
        return yil-self.tyil
    def talaba_id(self):
        return self.__idraqam
    @classmethod
    def get_talabalar_son(cls):
        return cls.__talabalar_soni
    def get_bosqich(self):
        return self.bosqich
    def __ge__(self,boshqa_talaba):
        return self.bosqich>=boshqa_talaba.bosqich
    def __gt__(self,boshqa_talaba):
        return self.bosqich>boshqa_talaba.bosqich
    def __eq__(self, other):
        return self.bosqich==other.bosqich

    def __repr__(self):
        return f"Talaba: {self.ism} {self.familiya} "
    def __lt__(self, boshqa_talaba):
        return self.bosqich<boshqa_talaba.bosqich


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    __shaxs_soni=0

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.__passport = passport
        self.tyil = tyil
        Shaxs.__shaxs_soni+=1

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f" {self.tyil}-yilda tug`ilgan"
        return info
    def get_pasport(self):
        return self.__passport

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    @classmethod
    def get_shaxs_soni(cls):
        return cls.__shaxs_soni
    def __repr__(self):
        return f"Shaxs: {self.ism} {self.familiya} "





