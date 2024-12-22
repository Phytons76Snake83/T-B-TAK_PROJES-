# Şiir satırları
siir = [
    "ŞimdisenkalkıpgidiyorsunGit",
    "GözlerindururmuonlardagidiyorlarGitsinler.",
    "Oysabenseningözlerinsizedemembilirsin",
    "OysaAllahbilirbugüniyiuyanmıştık",
    "Sevgideydiilkaçılışıgözlerimizinsırfonaydı",
    "Birkuşkonmuşparmaklarımauzunuzunötmüştü",
    "Birsevişmekgelmişbirdahagitmemişti",
    "Yoktudünlerdeevelsigünlerdekiyoksulluğumuz",
    "Sankihiçolmamıştı",
    "Oysakalbimişteşuracıktaçarpıyordu",
]

# Komutlar: (satır numarası, kelime numarası, harf numarası)
komutlar = [
    (1, 1, 7),   
    (1, 1, 13),   
    (1, 1, 19),   
    (1, 1, 23),   
    (1, 1, 31),
    (2, 1, 3),
    (2, 1, 9)
   
    
]

# Numara listesi (komutlarla eşleşecek numaralar)
numaralar = [7, 13, 19, 23, 31, 103, 109]
# Harf sonuçlarını tutacak liste
harf_sonuclari = []

# Komutları işle
for satir_num, kelime_num, harf_sayisi in komutlar:
    try:
        # İlgili satırdaki kelimeleri böl ve hedef harfi al
        kelimeler = siir[satir_num - 1].split()
        hedef_kelime = kelimeler[kelime_num - 1]
        hedef_harf = hedef_kelime[harf_sayisi - 1]  # Harf sırasını al
        harf_sonuclari.append(hedef_harf)
    except (IndexError, ValueError):
        # Harf bulunamazsa boş bırak
        harf_sonuclari.append("")

# Numara ve harfleri eşleştirip sonuçları listeliyoruz
harf_sonuclari = list(zip(numaralar, harf_sonuclari))

