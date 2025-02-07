"""
8.02.2025
Mavzu: INKAPSULYATSIA, KLASSNING XUSUSIYAT VA METODLARI
"""
from uuid import uuid4
class Avto:
    """ Avtomobil class"""
    __num_avto=0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """ Avtomobil xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto+=1
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """ MAshinaning km ga yana km qo'shamiz"""
        if km > 0:
            self.__km += km
        else:
            print("Mashinaga km kamaytirib bulmaydi")

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto


class Talaba:
    """ Talaba nomli klass yaratamiz"""
    __talabalar_soni=0
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__idraqam=uuid4()
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
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
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
