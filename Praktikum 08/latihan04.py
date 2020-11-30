#PHYTON PROJECT
#Soal3
#COPAS DARI #1
print('====================')
print('JUmlah Huruf')
total=int(input('Tentukan banyak nama mahasiswa yang ingin dimasukkan :'))
print('====================')
index=0
n=1 #hitung mundur break
e=[]
while True:
    print('Masukkan bilangan ke-',n,":",end =' ')
    bil=str(input())
    e.insert(index, bil)
    index+=1
    total-=1
    if total==0:
        break
e.sort()
e=tuple(e)
print('==============hasil===============')
for bil in e:
    got=len(bil)
    print(bil, got,'karakter')
