"""Ro'yaxat bilan ishlash - Working with lists"""

""".sort() - ro'yhatni alifbo tartibida tartiblaydi"""

ism=["Malika","Zilola","Aziza","Fotima","Bonu","Shohsanam","Iroda"]
ism.sort() # Tog'ri tartiblalsh
print(ism)    

# .sort(reverse=True) --> Bu teskari tartilab beradi

ism.sort(reverse=True)
print(ism)

# sorted() bu matnni aynan shu vaqtda tartiblab beradi
sorted(ism)
print(ism)
# sorted() .sort() ga o'xshash


"""reverse()"""
# .reverse() --> Bu ro'yxatni aylantirib beradi
ism.reverse()
print(ism)


"""list"""
#  list() bu ro'yxat yaratib beradi range() esa sonlarni chiqarib beradi bu ikkisini doim birgalikda ishlatamiz
# agar biz range() ni ishlatganimiz qavs ichiga bitta sonni o'zini yozsak u noldan hisoblaydi
son=list(range(1,10))
print(son)
son1=list(range(11))
print(son1)

# = orqali biz o'zgaruvchi yaratib unga boshqa o'zgaruvchidan [] orqali nimani nusxalashni belgilaymiz yana = bu belgi o'zgartirib ham berdi
raqam=son[:] # : bu boshidan oxirgacha nusxalash yana bu belgi gacha ni xam anglatadi
print(raqam)
raqam[-1]=6
print(raqam)


"""len()"""
# len()--> bu ro'yxatda nechta element borligini aniqlab beradi
oila=["Onam","Otam","Buvim","Akam","Ukam","Singlim","O'zim"]
print(f"Bizning oilada {len(oila)} ta kishi yashaydi bular {oila}")

# mix() , min(), sum() funksiyalari 

print(max(son)) # eng katta soni topib beradi
print(min(son)) # eng kichik soni topib beradi
print(sum(son)) # ro'yhatdagi sonlar yig'indisi


"""
tople --> o'zgarmas ro'yxat
agar biz ro'yxatni ()  shu qavs bilan ochib qo'ysak bu o'zgarmas ro'yxat deyildi "tuple"
biz touple ya'ni o'zgarmas ro'yxat bilan  hech qanday metodni ishlata olmaymiz
lekin agar biz biror metodni ishlatniqchi bo'lsak toupleni list ga almashtiramiz 
biz agar yana buni touple qilish uchun yana tuple qilamiz

"""

dasturlash=("phyton","java","java script")
# endi bunga hech qanday o'zgartirish kirita olmaymiz 
# o'zgartirish kiritish uchun list() dan foydalanamiz
dasturlash=list(dasturlash)
# endi buni o'zgartira olamiz
# yana bu ni o'z holiga qaytarrish uchun tupleni ishlatamiz
dasturlash=tuple(dasturlash)
print(f"dasturlashning turlari {dasturlash}")



"""If you do'nt understand uzbek, you translate word with translater"""