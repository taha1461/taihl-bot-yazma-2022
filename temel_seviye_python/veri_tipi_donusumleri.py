# Kullanıcıdan 2 sayı alıp toplama işlemi yapan program
# x = int(input("1.sayıyı girin"))
# y = int(input("2.sayıyı girin"))
print(x+y)

# farklı veri tiplerine bakalım : type()
x = 1 # int
y = 1.2 # float
ad = "taha" # string
sinav_basarili_mi = True # boolean
# print(type(x))
# print(type(y))
# print(type(ad))
# print(type(sinav_bsarili_mi))

# TİP DÖNÜŞTÜRME

# int'ten floa'a
print(float(x))

# float'tan int'e
print(int(y))

# bool'dan str'ye
print(sinav_basarili_mi)  # bool olarak true
print(str(sinav_basarili_mi))  # str olarak "True"

# bool'dan int'e
print(int(sinav_basarili_mi))

# int'ten str'ye
print(str(x)) # str olarak "1"

#str'den int'e
print(int(ad)) # metin int'e dönüşmez
sayi = "36"
print(int(sayi))
