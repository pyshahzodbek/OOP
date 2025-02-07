"""
05.02.2025
2-dars
Mavzu:Obyekt bilan ishlash
"""
# class Talaba:
#     """ Talaba nomlii klass yaratamiz."""
#     def __init__(self,ism,familya,tyil):
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#         self.bosqich=1
#     def get_info(self):
#         return f"{self.ism}  {self.familya}, AX-2401 guruhning  {self.bosqich}-bosqich talabasi."
#     def get_bosqich(self,bosqich):
#         self.bosqich=bosqich
#     def update_bosqich(self):
#         self.bosqich+=1
#
# talaba1=Talaba("Shahzod","Ravshanov",2006)
# talaba1.get_bosqich(1)
# print(talaba1.get_info())
# talaba1.update_bosqich()
# print(talaba1.get_info())
# class Fan:
#     def __init__(self,nomi):
#         self.nomi=nomi
#         self.talabalar_soni=0
#         self.talabalar=[]
#     def add_student(self,talaba):
#         """ fanga talablarni qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni+=1
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
# matematika=Fan("Hisob")
# talaba1=Talaba("Shahzod","Ravshanov",2006)
# talaba2=Talaba("Dilshod","Ochilov",2007)
# talaba3=Talaba("Baxrom","Kurbanov",2008)
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
# print(matematika.talabalar_soni)
# print(matematika.talabalar)
# mat_talabalar=matematika.get_students()
# print(mat_talabalar)
# dir(Talaba)
# print(dir(Talaba))
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__" )is False]
# #__dict__ metodi
# print(talaba1.__dict__)


# Amaliyot
class Avto:
    def __init__(self,model,rang,korobka,narh):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narh=narh
        self.kilometr=0
    def get_model(self):
        return self.model
    def get_rang(self):
        return self.rang
    def get_korobka(self):
        return self.korobka
    def get_narh(self):
        return self.narh
    def get_kilometr(self):
        return self.kilometr
    def get_info(self):
        return (f"Modeli:{self.model}, Avto rangi:"
                f"{self.rang}, Korobka:{self.korobka}"
                f", Narxi:{self.narh}, Yurgani:{self.kilometr}km")
    def upadate_km(self,kilometr):
        self.kilometr+=kilometr
avto=Avto("BMW","Qora","avtomat",50000)
print(avto.get_info())
avto.upadate_km(100)
print(avto.get_info())

class Avtosalon:
    def __init__(self,salon_nomi,manzil,sotuv_avto):
        self.salon_nomi=salon_nomi
        self.manzil=manzil
        self.sotuv_avto=sotuv_avto
        self.avtolar=[]
    def add_avto(self,yangi_avto):
        self.avtolar.append(yangi_avto)
    def get_info(self):
        return f"{self.salon_nomi} {self.manzil} {self.sotuv_avto}"
    def get_avtolar(self):
        return [avtolar.get_info() for avtolar in self.avtolar]

avto1=Avtosalon("Toshkent Avto","Toshkent",'malibu')
avto2=Avto("BMW","Qora","avtomat",50000)
avto1.add_avto(avto2)
print(avto1.get_info())
print(avto1.add_avto(avto2))
print(avto1.get_avtolar())
print(see_methods(Avtosalon))
print(avto1.__dict__)

