#open file
file = open("d:/KULIAH/PROTEK/Python Projects/Python-Projects-Protek/Praktikum 07/data.txt", "r")
#read 1st line
bil1 = int(file.readline())
#read 2nd line
bil2 = int(file.readline())
#bagi
try:
    hasil = bil1 / bil2
    print(bil1, 'dibagi', bil2, 'sama dengan', hasil)
except ZeroDivisionError:
    print ('Tidak boleh pembagian dengan nol!')