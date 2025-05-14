"""These functions have been created before, but I created them for myself.
Bu funksiyalar oldin yaratilgan lekin men o'zim uchun boshqasini yaratdim

"""

"""Ildiz topib beruvchi"""
def ildiz(son, daraja = 2):
    """Istalgan ildizni topib beruvchi funksiya"""
    x = 1
    while True:
     if x**daraja != son:
        x+=1
     elif x**daraja == son :
        break
    return x
    
print(ildiz(8,3))
    

        


"""ekuk (eng kichik umumiy karalli)"""

def ekuk(a:int,b:int) -> int:
    x = 1 # a ni yoki b ni shu songa ko'pytirish uchun
    c = 1 # returnda qaytarish uchun (c ni qiymatini almashtiramiz)
    while True: 
        if a*x%b == 0: # a ni x soniga ko'paytirganimizda u b ga bo'linsa bu qiymatni c ga yuklaymiz
            c = a*x
            break
        else:
            x = x + 1 # aks xolda x ni qiymatini 1 taga ortiramiz   
    return c

print(ekuk(13,14))

"""ekub (eng katta umimiy bo'luvchi)"""


def ekub(a:int,b:int) -> int:

    return a*b/ekuk(a,b) # tarifga ko'ra a va b ning ko'paytamasi ekuk va ekubning ko'paytmasiga teng
    # shunining uchun biz a ni b gako'paytirib ularning ekukiga bo'lyapmiz

print(ekub(15,14))
print(ekub(6,8))
print(ekub(30,15))


