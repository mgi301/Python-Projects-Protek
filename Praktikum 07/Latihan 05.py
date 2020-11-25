name = input(str("Masukkan nama file: "))
try:
    file = open(name, 'r')
    while True:
        newdata = input(str("Data yang mau ditambahkan: "))
        file = open(name, 'a')
        file.write(newdata)
        file.close()
        yesnt = input(str("mau lagi  (y/n): "))
        if yesnt == 'n':
            break
except (FileNotFoundError):
    print('File tidak ditemukan')