branslar = ("Yazilim", "Tasarim","Pazarlama")

tum_ogrenciler = []

ogrenci1_ad = "Ahmet".strip()
ogrenci1_brans = ["Tasarim"]

ogrenci2_ad = "Sinan".strip()
ogrenci2_brans = ["Yazilim"]

ogrenci3_ad = "Baran".strip()
ogrenci3_brans = ["Pazarlama"]

tum_ogrenciler.append([ogrenci1_ad, ogrenci1_brans])
tum_ogrenciler.append([ogrenci2_ad, ogrenci2_brans])
tum_ogrenciler.append([ogrenci3_ad, ogrenci3_brans])

print("Başlangiç Öğrenci Listesi:",tum_ogrenciler)

tum_ogrenciler.insert(0,["Başkan",["Yazilim","Tasarim","Pazarlama"]])
print (f"Toplam Kayıtlı Öğrenci Sayısı: {len(tum_ogrenciler)}")

tum_ogrenciler.remove(["Ahmet",["Tasarim"]])
print(tum_ogrenciler)
son_cikan = tum_ogrenciler.pop()
print("Sistemden en son çıkan öğrenci:",son_cikan[0])

tum_ogrenciler.append(["Burak Tan",["Tasarim"]])
print(tum_ogrenciler)

print(sorted(tum_ogrenciler))
print(tum_ogrenciler)

tum_ogrenciler.sort()
print(tum_ogrenciler)

