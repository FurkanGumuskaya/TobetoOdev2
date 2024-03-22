
#Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.

def asal_carpanlari_bul(sayi):
    asal_carpanlar = []
    carpan = 2  

    while carpan * carpan <= sayi:
        if sayi % carpan == 0:
            asal_carpanlar.append(carpan)
            sayi //= carpan  
        else:
            carpan += 1

    if sayi > 1:
        asal_carpanlar.append(sayi)

    return asal_carpanlar

sayi = int(input("Bir sayı girin: "))
asal_carpanlar = asal_carpanlari_bul(sayi)
print(f"{sayi} sayısının asal çarpanları: {asal_carpanlar}")



