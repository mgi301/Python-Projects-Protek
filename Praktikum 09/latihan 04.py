#SOAL 4
import random
def shufflestring(x,n):
    result=[]
    if n > 2*len(x):
        n=(len(x)*2)
        print("Jumlah pengacakan lebih dari jumlah acak yang dapat dilakukan")
        print('jumlah pengacakan diubah ke ',n)
    while n>0:
        acak = random.sample(x, len(x))
        done = ''.join(acak)
        if (done in result)==True:
            n+=1
        if (done in result)==False:
            result.append(done)
        n -= 1
    print(result)

shufflestring('aku',100);