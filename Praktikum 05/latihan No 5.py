#Gaji pokok dan golongan
kode=input ("Masukkan kode karyawan               :")
name=input ("Masukkan nama karyawan               :")
gol=input ("Masukkan golongan                    :")
status=int(input ("Masukkan status/(1:menikah,2:blm)    :"))
if (status==1):
    stat="menikah"
    anak=int(input("Masukkan jumlah anak                 :"))
if (status==2):
    stat="belum menikah"
plus_sutri = 10
plus_anak = 5
if (gol=="A"):
    pokok = 10000000
    cut = 2.5
    if (status==1):
        plus_sutri=plus_sutri/100*pokok
        plus_anak=plus_anak/100*pokok
        total=plus_sutri+plus_anak+pokok
        cut_value=cut/100*total
        clear=total-cut_value
    else:
        cut_value = cut / 100 * pokok
        clear = pokok-cut_value
if (gol=="B"):
    pokok = 8500000
    cut = 2
    if (status == 1):
        plus_sutri = plus_sutri / 100 * pokok
        plus_anak = plus_anak / 100 * pokok
        total = plus_sutri + plus_anak + pokok
        cut_value = cut / 100 * total
        clear = total - cut_value
    else:
        cut_value = cut / 100 * pokok
        clear = pokok - cut_value
if (gol=="C"):
    pokok = 7000000
    cut = 1.5
    if (status == 1):
        plus_sutri = plus_sutri / 100 * pokok
        plus_anak = plus_anak / 100 * pokok
        total = plus_sutri + plus_anak + pokok
        cut_value = cut / 100 * total
        clear = total - cut_value
    else:
        cut_value = cut / 100 * pokok
        clear = pokok - cut_value
if (gol=="D"):
    pokok = 5500000
    cut = 1
    if (status == 1):
        plus_sutri = plus_sutri / 100 * pokok
        plus_anak = plus_anak / 100 * pokok
        total = plus_sutri + plus_anak + pokok
        cut_value = cut / 100 * total
        clear = total - cut_value
    else:
        cut_value = cut / 100 * pokok
        clear = pokok - cut_value
print("====================================")
print("STRUK RICIAN GAJI KARYAWAN")
print("------------------------------------")
print("Nama Karyawan            :",name,"   Kode:",kode)
print("Golongan                 :",gol)
print("Status Menikah           :",stat)
print("Jumlah Anak              :",anak)
print("------------------------------------")
print("Gaji Pokok               : Rp",pokok)
print("Tunjangan Istri/Suami    :",plus_sutri)
print("Tunjangan anak           :",plus_anak)
print("------------------------------------")
print("Gaji Kotor               : Rp",total)
print("Potongan (",cut,"%)          : Rp",cut_value )
print("------------------------------------")
print("Gaji Bersih              :",clear)