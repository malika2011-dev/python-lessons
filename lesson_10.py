"""If-else-elif"""

""" if else """
"""comment"""
# if va elsa dan oldin hech qachon joy tashlamang va oxirida : qo'ying
# if agar --> shart bajarilsa
# else aks holda --> shart bajarilmasa
# ==  --> ga tengmi  degan ma'noda 
# != --> teng emasmi dgan ma'noda
# >=  --> katta yoki teng degan ma'noda
# agar : shu belgi qolib ketsa ham xato
# : --> bu belgidan keyin biz shartni tugatdik keyin print()  qilamiz
# doim biz for ni ishlatib ro'yxatni qiymatini bilmoqchi bo'lsak doim oxirgi element chiqadi
# True bu if , False else , desa ham bo'ladi

cars=["bmw","monza","cobalt","mers"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


ism=input("Ismingizni kiriting: ")
if ism.lower() !="malika":
    print(f"Kechirasiz {ism.title()} bizga malika kerak edi. ")
else:
    print("Salom, Malika")  

javob=float(input("12*6 nechiga teng"))
if javob != 72:
    print("Notog'ri javob")
else:
    print("Tog'ri")

yosh=int(input("Yoshingiz nechida? "))
if yosh>=16:
    print("Siz maktabni bitirdingiz!")
else:
    print(f"hali maktabni tugatishingizga {16-yosh} yil bor")

login=input("Yangi login kiriting: ")
if len(login)<=5:
    print("Loginingiz 5 ta harfda o'tishi shart!")
else:
    print(f"Sizning loginigiz quidagicha , {login}")

yil=int(input("Yoshingiz nechida? "))
if 2024-yosh<15:
    print(f"Siz {yil} yoshda ekansiz")
    print("Siz olimpiadaga qatnasha ololmaysiz")
else:
    print("Xush kelibsiz")


"""if else va elif"""
# elif --> agarda bu if va elsening yig'indisi desa ham bo'ladi
#  biz yana elif ni bir martadan ko'ra ko'proq ishlata olamiz
#  yana bizda yordamchi operatorlar bor bular or va and
# or--> yoki degan ma'noni anglatadi
# and--> va degan ma'noni anglatadi
# or ni 1ta dan ortiq ishlatamiz    
# and ni 1ta dan ortiq savollar ishlatamiz
# True --> to'g'ri bo'ldi yana bu 1 ham deyiladi
# false --> Notog'ri bo'lamydi yana bu 0 ham deyiladi

yosh=int(input("Yoshingizni kiriting : "))
if yosh<4 :
    print("Sizga kirish tekin ")
elif yosh<=12:
    print("Sizga kirish 5000 so'm")
else:
    print("Sizga kirish 10000 so'm")
 
"""and va or operatorlari"""

kun=input("Bugun qaysi kun? ")
if kun.lower() =="shanba" or kun.lower()== "yaksanba":
    print("Bugun dam olish kuni")
else:
    print("Bugun dam olish kuni emas! ")

oy=input("Hozir qaysi oy? ")
sana=input("Sana nechi? ")
if oy.lower() =="yanvar" or oy.lower()=="dekabr" or oy.lower()=="fevral" and sana<=10 or sana<=20 :
    print("Hozir qish va hali qish tugamaydi ")
else:
    print("Hozir qish emas ")

narx=20000
non=True
choy=False
if non and choy:
    print(f"Jami {narx+10000} so'm")
elif choy or non:
    print(f"Jami {narx+5000} so'm ")
else:
    print(f"Jami {narx} so'm")

    """in va not in  operatori"""
# in --> bor
# not in --> yo'q 

menu=["manti", "osh", "qozonkabob"]
ovqat=input("Qanday ovqat kiritasiz: ")
if ovqat in menu:
    print("Ovqat qabul qilindi")
else:
    print("Kechirasiz bizda  bunday taom yo'q")

number=int(input("Son kiriting: "))
if number<0:
    print("manfiy son")
elif number == 0:
    print( " Siz kiritgan son 'Manfiy' ham emas, 'Musbat' ham emas")
    print(" Siz kiritgan son 'Toq  son ham emas, 'Juft' son hama emas ")
else:
    print(" Siz kiritgan son 'Musbat son' ")
    if number%2:
        print(" Siz kiritgan son 'Toq' son")
    else:
        print(" Siz kiritgan son 'Juft' son ")

menu=["Besh barmoq","Somsa","Chuchvara","Osh","Qozonkabob","Manti"]
buyurtmalar=["Osh","Xonim","Sho'rva","Shashlik","Qozonkabob","Manti"]
for taom in buyurtmalar:
    if taom.title() in menu :
        print(f"Bizda {taom.title()} taomi menuda bor")
    else:
        print(f"Kechirasiz afsuski bizda {taom.title()} taomi menuda yo'q")

""" Demak bundan bilsa bo'ladiki if ni 2 yoki undan ortiq ishlatsa
 bo'ladi va yana u for operatori bilan ham birga kelishi mumkin

"""
menu=["Besh barmoq","Somsa","Chuchvara","Osh","Qozonkabob","Manti"]
buyurtmalar=[]
buyurtmalar.append(input("1-taomni kiriting : "))
buyurtmalar.append(input("2-taomni kiriting : "))
buyurtmalar.append(input("3-taomni kiriting : "))
buyurtmalar.append(input("4-taomni kiriting : "))
buyurtmalar.append(input("5-taomni kiriting : "))
print(f"Demak siz {buyurtmalar} taomlarini xoxlaysiz")   
for taom in buyurtmalar:
    if taom in menu:
        print(f"Bizda {taom} taomi menuda bor")
        print("Va sizning buyutmangiz qabul qilindi")
    else:
        print(f"Kechirasiz bizda afsuski {taom} taomi menuda yo'q")
