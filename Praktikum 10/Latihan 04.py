#Soal 4
test = input('Masukkan NIM yang mau dicari: ')
file=open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/File soal 2.txt','r')
#PLESE DOWNLOAD FILENYA
readthis = file.readlines()
dataMhs=[]
for value in readthis:
    newdata = value.rstrip()
    fresh = newdata.split('|')
    databaru={}
    databaru['nim']=fresh[0]
    databaru['nama']=fresh[1]
    databaru['alamat']=fresh[2]
    dataMhs.append(databaru)
baris=1
for key in dataMhs:
    if key['nim'] == test:
        print('NIM      :', key['nim'])
        print('Nama     :', key['nama'])
        print('Alamat   :', key['alamat'])
        break
    if baris==len(dataMhs):
        print('Data mahasiswa tidak ditemukan')
    baris+=1