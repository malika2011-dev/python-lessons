"""Dictionary (Lug'at)"""
# Biz buni ko'proq biron bir narsaning ma'lumoti haqida ishlatamiz
# va biz uni yaratish uchun {} dan foydalanamiz va uni print() orqali chiqarishimiz uchun [] bundan foydalanamiz
# va lug'atda doim 1-tarafi ya'ni value tomonni str -- string ya'ni matn bo'lishi kerak key esa hohlagancha



car = {"model": "BMW", "rangi":"qora"}
print(car["model"])
print(car["rangi"])

eng_uzb = {"apple":"olma", "apricot":"o'rik", "banana":"banan"}
print(eng_uzb)
print(eng_uzb["apple"])

mevalar = {"olma":"5000", "o'rik":"12000", "uzum":"7000", "banan":"22000"}
print(f"Olma {mevalar["olma"]} so'm")
# Lug'atda istalgan ma'lomot turlarini saqlash mumkin

pupil = {"ism":"malika",
        "yosh":"13",
        "t_yil":"2011"
}

print(f"O'quvchining ismi: {pupil["ism"]},\
 yoshi {pupil["yosh"]}, tug'ilgan yili {pupil["t_yil"]}")

print(pupil)


pupil["fan"] = "Matemetika"
pupil["sinf"] = "7-green"
pupil["maktab"] = "Bobarahim Mashrab"
print(pupil["maktab"])     # qo'shish
pupil["ism"] ="Shohsanam"  # o'zgartirish
print(pupil["ism"] )
print(pupil)




# """Bo'sh lug'at"""

oquvchi = {}
oquvchi["ism"] = "Hadicha"
oquvchi["yosh"] = 12
oquvchi["sinf"] = 1
print(f"O'quvchining ismi {oquvchi["ism"].title()} , yoshi  \
       {oquvchi["yosh"]} da sinfi {oquvchi["sinf"]} - white")


# """qiymatni yangilash"""

oquvchi["yosh"] = 13
print(f"O'quvchining ismi {oquvchi["ism"].title()} , yoshi  \
       {oquvchi["yosh"]} da sinfi {oquvchi["sinf"]} - white")

# """del operatori"""
# # del operatoridan biz foydalanishda avval
# # del ni o'zini yozamiz va keyin o'zgaruvchi va kalit 
# # so'zni yozamiz.


pupil = {"ism":"malika", "yosh":"13", "t_yil":"2011"}
print(pupil)
del pupil["yosh"]
print(pupil)

# """Lug'atlarni bir nechta qatorda yozish"""
# #  bunda biz har yangi qatordan oldin ,(vergul)
# # dan foydalanamiz.


oila = {
    "ota" : "Akramboy",
    "ona" : "Madinaxon",
    "buvi" : "Tojixon",
    "aka" : "Akramjon",
    "uka" : "Zakariyo",
    "singil": "Hadicha"
}


# """.get() metodi"""


singil = oila["singil"]
print(f"Singilning ismi {oila["singil"]}")

ism = oila.get("singil", "Bunday ism mavjus emas")
print(ism)

ism2 = oila.get("opa", "Bunday ism mavjud emas")
print(ism2)


""".items()  metodi"""
# for operatori bilan foydalanishda yordam beradi
# ,(verguldan) oldingi yozilgani kalit, verguldan keyingi yozilgani qiymat
mevalar = {"Olma":"5000", "O'rik":"12000", "Uzum":"7000", "Banan":"22000"}
for meva, narx in mevalar.items():
    print(f" Meva : {meva}")
    print(f"Narx : {narx}")

taomlar = {
    "Malika" : "Pitsa",
    "Shohsanam" : "Lavash", 
    "Sevara" : "Hot - Lunch",
    "Fotima" : "Kartoshka",
    "Zilola" : "Monster"
}

for ism, taom in taomlar.items():
    print(f"{ism}ning yaxshi ko'rgan taomi {taom}")

""".keys() metodi"""
# Lug'atdagi kalitlarni chiqarib beradi
# biz keys() dan foydalanmasak ham u baribir konsulga 
# keys() ni chiqarib beradi

mevalar = {"olma":"5000",
    "o'rik":12000,
    "uzum":7000,
    "banan":22000
}

print("Mevalar nomi: ")
for mahsulot in mevalar.keys():
    print(mahsulot.title())

# 2-usul

    print("Mevalar nomi: ")
for mahsulot in mevalar:
    print(mahsulot.title())



bozorlik = ["olma", "anjir", "uzum", "banan"]
for mahsulot in mevalar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mevalar[mahsulot]} so'm")
    else:
        print(f"Kechirasiz bizda {mahsulot} yo'q! ") 


"""Lug'atni elementlarini tartib bilan chiqarish"""
print("Do'konimizdagi mahsulotlar: ")
print(sorted(mevalar.keys()))

#  yoki

print("Do'konimizdagi mahsulotlar: ")
for buyum in sorted(mevalar):
    print(buyum.title())

""".values() metodi"""
# bu lug'atdagi qiymatlarni chiqarib beradi

telefonlar = {
    "Shahlo" : "iphone 13",
    "Dilafruz": "iphone 14",
    "Iroda": "iphone 15",
    "Zuhra": "iphome 15 pro",
    "Rayxona": "redmi 14 pro ",

}

print("Foydalanuvchilar quidagi telefonlardan foydalanishadi: ")
for telefon in telefonlar.values():
    print(telefon.title())

"""set() funksiyasi"""
# elementlarni takrorlanmagan holatda chiqarib beradi
# sets --- .> ma'lumot turi -- > lug'atda bir xil kelgan kalitlar uchun
# set() --- > funksiya ---> elementlar takrorlanmasligi uchun
# Lug'atda elementlar takrorlanmaydi



telefonlar1 = {
    "Shahlo" : "iphone 16",
    "Dilafruz": "iphone 14",
    "Iroda": "iphone 15",
    "Zuhra": "iphome 13 ",
    "Mubina": "iphone 16",
    "Rayxona": "redmi 11 pro ",
    "Sarvinoz": "redmi 12 pro",
    "Saida": "redmi 12 pro"

}

print("Foydalanuvchilar quidagi telefonlardan foydalanishadi: ")
 
for tel in set(telefonlar1.values()):
    print(tel)

toys = {"ball", "car", "lamp", "ball"}
print(type(toys))
print(toys)