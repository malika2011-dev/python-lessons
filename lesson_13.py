"""While -- > 17 - dars"""
son = 1 # songa 1 qiymatini beramiz
while son <= 5 : #toki son 5 dan kichik yoki teng ekan ..
    print(son, end=' ') # sonni konsulga chiqaramiz
    son += 1 # songa 1 ni qo'shamiz
# a = a + b --> a += b 
print("Dastur tugadi")

"""while and input()"""
print("Kiritilgan sonning kvadratini topib beruvchi dastur")
savol = "Istalgan sonni kiriting "
savol += "( Daturni to'xtashish uchun 'exit' deb yozing ): "
qiymat = " "
while qiymat != "exit":
    qiymat = (input(savol))
    if qiymat != "exit":
        print(float(qiymat)**2)
print("Dastur tugadi")

"""ishora"""
print("Kiritilgan sonning kvadratini topib beruvchi dastur")
savol = "Istalgan sonni kiriting "
savol += "( Daturni to'xtashish uchun 'exit' deb yozing ): "
ishora = True
while ishora:
    qiymat = (input(savol))
    if qiymat == "exit":
        ishora = False
    else:
        print(float(qiymat)**2)
print("Dastur tugadi")

"""break while"""


print("Kiritilgan sonning kvadratini topib beruvchi dastur")

while True:  # abadiy tsikl
    savol = input("Istalgan sonni kiriting ( Daturni to'xtashish uchun 'exit' deb yozing ): ")
    if savol != "exit":
        print(int(savol)**2)
    else:
        break  # tsiklni to'xtatish
print("Dastur tugadi")


"""break"""
sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5:
        break
    print(f"{son} nig kvadrati {son**2} ga teng")

"""continue"""
# breakning aksi

sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5:
        continue
    print(f"{son} nig kvadrati {son**2} ga teng")

"""continue while"""
son = 0
while son < 10:
    son += 1
    if son%2!=0:
        continue
    else:
        print(f"{son} juf son")

