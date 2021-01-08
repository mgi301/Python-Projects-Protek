#Project1
file = open('D:/dataKaryawan.dat','w')

def addKaryawan(nip,nama,alamat,gol,tgllahir,umur):
    datakaryawan = []
    for data in (nip,nama,alamat,gol,tgllahir,umur):
        datakaryawan.append(data)
    output='|'.join(datakaryawan)+'\n'
    file.write(output)

from datetime import *
def getUsia(tgl):
    lahir = datetime.date(datetime.strptime(tgl, '%Y-%m-%d'))
    sekarang = datetime.date(datetime.today())
    umur = int((sekarang - lahir).days/365)
    return str(umur)

while True:
    nip     = input('Masukkan NIP       : ')
    name    = input('Masukkan Nama      : ')
    address = input('Masukkan Alamat    : ')
    while True:
        gol     = input('Masukkan Golongan  : ')
        if gol in ['A','B','C']:
            break
        else:
            print('Pilihan Input: A,B,C')
    birth   = input('Masukkan Tgl Lahir : ')
    addKaryawan(nip,name,address,gol,birth,getUsia(birth))
    print('')
    file.close
    again   = input('Tambah data  (y/n) : ')
    if again=='n':
        break