# Şiir satırları
siir = [
    "Şimdi sen kalkıp gidiyorsun. Git",
    "Gözlerin durur mu onlar da gidiyorlar. Gitsinler.",
    "Oysa ben senin gözlerinsiz edemem bilirsin",
    "Oysa Allah bilir bugün iyi uyanmıştık",
    "Sevgideydi ilk açılışı gözlerimizin sırf onaydı",
    "Bir kuş konmuş parmaklarıma uzun uzun ötmüştü",
    "Bir sevişmek gelmiş bir daha gitmemişti",
    "Yoktu dünlerde evelsi günlerdeki yoksulluğumuz",
    "Sanki hiç olmamıştı",
    "Oysa kalbim işte şuracıkta çarpıyordu",
]

# Komutlar: (satır numarası, kelime numarası, harf numarası)
komutlar = [
    (2, 3, 9),   
    (2, 6, 7),   
    (2, 9, 3),   
    (3, 3, 9),   
    (3, 6, 3),
    (3, 9, 3),
    (4, 1, 3),
    (4, 3, 1),
    (4, 6, 7),
    (4, 7, 9),
    (4, 8, 3),
    (4, 9, 7),
    (5, 1, 9),
    (5, 8, 7),
    (6, 6, 3), 
    (7, 1, 7),
    (7, 5, 3),
    (7, 7, 3),
    (7, 8, 3),
    (8, 1, 9),
    (8, 3, 9),
    (8, 6, 1),
    (9, 6, 3),
    (9, 8, 1),
    (10, 1, 7),
    (10, 3, 7)
    
]

# Numara listesi (komutlarla eşleşecek numaralar)
numaralar = [139, 167, 193, 239, 263, 293, 313, 331, 367 ,379 ,383 ,397 ,419 ,487 ,563 ,617 ,653 ,673 ,683 ,719 ,739 ,761 ,863 ,881 ,917 ,937 ]

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
harf_sonuc_listesi = list(zip(numaralar, harf_sonuclari))

