
def selectedFood():
    with open("Yemekler.txt", "r") as FILE:
        for YEMEK in FILE:
            print(YEMEK)


def foodName():
    Yemekad = input("Yemegin Adını Girin: ")
    with open("Yemekler.txt", "a") as FILE:
        FILE.write("Yemek Adı :" +  " " +Yemekad + '\n')


def writeMaterial():
    malzemeİsmi = input("*Sıra sıra giriniz *" +" "+'Malzeme Adı Girin: ')
    with open("Yemekler.txt", "a") as FILE:
        FILE.write( "Malzemeler" +" "+ malzemeİsmi + '\n')
       





while True:
    Food = input('1- Yemekleri Listele \n 2- Yemek Ekleyin \n 3-Malzeme Girin  \n 4- Exit\n')

    if Food == '1':
        selectedFood()
    elif Food == '2':
        foodName()
    elif Food == '3':
        writeMaterial()
    else:
        break

