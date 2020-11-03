#Gaji pokok dan golongan
kode=input ("Masukkan kode karyawan     :")
name=input ("Masukkan nama karyawan     :")
gol=input ("Masukkan golongan          :")
if (gol=="A"):
    pokok =10000000
    cut = 2.5
    cut_value = cut/100*pokok
    clear = (100-cut)/100*pokok
if (gol=="B"):
    pokok = 8500000
    cut = 2
    cut_value = cut / 100 * pokok
    clear = (100 - cut) / 100 * pokok
if (gol=="C"):
    pokok = 7000000
    cut = 1.5
    cut_value = cut / 100 * pokok
    clear = (100 - cut) / 100 * pokok
if (gol=="D"):
    pokok = 5500000
    cut = 1
    cut_value = cut / 100 * pokok
    clear = (100 - cut) / 100 * pokok
print("====================================")
print("STRUK RICIAN GAJI KARYAWAN")
print("------------------------------------")
print("Nama Karyawan            :",name,"   Kode:",kode)
print("Golongan                 :",gol)
print("------------------------------------")
print("Gaji Pokok               : Rp",pokok)
print("Potongan (",cut,"%)          : Rp",cut_value )
print("------------------------------------")
print("Gaji Bersih              :",clear)
