#Soal 1
#file= "Bassbooster"

openthis = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/File soal 1.txt', 'r')
#PLESE DOWNLOAD FILENYA
read=openthis.readlines()
ganjil=0
genap=0
for x in read:
    x=int(x)
    if x % 2 == 0:
        genap+=1
    elif x % 2 == 1:
        ganjil+=1
    else:
        continue
print('Banyaknya bilangan genap : ',genap)
print('Banyaknya bilangan ganjil: ',ganjil)