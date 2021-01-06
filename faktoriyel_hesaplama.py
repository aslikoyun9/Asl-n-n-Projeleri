sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz:"))
deger = 1
for i in range(sayi):
    deger = deger * (i + 1)

print("Faktoriyel : ", deger)