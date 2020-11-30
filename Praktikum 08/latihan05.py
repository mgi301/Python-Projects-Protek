#PHYTON PROJECT
#Soal4
sayur = ['bayam', 'kangkung', 'selada']
print('====================')
print('MENU')
print('A.   Tambah data sayur')
print('B.   Hapus data sayur')
print('C.   Tampilkan data sayur')
print('====================')
#Jawab KAPITAL A,B,atau C
while True: #Memudahkan penguji
    result = str(input('Pilihan anda: '))
    if result=='A':
        new=str(input('Masukkan nama sayur yang ingin ditambahkan: '))
        sayur.append(new)
    if result=='C':
        for nama in sayur:
            print(nama)
    if result=='B':
        hapus=str(input("Masukkan nama sayur yang akan dihapus: "))
        try:
            nomor=sayur.index(hapus)
            del sayur[nomor]
        except ValueError: #Belum terbiasa in & not in
            print('Data tidak ditemukan')

    lagi=str(input('ingin mengulang?    (y/n)'))
    if lagi=='y':
        continue
    if lagi=='n':
        break