#
import random
import time

def sayi_bul():
    liste = set()
    quit = False
    while quit == False:
        try:
            lenght = int(input("Listenin eleman sayısı kaç olsun? >>: "))
            if lenght <= 0 :
                raise ValueError
            a, b = map(int, input("Sayılar hangi aralıkta olsun. 2 sayı, aralarına virgül koyarak giriniz >>: ").split(","))

            if b < a :
                print("2.sayı 1.sayıdan küçük olamaz. Tekrar deneyiniz..")
            elif b-a+1 < lenght:
                print("Sayı aralığı liste uzunluğundan küçük. Tekrar deneyiniz..")
            else:
                quit = True
        except (ValueError):
            print("Lütfen geçerli sayı giriniz.")

    print(f"{a} ile {b} arasındaki sayılardan, elemanları birbirinden farklı, {lenght} elemanlı liste oluşturuluyor...")
    time.sleep(2)
    while len(liste) < lenght:
        liste.add(random.randint(a, b))
    print("Liste hazır..")
    time.sleep(0.5)

    kontrol = False
    while kontrol == False:
        try:
            sayigir = int(input("Kaç adet sayı seçmek istiyorsunuz? >>: "))
            if sayigir == 0 or sayigir < 0 :
                raise ValueError
            elif sayigir <= lenght :
                kontrol = True
            else:
                raise ValueError
        except (ValueError):
            print("Seçilecek sayı 0 veya 0'dan küçük olamaz..")
            print("Seçilecek sayı sayısı liste eleman sayısından büyük olamaz. Tekrar deneyiniz..")

    sayilar = []
    sansli_sayilar= []

    for i in range(sayigir):

        correct = False
        while correct == False:
            try:
                bulunacak = int(input(f"{i+1}. İstediğiniz sayıyı giriniz >>: "))
                if bulunacak not in range(a, b+1):
                    print("Girilen aralığın dışında sayı seçtiniz, Tekrar deneyiniz..")
                else:
                    sayilar.append(bulunacak)
                    correct = True
            except (ValueError):
                print("Lütfen geçerli sayı giriniz.")

    count = 0
    for sayi in sayilar:
        if sayi in liste:
            count += 1
            sansli_sayilar.append(sayi)
    if count > 0:
        print(f"*** Şanslısınız...{len(liste)} elemanlı listede {count} sayıyı denk getirdiniz.***")
    else:
        print("Seçtiğiniz hiçbir sayı listede yok :(")

    goster = input("Tüm liste ve seçtiğiniz sayılar gösterilsin mi? (E)vet >>: ")
    if goster == "e":
        print(f"Tüm liste : {list(sorted(liste))}")
        print(f"Seçtiğiniz sayılar : {sorted(sayilar)}")
        print(f"Şanslı sayılar : {sorted(sansli_sayilar)}")
    else:
        print("Tekrar bekleriz.. İyi şanslar..")

sayi_bul()



