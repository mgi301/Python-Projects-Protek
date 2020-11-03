from random import randint
score=100
bil=randint(0,100)
print(bil)
idk=int(input("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!"))
while True:
    if (idk > bil):
        print("Tebakan anda :", idk)
        idk = int(input("Hehehe… Bilangan tebakan anda terlalu besar"))
        score-=2
        if score <= 0:
            score = 0
    if (idk < bil):
        print("Tebakan anda :", idk)
        idk = int(input("Hehehe… Bilangan tebakan anda terlalu kecil"))
        score-=2
        if score <= 0:
            score = 0
    if (idk==bil):
        break
print("Tebakan anda :", idk)
print("Yeeee… Bilangan tebakan anda BENAR :-)")
print(" ")
print("Score Anda: ",score)
