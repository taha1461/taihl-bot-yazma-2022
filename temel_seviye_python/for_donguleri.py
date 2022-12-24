# öğrenci isimlerinden oluşan bir liste oluşturalım
ogrenciler = ["Eren", "Emirhan", "Taha"]

# her öğrencinin adını ekrana yazdıralım
# örnek: öğrencinin adı : Eren
for ogrenci in ogrenciler:
    print(f"Öğrencinin adı: {ogrenci}")

# İçinde ikili sayılardan oluşan tuple verilerinin olduğu bir liste oluşturalım
sayilar = [(1, 2), (3, 4), (5,6)]
for a,b in sayilar:
    print(f"1.sayı {a}, 2.sayı: {b}")

# okulumuzun adının yer aldığı bir değişkeni kelimelere
# bölüp her kelimeyi döngü içinde ekrana yazdıralım.
okul = "Sancaktepe Teknoloji Anadolu İmam Hatip Lisesi"
for a in okul.split():
    print(a)

# öğrencilerin yer aldığı bir dict veri tipi oluşturalım
ogrenciler = kisiler = {
    1:{
        "ad": "Eren",
        "soyad": "Özdal",
        "cinsiyet": "True",
        "dersler": ["Görsel Sanatlar","Matematik", "Hayat Bilgisi"]
    },
    45: {
        "ad": "Zeyneb",
        "soyad": "Özdal",
        "cinsiyet": "False",
        "dersler": ["Görsel Sanatlar", "Matematik", "Fen Bilimleri"]
    }
}

# öğrencilerin numaralarını ve adlarını yazdıralım
for no, ogrenci in ogrenciler.items():
    print(f"{no} numaralı öğrenci: {ogrenci['ad']}")
