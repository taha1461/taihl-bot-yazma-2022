# 0'dan 100'e kadar olan tek ve çift sayıları yazdıralım
# örnek: 1 tek sayıdır
# örnek: 2 çift sayıdır
# = 0
#while sayi < 100:
#    if sayi % 2 == 0:
#        print(f"{sayi} çift sayıdır.")
#    else:
#        print(f"{sayi} tek sayıdır.")

#    sayi += 1

# excel okuma modülünü içeri aktaralım
import xlrd

# excel dosyasını açalım
ck = xlrd.open_workbook("veriler/WorldCupPlayers.xls")

# excel çalışma sayfasını alalım
cs = ck.sheet_by_index(0)

# toplam satırve sütün sayılarını alalım
satir_sayisi = cs.nrows
sutun_sayisi = cs.ncols
print(f"Satır sayısı: {satir_sayisi}")
print(f"Sütün sayısı: {sutun_sayisi}")

# ilk başlık satırını okuyalım
a1 = cs.cell(0, 0)
print(a1)

# tüm futbocuların isimlerini yazdıralım
satir = 1 # başlıkları es geçmek içi 1. indeksten başlıyoruz
while satir < satir_sayisi:
    futbolcu = cs.cell_value(satir, 6)
#   if futbolcu.startswith("R"):
 #    print(f"Futbolcu:{futbolcu}")

 # bir olayı yaşamış futbolcuları yazdıralım
    olay = cs.cell_value(satir, 8)
    if olay != "":
        print(f"Futbolcu: {futbolcu} - olay : {olay}")
    satir += 1