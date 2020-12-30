#soal 3
openthis = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/File soal 2.txt','r')
#PLESE DOWNLOAD FILENYA
readthis = openthis.readlines()
dataMhs={}
newdict=1
#Sebenarnya saya sudah bikin dict seperti ini sebelumnya
#Tapi saya ubah jadi list, setelah diskusi sama temen jadi balik lagi ke
#bentuk dict seperti ini
#bentuk list dapat dilihat di soal 4
for value in readthis:
    newdata = value.rstrip()
    fresh = newdata.split('|')
    databaru={}
    databaru['nim']=fresh[0]
    databaru['nama']=fresh[1]
    databaru['alamat']=fresh[2]
    dataMhs[newdict]=databaru
    newdict+=1
print(dataMhs)
openthis.close()
