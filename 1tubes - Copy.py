import modultubes
import random
import pyfiglet
from colored import fg

#colorfg
blue1 = fg('light_sky_blue_3a')   
blue2 =  fg('light_sky_blue_3b')   
blue3 = fg('sky_blue_2')        
blue4 = fg('chartreuse_2b')    

deep_pink_4c = fg('deep_pink_4c')
medium_violet_red = fg('medium_violet_red')
darkviolet = fg('dark_violet_1b')
purple = fg('purple_1b')

red = fg('red_3a')
green = fg('green_1')
gold = fg('light_goldenrod_3')

kartu=modultubes.membuatkartu()

cekmenu=True
option=modultubes.begin()
if option=='register' :
    option=modultubes.access(option)
    data=modultubes.access(option)
else:
    data=modultubes.access(option)
chips=data[2]

while (cekmenu==True):
    main=modultubes.fungsimenu()
    
    while (main=="ya"):
        pemain=[]
        komputer=[]
        jumlahkartuas=0
        kartuasbernilai11=0
        poinpemain=0
        poinkomputer=0
        bet = int(input("ingin bertaruh berapa? "))

        pemain.append(modultubes.membagikartu(kartu))
        komputer.append(modultubes.membagikartu(kartu))
        pemain.append(modultubes.membagikartu(kartu))
        komputer.append(modultubes.membagikartu(kartu))

        jumlahkartuas=jumlahkartuas+modultubes.mengecekkartuas(pemain[0])
        jumlahkartuas=jumlahkartuas+modultubes.mengecekkartuas(pemain[1])

        poinpemain=modultubes.menghitungkartu(pemain[0]) + modultubes.menghitungkartu(pemain[1])
        poinkomputer=modultubes.menghitungkartu(komputer[0]) + modultubes.menghitungkartu(komputer[1])

        print()
        print("ini kartu yang kamu dapat",pemain)
        cek=modultubes.menghitungkartuas(jumlahkartuas)
        poinpemain=poinpemain+cek[0]
        kartuasbernilai11=cek[1]
        komputer1=komputer[0]
        print()
        print()
        print("ini jumlah kartu kamu sekarang",poinpemain)
        print("kartu komputer yang dibuka ",modultubes.membukakartukom(komputer))
        print()
        tambahkartu=str(input("Apakah kamu ingin menambah kartu? ya/tidak: "))
        while (tambahkartu=="ya" or poinkomputer<=17):
            if tambahkartu=="ya":
                cekpemain=modultubes.tambahkartu(kartu)
                jumlahkartuas=jumlahkartuas+modultubes.mengecekkartuas(cekpemain)
                poinpemain=poinpemain+modultubes.menghitungkartu(cekpemain)
                pemain.append(cekpemain)

                poinpemain=poinpemain-(10*kartuasbernilai11)
                kartuasbernilai11=0

                print("ini kartu kamu sekarang",pemain)
                cek=modultubes.menghitungkartuas(jumlahkartuas)
                poinpemain=poinpemain+cek[0]
                kartuasbernilai11=cek[1]
                print("ini jumlah kartu kamu sekarang",poinpemain)

            if poinkomputer<=17:
                cekkomp=modultubes.tambahkartu(kartu)
                poinkomputer=poinkomputer+modultubes.menghitungkartu(cekkomp)
                komputer.append(cekkomp)

            if tambahkartu=="ya":
                tambahkartu=str(input("Apakah kamu ingin menambah kartu? ya/tidak: "))
                print("kartu komputer yang dibuka ",komputer)
            print("")

        chips=modultubes.menghitunghasil(poinpemain,poinkomputer,chips,bet)
        modultubes.updatechips(data[0],data[1],chips)
        komputer.append(komputer1)
        print(komputer,"Jumlah poin komputer: ",poinkomputer)
        print("")
        main=str(input("Apakah kamu ingin main? ya/tidak: "))
