"""
05.02.2025
3-dars
Mavzu:Vorislik va polimorfizm
"""


# class Shaxs:
#     def __init__(self, ism, familya, pasport, tyil):
#         self.ism = ism
#         self.familya = familya
#         self.pasport = pasport
#         self.tyil = tyil
#
#     def get_info(self):
#         """ Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familya} ."
#         info += f" Pasport raqami: {self.pasport}, {self.tyil}_yilda tug'ilgan."
#         return info
#
#     def get_age(self, yil):
#         return yil - self.tyil
#
#
# inson = Shaxs("Shahzod", "Ravshanov", "AD29457", 2006)
# # print(f"{inson.get_info()} {inson.get_age(2025)} yoshda")
#
#
# class Fan:
#     def __init__(self, fan1):
#         self.fan1 = fan1
#         # self.fan2 = fan2
#         # self.fan3 = fan3
#         self.fanlar = []
#
#     def get_fan(self):
#         return f"{self.fan1}"
#
#
# fanla = Fan("matjcj")
#
#
# # print(fanla.get_fan())
# # VORIS KLASS YARATISH
# class Talaba(Shaxs):
#     """ Talaba  Klassi"""
#
#     def __init__(self, ism, familya, pasport, tyil, idraqam, manzil: str):
#         super().__init__(ism, familya, pasport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
#         self.fanlar = []
#
#     def get_id(self):
#         return self.idraqam
#
#     def get_bosqich(self):
#         return self.bosqich
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familya} ."
#         info += f"{self.get_bosqich()}-bosqich.ID raqami: {self.idraqam}"
#         return info
#
#     def bosh(self):
#         return self.fanlar
#
#     def fanga_yozil(self, fan):
#         if isinstance(fan, Fan):
#             return self.fanlar.append(fan)
#         else:
#             "bjdfljkdfljkdf"
#
#
#
# talaba = Talaba("Shahzod", "Ravshanov", "AD29457", 2006, "0001254", "a")
# # print(f"{talaba.get_info()}. ID raqami: {talaba.get_id()}")
# # print(f"{talaba.get_bosqich()}-bosqich talabasi")
# # #POLIMORFIZM — SUPER KLASS METODLARINI QAYTA YOZISH
# talaba.fanga_yozil(["abjls", "efwfg"])
# for i in talaba.bosh():
#     print(i)
# # OBYEKT ICHIDA OBYEKT
# class Manzil:
#     """ Manzilni saqlash uchun klass"""
#
#     def __init__(self, uy, kocha, tuman, viloyat):
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
#
#     def get_manzil(self):
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, {self.kocha} kochasi, {self.uy}-uy"
#         return manzil

#
# talaba_manzil = Manzil(12, 'Beshbek', "Shahrisabz", "Qashqadaryo")
# talaba=Talaba("Shahzod","Ravshanov","AD29457",2006,"000125445",talaba_manzil)
# print(talaba.manzil.get_manzil())
# print(talaba.manzil.tuman)

# Amaliyot
class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Fan:
    def __init__(self,fanla):
        self.fanla=fanla


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    def fanga_yozil(self, fan):
        """Fanga yozilish metodi"""
        if isinstance(fan, Fan):  # Fan klassi obyektini tekshiramiz
            self.fanlar.append(fan)  # Fan ro'yxatga qo'shiladi
            print(f"{self.ism} {self.familiya} {fan.fanla} faniga yozildi.")
        else:
            print("Xato: Fanga yozish uchun Fan klassi obyektini uzating!")

    def bosh(self):
        return [fan.fanla for fan in self.fanlar]
    def remove(self,fan):
        if fan in self.fanlar:
         self.fanlar.remove(fan)
         return f"{self.ism} {self.familiya} {fan.fanla} fangasi o'chirildi."
        else:
         return  "Siz bu fanga yozilmagansiz."

class Professor(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,ish_joy,unvier_tugat):
        super().__init__(ism,familiya,passport,tyil)
        self.ish_joy=ish_joy
        self.unvier_tugat=unvier_tugat
    def get_info(self):
        return (f"Professor, ismi: {self.ism} , familyasi:{self.familiya},Pasport id raqam:{self.passport},"
                f"tug'ilgan yili:{self.tyil},Ish joyini:{self.ish_joy},Unversitetni tugatgan yili:{self.unvier_tugat}")

class Foydalanuvchi(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,manzil,ish_joyi):
        super().__init__(ism,familiya,passport,tyil)
        self.manzil=manzil
        self.ish_joyi=ish_joyi
    def get_info(self):
        return (f"Foydalanuvchi, ismi: {self.ism} , familyasi:{self.familiya},Pasport id raqam:{self.passport}"
                f"tug'ilgan yil: {self.tyil},manzili: {self.manzil},ish joyini:{self.ish_joyi}")
class Admin(Foydalanuvchi):
    def __init__(self,ism,familliya,passport,tyil,manzil,ish_joyi,admin_kod,):
        super().__init__(ism,familliya,passport,tyil,manzil,ish_joyi)
        self.admin_kod=admin_kod
    def get_info(self):
        return (f"Admin, ismi: {self.ism} , familyasi:{self.familiya},Pasport id raqam:{self.passport}"
                f"tug'ilgan yil: {self.tyil},manzili: {self.manzil},ish joyini:{self.ish_joyi},admin kodi: {self.admin_kod}")
    def admin_kod_qaytar(self):
        return self.admin_kod
    def ban_user(self):
        print(" Foydalanuvchi bloklandi.")


fan1=Fan("Matematika")
fan2=Fan("Fizika")
fan3=Fan("Ona tili")
talaba=Talaba("Shahzod","Ravshanov","AD29457",2006,"000125445",fan1)
print(talaba)
talaba.fanga_yozil(fan1)
talaba.fanga_yozil(fan2)
talaba.fanga_yozil(fan3)
print(talaba.bosh())
# talaba.fanga_yozil("gsagsgd")
talaba.remove(fan1)
print(talaba.bosh())
admin=Admin("sjdhd","dhd","Adg5656",2523,"dbhfh",'shhdhdvd',6566)
print(admin.get_info())
print(admin.admin_kod_qaytar())
admin.ban_user()