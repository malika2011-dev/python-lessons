"""while va ro'yxatlar -- > 18 - dars"""

print("Yaqin do'stlaringizni ro'yxatini tuzamiz")
ismlar = []
n = 1
while True:
    savol = input(f"{n} - do'stingizni ismini kiriting: ")
    ismlar.append(savol)
    n = n + 1

    takrorlash = input("Yana do'stlaringizni ismini kiritimoqchisimisiz (ha\yo'q): ").lower()
    if takrorlash != "ha":
        break
print("Sizning do'stlaringiz: ", end=", ")
for ism in ismlar:
    print(ism.title(), end=" , ")



"""while va lug'at"""

print("Do'stlaringizni yoshini saqlaymiz! ")
dostlar = {}
ishora = True

while ishora:
    ism = input("Do'stingizni ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriitng: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot qo'shishni xoxlaysizmi (ha/yo'q): ")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")



"""while va ro'yxatdagini o'chirish"""

# agarda biz ro'yxatdagi elementni while orqali o'chirsak u element nech marta 
# takrorlangan (ro'yxat ichida 2 ta 3 yoki 4ta bo'lsa ham) bo'lsada o'chadi
# ctrl + c -- terminalni harqanday holatda to'xtadadi



cars2 = ["malibu", "nexia", "onix", "nexia" , "trecker", "nexia", "tayota", "byd"]

while "nexia" in cars2:
    cars2.remove("nexia")
print(cars2)

"""while va ro'yxat bilan ish"""

talabalar = ["hasan", "husan", "olim", "ali"]
baholangan_t = {}
while talabalar: # ro'yxat bo'shaguncha takrorlanadi
    talaba = talabalar.pop() # ro'yxatdan biror bir talabani sug'urib oladi
    baho = input(f"{talaba.title()} ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_t[talaba] = baho

print("Talabalar ro'yxati: ")
for talaba , baho in baholangan_t.items():
    print(f"{talaba.title()} : {baho}")
    