from Inkapsulyatsiya import Avto,Talaba,Shaxs

avto1=Avto("GM","Malibu",'Qora',2020,40000,)
avto2=Avto("GM","Gentra",'Qora',2020,40000,5000)
print(avto1.get_id())
print(avto1.get_km())
avto1.add_km(1000)
print(avto1.get_km())
print(avto1.get_num_avto())


# Amaliyot

talaba1=Talaba("Shahzod","Ravshanov",2006)
print(talaba1.talaba_id())
print(talaba1.get_age(2025))
shaxs1=Shaxs("Shahzod","Ravshanov","AD29457",2006)
print(shaxs1.get_pasport())
print(shaxs1.get_info())
print(shaxs1.get_shaxs_soni())
print(talaba1.get_talabalar_soni())