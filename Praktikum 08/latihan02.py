#PHYTON PROJECT
#Soal1
print('====================')
print('Mengurutkan Bilangan')
total=int(input('Tentukan banyak bilangan yang ingin dimasukkan :'))
print('====================')
index=0
n=1

e=[]
while True:
    print('Masukkan bilangan ke-',n,":",end =' ')
    bil=int(input())
    e.insert(index, bil)
    index+=1
    n+=1
    total-=1
    if total==0:
        break
e.sort()
print(e)