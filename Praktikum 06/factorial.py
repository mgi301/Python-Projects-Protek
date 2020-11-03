#combinasi
def faktorial(a):
    b=a
    while True:
        a -= 1
        b *= a
        if a == 1:
            break
    return b
def Combine(n,r):
    hasil=faktorial(n)/faktorial(n-r)
    return hasil
def Permutasi(x,d):
    hasil = faktorial(x) / (faktorial(x - d) * faktorial(d))
    return hasil

N=5
R=3
print (Combine(N,R))
N=10
R=3
print (Permutasi(N,R))