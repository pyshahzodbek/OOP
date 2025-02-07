""""
04.02.2025
1-dars
Mavzi: Klass
"""
# def salom_ber():
#     print("Assalomu alaykum")
# print(type(salom_ber))
# class Talaba:
#     """ Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def tanishtir(self):
#         return f"Ismim {self.ism} {self.familiya}.{self.tyil} yilda tug'ilgan."
#     def get_name(self):
#         return self.ism
#     def get_lestname(self):
#         return self.familiya
#     def get_Fulname(self):
#         return f"{self.ism} {self.familiya}"
#     def get_age(self,yil):
#         return yil-self.tyil
#
# # KLASSDAN OBYEKT YARATAMIZ
# talaba1=Talaba("Shahzod","Ravshanov",2006)
# # print(talaba1.ism)
# # print(talaba1.familiya)
# # print(talaba1.tyil)
# talaba2=Talaba("Murat","Musayev",2003)
# talaba3=Talaba("Dilshod","Ochilov",2007)
# print(talaba1.tanishtir())
# print(talaba2.tanishtir())
# print(talaba3.tanishtir())
# talaba4=Talaba("Burhoniddin","Dehqonboyev",2006)
# talaba4.tanishtir()
# print(talaba4.tanishtir())
# print(talaba4.get_Fulname())
# print(talaba4.get_age(2025))
# class User:
#     def __init__(self,name,username,email):
#         self.name=name
#         self.username=username
#         self.email=email
#     def describe(self):
#        pass
#     def get_email(self):
#         pass
# Amaliyot
class Users:
    def __init__(self,name,username,email):
        self.name=name
        self.username=username
        self.email=email
    def get_name(self):
        return self.name
    def get_username(self):
        return self.username
    def get_email(self):
        return self.email
    def get_info(self):
        return f"Foydalanuvchi:{self.email},ismi:{self.name} {self.username},email:{self.email}@gmail.com"

user=Users("Shahzod","Ravshanov","shahzod1406")
print(user.get_name())
print(user.get_username())
print(user.get_email())
print(user.get_info())
