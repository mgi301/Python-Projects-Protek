#Soal 5
file=open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/File soal 5.txt','r')
#PLESE DOWNLOAD FILENYA
for line in file:
    line=line.rstrip('\n')
    line=line.split('|')
    total=0
    for angka in line:
        try:
            angka=int(angka)
            total+=angka
        except ValueError:
            print('\"',angka,'\" Bukan bilangan')
            break
    print (total)

