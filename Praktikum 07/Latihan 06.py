print ('_____________________________')
print ('PROGRAM HITUNG RATA RATA')
print ('-----------------------------')
a=0
start=0
def masukan():
    try:
        global again
        global start
        global a
        bil = float(input('Masukkan bilangan bulat :    '))
        again = input(str('Lagi     (y/n) ? : '))
        start += bil
        a += 1
    except ValueError:
        print("Bukan bilangan bulat")
while True:
    masukan()
    if again=='n':
        break
print ('_____________________________')
mean = start/a
print('Rata - ratanya adalah : ', mean)