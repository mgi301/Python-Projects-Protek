#SOAL3
def bintang(n):
    tengah = 2*x+5 #centre
    kolom = 1
    looper=0
    while looper<x:
        v=('*'*kolom)
        print(v.center(tengah))
        looper+=1
        kolom+=2
    kolom-=4
    looper-=1
    while looper>0:
        v = ('*' * kolom)
        print(v.center(tengah))
        looper -= 1
        kolom -= 2
x=4 #masukkan jumlah bintang yang mau dibuat
bintang(x);