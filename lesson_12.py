"""NESTING """

# bir narsa ichida 5rtfdccccc 
# boshqa narsani saqlash
# for operatori bilan foydalannish

"""Lug'atlar ro'yxati"""

car0 = {
    'model':'lacetti',
    'rang':'oq',
    'yil':2018,
    'narh':13000,
    'km':50000,
    'korobka':'avtomat'
 }

car1 = {
    'model':'nexia 3',
    'rang':'qora',
    'yil':2015,
    'narh':9000,
    'km':89000,
    'korobka':'mexanika'
 }

car2 = {
    'model':'gentra',
    'rang':'qizil',
    'yil':2019,
    'narh':15000,
    'km':20000,
    'korobka':'mexanika'
}
# 1-navbatda lug'atlarni ro'yxat qilin olamiz
# keyin esa for stikilidan foydalanamiz
cars = [car0, car1, car2]

for car in cars:
    print(f"{car["model"].title()}, "
      f"{car["rang"].title()} rang, "
      f"{car["yil"]} - yil , {car["narh"]} $")

# ro'yxatda elementni chiqarish uchun nima ish qilsak
# nestingda ham shunday

# title() va boshqalarni mana bunday ishlatamiz  
print(cars[1]["rang"])
print(f"{cars[2]["rang"].title()} " 
      f"{cars[2]["model"]}")


# lug'atdagi ro'yxatni for stikili orqali qilish
malibus = []
for n in range(10):
    new_car = {
        "model":"malibu",
        "rang":None, # noaniq
        "yil":2020,
        "narh":None,
        "km":0,
        "karobka":"avto"
    }
    malibus.append(new_car)


# endi for stikili orqali qiymatni o'zgartiramiz
for malibu in malibus[:3]:
    malibu["rang"] = "qizil"
for malibu2 in malibus[3:6]:
    malibu2["rang"] = "qora"
for malibu3 in malibus[6:]:
    malibu3["rang"] = "oq"

# endi hamma sini birgalikda kiritamiz
for malibu0 in malibus:
    print(malibu0)


# endi esa if va else ni ham ishlatamiz
for malibu in malibus:
    if malibu["karobka"] == "avto":
        malibu["narx"] = "4000$"
    else:
        malibu["narx"] = "3500$"

print(malibu)


"""Lug'at ichida ro'yxat"""
dasturchilar = {
    "ali":["python","C++"],
    "vali":["html","css","js"],
    "hasan":["php","sql"],
    "husan":["python","php"],
    "maryam":{"c++","c#"}
}
# demak biz value va key larni ham for stikili orqali ajrata olamiz
for ism , tillar in dasturchilar.items():
    print(f"\n{ism.title()} quidagi dasturlash tillarini biladi: ", end=" ")
    for til in tillar:
        print(f"{til.upper()} ",end = '')


"""info"""

hamkasblar = {
    "ali" : {"familya":"valiyev",
             "tyil":1995,
             "malumot":"oliy",
             "tillar":["c++", "python"],
             },
    "Vali" : {"familya":"aliyev",
             "tyil":1994,
             "malumot":"o'rta maxsus",
             "tillar":["html", "css", "js"],
             },
    "hasan" : {"familya":"husanov",
             "tyil":1993,
             "malumot":"maxsus",
             "tillar":["php", "python"],
             },
    
}
# info bu lug'at ichidagi lug'atni ajratib beradi va ro'yxatni ham
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info["familya"].title()}",
           f"{info["tyil"]} - yilda tug'ilgan",
             f" Ma'lumoti : {info["malumot"]}, \n"
             "Quidagi dasturlash tillarini biladi: ")
    for til in info["tillar"]:
        print(til.upper())
