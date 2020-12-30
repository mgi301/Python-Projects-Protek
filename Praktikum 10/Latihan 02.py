#Soal 2
retry="y"
newfile = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/File soal 2.txt','w')
newfile.close()
newfile = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/File soal 2.txt','a+')
#PLESE DOWNLOAD FILENYA
while retry=="y":
    NIM    = input('Masukkan NIM            :')
    name   = input('Masukkan Nama Mhs       :')
    address= input('Masukkan Alamat         :')
    retry  = input('Ulangi input lagi (y/n) :')
    printthis=NIM+'|'+name+'|'+address+'\n'
    newfile.write(printthis)
newfile.seek(0,0)
print('isi file yang dihasilkan :')
read=newfile.read()
print(read)
newfile.close()