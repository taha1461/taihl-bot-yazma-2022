# kullanıcıdan isim, soyad  ve yaş bilgilerini alalım
isim = input("isminiz: ")
soyad = input("soyadınız: ")
yas = input("yaşınız: ")

# kullanıcı bilgilerini yazdıralım
# -> Adınız: taha, yaşınız:36
print("Adınız: " + isim + " " + soyad + " ,yasınız: " + yas)
print("Adınız: {} {}, Yaşınız: {}".format(isim, soyad, yas))
print("Adınız: {2} {0}, Yaşınız: {1}".format(soyad, yas, isim))
print("Adınız: {x} {y}, Yaşınız: {z}".format(y=soyad, z=yas, x=isim))
print(f"Adınız: {isim} {soyad}, Yaşınız: {yas}")