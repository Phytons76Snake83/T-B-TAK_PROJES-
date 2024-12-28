sayi = int(input("Lütfen sayıyı giriniz: "))

durdur = False

ikilik_taban = ""
while not durdur:
    bolum = sayi // 2
    kalan = sayi % 2
    ikilik_taban = str(kalan) + ikilik_taban 
    sayi = bolum
    if sayi == 0:
        durdur = True

print("İkilik tabanda gösterimi:", ikilik_taban)




