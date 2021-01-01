#Soal 02
#MAX PENGEMBALIAN BUKU 7 HARI!!!
printfile=open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 11/File no 2.txt','a')
#DOWNLOAD ALL REQUIRED FILE BEFORE TEST!
#Required file = File no 2.txt
import datetime
from datetime import*
today=datetime.date(datetime.today())
kembali=today+timedelta(days=7)
today=str(today)
kembali=str(kembali)
while True:
    datalist = []
    code=   input('Masukkan Kode Member     :')
    name=   input('Masukkan Nama Member     :')
    book=   input('Masukkan Judul Buku      :')
    repeat= input('Ulangi lagi     (y/n)    :')
    datalist.append(code)
    datalist.append(name)
    datalist.append(book)
    datalist.append(today)
    datalist.append(kembali)
    joint='|'.join(datalist)+'\n'
    printfile.write(joint)
    if repeat=='n':
        break
printfile.close()
printfile = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 11/File no 2.txt','r')
print(printfile.read())