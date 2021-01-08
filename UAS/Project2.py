#Project2
file = open('D:/dataKaryawan.dat','r')

#Download dan taruh file dari github secara manual ke drive D:, atau ikuti file
#yang telah di generate dari project 1

newdict={}
for line in file.readlines():
    line = line.rstrip('\n').split('|')
    newdict[line[0]]=line[-5:]

def getGapok(gol):
    if gol=='A':
        return '4.000.000'
    if gol=='B':
        return '4.500.000'
    if gol=='C':
        return '5.000.000'
    else:
        return 'Terdapat salah input golongan'

call = input('Masukkan Kode Karyawan: ')
print('')

try:
    print('Kode Karyawan    :',call)
    print('Nama Karyawan    :',newdict[call][0])
    print('Alamat           :',newdict[call][1])
    print('Golongan         :',newdict[call][2])
    print('Gaji Pokok       :',getGapok(newdict[call][2]))
    print('Tanggal Lahir    :',newdict[call][3], '(Usia:',newdict[call][4],'Tahun)',end='')
except KeyError:
    print('Data tidak ditemukan',end='')