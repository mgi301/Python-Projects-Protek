#PHYTON PROJECT
#Soal10
#tidak menerina kesalahan input
buah={'apel':5000,"jeruk":8500,'mangga':7800,'duku':6500}
awal=0
while True:
    want=str(input('Nama buah yang dibeli   :'))
    total=int(input('Berapa Kg               :'))
    again=str(input('beli buah yang lain (y/n) :'))
    harga=buah[want]*total
    awal+=harga
    if again=='n':
        break
print("___________________________________")
print('Total Harga             :',awal)