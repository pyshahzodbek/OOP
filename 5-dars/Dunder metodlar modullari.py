from Dunder_metodlari import Avto,AvtoSalon,Talaba,Shaxs,Fan
avto1=Avto("GM",'MAlibu',"qora","2025","40000")
avto2=Avto("GM",'Gentra',"qora","2025","25000")
print(avto1) # obyekt haqida ma'lumot
# x.__lt__(self,y)
# x<y
# x.__le__(self,y)
# x<=y
# x.__gt__(self,y)
# x>y
# x.__ge__(self,y)
# x>=y
# x.__eq__(self,y)
# x==y
# x.__ne__(self,y)
# x!=y
print(avto1==avto2)
print(avto1<=avto2)
print(avto1>avto2)
salon1=AvtoSalon("MaxAvto")
print(salon1)
for avto in [avto1,avto2]:
    salon1.add_avto(avto)

print(len(salon1))
print(salon1[1])
avto3=Avto("Mazda",'6',"qora","2025","40000")
salon1[0]=avto3
print(salon1[0])
print(len(salon1))

salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("Avto Lider")
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)

salon1.add_avto(avto1,avto2,avto3)
salon2.add_avto(avto4,avto5,avto6)
salon3=salon1+salon2
print(salon3)
print(salon3[:])

avto7 = Avto("BMW", 'X7','Qora',2015,75000)
salon1 + avto7
print(salon1[:])
"""
            Qo'shish
            __add__
            Ayiris
            __sub__
            Ko'paytirish
            __mul__
            Daraja
            __pow__
            Bo'lish
            __div__
"""
avto_new=Avto("BMW",'X7',"qora","2025","40000")
salon1(avto_new)
salon1()
""" Amaliyot"""
talaba1=Talaba("Shahzod",'Ravshanov',2006,1)
talaba2=Talaba("Otabek",'Islomov',2006,1)
talaba3=Talaba("Otabek",'Karimov',2006,2)
print(talaba1==talaba2)
fan1=Fan("Matematika")
fan1.add_student(talaba1)
fan1.add_student(talaba2)
# fan1[1]=talaba3
print(fan1)
fan1=fan1+talaba3
# print(fan1)
fan1=fan1-talaba1
print(fan1)
fan1=Fan("Fizika")
fan1(talaba2)