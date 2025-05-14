"""Funksiya -- > 19 dars"""

# funksiya orqali biz o'zimiz funksiya yasay olamiz
# biz uchun argument  foydalanuvchi uchun argument

# docstring -->._doc_ -->  funksiya haqida ma'lumot beruvchi

"1-usul"
def salom_ber():
    """Salom beruvchi funksiya"""
    ism = input("Ismingizni kiriting: ")
    print(f"{ism.title()} assalomu aleykum!")

salom_ber()

"2-usul"

def salom_ber2(ism2):
    "Foydalanuvchiga salom beruvchi funksiya"
    print(f"Assalomu aleykum hurmatli {ism2.title()}")

salom_ber2("malika")
salom_ber2("shohsanam")

"""Paremetrlardan foydalanish"""

def toliq_ism(ism, familya):
    "Foydalanuvchuning to'lqi ismini jamlan chiqaruvchi funksiya"

    print(f"Ismi: {ism.title()}\n"
          f"Familyasi : {familya.title()}")
    
toliq_ism("malika", "abdulahadova")

"""Parametrlar"""

def yosh_hisobla(ism, t_yil):
    """Yoshni hisoblovchi dastur"""
    print(f"{ism.title()} {2025 - t_yil} yoshda ")

# hatolikni oldini olish uchun funksiyadan foydalaniyotganda o'zgaruvchi nomi bilan qiymat kiritish kerak
yosh_hisobla("malika", 2011)
yosh_hisobla(t_yil = 2011, ism = "malika")

"""paremeterda standart xolatlari"""
def aniq_yoshni_top(t_yil, hozir = 2025):
    "Foydalanuvchining hozirda nechayosh ekanligini hisoblaydi"
    print(f"Siz {hozir - t_yil} yoshdasiz")

aniq_yoshni_top(2011, 2025)
aniq_yoshni_top(2011)
    



"""Funksiya qiymat qaytarish ---> 20 -dars"""

# return -- > qaytarish, yasash
# local varible -- > ichki o'zgaruvchi

def toliq_ism_yasa(ism, familya):
    """To'liq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism.title()} {familya.title()}"
    return toliq_ism

talaba = toliq_ism_yasa("malika", "abdulahadova")
print(talaba)

print(f"{talaba} nugun keldi")

"""Ixtiyoriy agrumnet"""
# Hohlasa kiritiadi hohlamasa kiritmaydi

def toliq_ism_yasa(ism, familya, otasining_ismi = ""):
    "To'liq ism qaytaruvchi funksiya"
    if otasining_ismi: # agar otasining ism bor bo'lsa
        toliq_ism = f"{ism.title()} {otasining_ismi.title()} {familya.title()}"
    else:
        toliq_ism = f"{ism.title()} {familya.title()}"
    return toliq_ism.title()
    
talaba1 = toliq_ism_yasa("shohsanam", "mamadjanova")
talaba2 = toliq_ism_yasa("zilola", "sobirjanova", "azamovna")

print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


"""def va lug'at"""

def avto_info(kompaniya, model, rangi, karobka, yili, narhi = None):
    avto = {
        "kompaniya":kompaniya,
        "model":model,
        "rangi":rangi,
        "karobka":karobka,
        "yili":yili,
        "narhi":narhi,
    }
    return avto

avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000  )

avtolar = [avto1, avto2]
for avto in avtolar:
    print("Onayn bozordagi mavjud  avtomashinalar: ")
    if avto["narhi"]:
        narh = avto["narhi"]
    else:
        narh = "Noma'lum"
    print(f"{avto["rangi"]} {avto["model"]} narhi {narh} $ ")





"""oraliq -- > range"""


# def oraliq(min, max, qadam=1):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += qadam
        
#     return sonlar
    
# print(oraliq(1,10,2))

# print(oraliq(3, 15, 2))

 

"""katta -- > max"""
# def katta(sonlar):
#     "Eng kattasini topib beruvchi dastur"
#     x = sonlar[0]
#     for son in sonlar:
#         if son > x:
#             x = son
#     return x



# print(katta(oraliq(1, 10, 2)))


"""kichik -- > min"""      
# def kichik(sonlar):
#     "Eng kichigini topib beruvchi dastur"
#     x = sonlar[0]
#     for son in sonlar:
#         if son < x:
#             x = son
#     return x
 

# print(kichik(oraliq(1, 10 , 2)))


"""Avto info davomi while bilan"""
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting: ")

#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("MOdeli: ")
#     rang = input("Rangi: ")
#     karobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input('Narxi: ')

#     avtolar.append(avto_info(kompaniya, model, rang, karobka, yili, narhi))

#     javob = input("Yana kiritishni xoxlaysizmi (ha\yo'q): ")
#     if javob == "yo'q":
#      for avto in avtolar:
#         print("Onayn bozordagi mavjud  avtomashinalar: ")
#         if avto["narhi"]:
#             narh = avto["narhi"]
#         else:
#          narh = "Noma'lum"
#     print(f"{avto["rangi"].title()} {avto["model"].title()} narhi {narh} $ ")
#     break


"""Funksiya ro'yxatga uzatish ---> 21 -dars"""

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()} ning bahosini kriting: ")
#         baholar[ism] = int(baho)

#     return baholar

# talabalar = ["malika", "zilola", "shohsanam", "fotima"]
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)



"""Moslashuvchan, o'zgaruvchan  funksiyalar  --- > 22 - dars"""

"""*args va *kwargs"""

# # *args ---> hohlagancha ma'lumot qo'shish mumkin
# # **kwargs --- > Kalit so'z bilan hohslagancha ma'lumot qo'shish mumkin

# def summa(sonlar, *sonlar2):
#     """Kirtilgan sonlarning yig'indisini topuvchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     for son2 in sonlar2:
#         yigindi += son2
#     return yigindi

# sonlar = list(range(1,10))
# print(summa(sonlar, 4,5,6,7))

# def pupil(ism, familya , **malumotlar):
#     """O'quvchi haqidagi malumotni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar["ism"] = ism
#     malumotlar["familya"] = familya

#     return malumotlar

# student = pupil("Malika", "Abdulahadova", yosh = 14, sinf = 7)
# print(student)