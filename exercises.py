"""1-mashq"""
son=int(input("Juft son kiriting: "))

if son%2 == 0:
    print("Rahmat")
else:
    print("Iltimos juft son kiriting")

"""2-mashq"""
yosh=(input("Yoshingizni kiriting: "))
yosh=int(yosh)
if yosh<4  or yosh>60  :
    print("Sizga kirish bepul")
if yosh<18 or yosh<60 :
    print("Sizga kirish 10000 so'm")  
if yosh>18 :
    print("Sizga kirish 20000 so'm")

"""3-mashq"""
son1=input("1-sonni kiriting: ")
son2=input("2-sonni kiriting: ")
son1=float(son1)
son2=float(son2)
if son1>son2:
    print(f"{son1} > {son2}")
if son2>son1:
    print(f"{son2}>{son1}")

# yoki 
    
sonlar=[]
(sonlar.append(son1))
sonlar.append(son2)
son1 = int(son1)
son2 = int(son2)
print(f"{max(sonlar)} soni katta, {min(sonlar)} soni esa kichik" )
    
""" 4-mashq """
mavjud = []
mavjud_emas = []
print("Assalomu aleykum do'konimizga xush kelibsiz! ")
mevalar = ["anor", "uzum", "gilos", "olcha", "nok"]
for son in range(1,6):
    meva = input(f"Olmoqchi bo'lgan {son}-mevangizni kiriting: ")
if meva in mevalar:
        mavjud.append(meva)
        print(f"Bizda bor : {mavjud}")
if meva not in mevalar:
        mavjud_emas.append(meva)
        print(f"Bizda yo'q {mavjud_emas}")
        








# """4-mashq"""

# mahsulotlar2 = ["anor", "uzum", "olma", "gilos", "behi", "anjir"]
# savat2 = []
# for n2  in range(0,5) :

#     savat2.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# mavjud_emas2=[]

# for mahsulot2 in savat2:
   
#     if mahsulot2 not in mahsulotlar2:
#          mavjud_emas2.append(mahsulot2)

# print(f"Bizda {mavjud_emas2}  yo'q ")


# """5-mashq"""

# foydalanuvchilar = ["aziza", "alisher", "anora", "asila", "aygul", "ali", "anvar", "asad"]

# login = (input("Kiritishingiz kerak bo'lgan loginni kiriting: "))
# if login in foydalanuvchilar:
#     print("Kechirasiz bu login bant! ")
# else :
#     print(f"Xush kelibsiz {login.title()}")




""""5-mashq"""

# print("Assalomu aleykum xush kelibsiz!")
# ism = input("Ismingizni kiriting: ")
# familya = input("Familyangizni kiriting: ")
# yosh = input("Yoshingizni kiriting: ")
# millat = input("Millatingizni kiriting: ")
# shahar = input("Hozirda yashayotgan shahringizni kiriting: ")

# print("Pasportingiz tayyor ko'rishingiz mumkin: ")

# print(f"Ism :    {ism} ")
# print(f"Familya :{familya} ")
# print(f"Yosh :   {yosh} ")
# print(f"Milllat: {millat} ")
# print(f"Shahar : {shahar} ")



"""14 - dars"""
# """ 1-mashq"""
# onam = {"ism" : "Madina", "t_yil" : 1991, "shahar" : "Namangan"}
# print(f"Onamning ism {onam["ism"]}, yoshlari {onam["t_yil"]}da {onam["shahar"]} da tug'ilganlar.")

# """2-mashq"""
# taomlar = {
#     "Malika" : "Pitsa",
#     "Shohsanam" : "Lavash", 
#     "Sevara" : "Hot - Lunch",
#     "Fotima" : "Kartoshka",
#     "Zilola" : "Monster"
# }

# for ism, taom in taomlar.items():
#     print(f"{ism} ning yaxshi ko'rgan taomi {taom}")


# """3-mashq"""
# phyton_izohli_lugat = {
#     "float": "O'nlik son",
#     "integer": "Butun son",
#     "string" : "matn",
#     "if": "agar"
# }

# kalit = input("Kalit so'z kiriting: ").lower()
# tarjima = phyton_izohli_lugat.get(kalit)
# if tarjima == None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")


"""15-dars"""
# """1-mahshq"""
# phyton_izohli_lugat = {
#     "float": "O'nlik son",
#     "integer": "Butun son",
#     "string" : "matn",
#     "if": "agar"
# }

# for lugat, qiymat in phyton_izohli_lugat.items():
#     print(f"{lugat} - {qiymat}")

# # """2-mashq"""
# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# print("Dunyo davlatlari")
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.upper())

# print("Dunyo davlatlari poytaxti: ")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

# shahar = input("Qaysi davlatning poytaxtini bilishni istaysiz: ").lower()
# poytaht = davlatlar.get(shahar)
# if poytaht == None:
#     print(f"Kechirasiz bizda {shahar} haqida ma'lumot yo'q")
# else:
#     print(f"{shahar.title()}ning poytaxti {poytaht.title()} shahri")


# """3-mashq"""
# menu = {
#     'osh':20000,
#     "lag'mon":22000,
#     'non':4000,
#     'choy':5000,
#     'shashlik':12000,
#     'somsa':6000,
#     'tabaka':15000
# }

# print("3 taom buyurtma bering: ")
# buyurtmalar =[]
# for x in range(3):
#     buyurtmalar.append(input(f"{x+1} - taom : ").lower())
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} -  {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz bizda {buyurtma.title()} yo'q")










































    





    
































