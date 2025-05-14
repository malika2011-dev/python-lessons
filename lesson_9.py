"""For operatori va ro'yxat """


ismlar = ["ali", "jobir", "komil", "lola", "shodiya"]
for ism in ismlar:
    print("Salom", ism)

#2
mashinalar = ["kia", "toyota", "onix", "monza", "gentra"]
for mashina in mashinalar:
    print("Eng yaxshi mashina bu", mashina)

"""
for operatorida har bir elementga bir nom qo'yib uni o'zgaruvchi ichida yozamiz 
va agar biz printni ishlatyotganimizda print yonidan joy tashlamasak u bir marta takrorlanadi holos
va buni sonlar bilan ham ishlatsa bo'ladi va doim : oxirida qo'yish kerak
"""

sonlar=list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

    sonlar2=list(range(11))
    sonlarning_kvadrati=[]
    for son2 in sonlar2:
        sonlarning_kvadrati.append(son**2)
print(sonlar2)
print(sonlarning_kvadrati)

print(" 5 ta eng yaqin dugonangiz kim? ")
dugonalar=[]
for dugona in range(5):
    dugonalar.append(input(f"{dugona+1} - dugonagiz ismini kiriting: "))
print(dugonalar)
