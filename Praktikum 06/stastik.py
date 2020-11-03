def total(*myData):
    jumlah=0
    for test in myData:
        jumlah += test
    print (jumlah)
def avg(*myData):
    total=0
    jumlah=0
    for value in myData:
        total += value
        jumlah += 1
    avg=total/jumlah
    print (avg)
def max(*myData):
    min=0
    for value in myData:
        if(value > min):
            min=value
    print(min)
def min(*myData):
    max=9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    for value in myData:
        if (value<max):
            max=value
    print(max)

print('A')
print('Rata Rata :')
avg(5,10,4,9,30,16,2,11)
print("Nilai maksimum :")
max(5,10,4,9,30,16,2,11)
print("Nilai minimum")
min(5,10,4,9,30,16,2,11)
print('B')
print('Rata Rata :')
avg(81,98,12,83,45,77,69,30,56)
print("Nilai maksimum :")
max(81,98,12,83,45,77,69,30,56)
print("Nilai minimum")
min(81,98,12,83,45,77,69,30,56)