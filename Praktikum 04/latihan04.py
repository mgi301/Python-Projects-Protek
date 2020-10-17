#soal1
bill12jam = 200000
billnext = 10000
jam_start = 6
menit_start = 0
jam_end = 23
menit_end = 50
jam_test = (jam_end - jam_start)
biaya1 = bill12jam + ((jam_test - 12) + (menit_end - menit_start)/60) * billnext
if (jam_test>12):
    print ("jawaban soal 1 :")
    print (int(biaya1),'Rupiah')
elif (jam_test<12):
    print("jawaban soal 1 :")
    print (bill12jam, 'Rupiah')

#soal2
total_distance = 795
efficiency1 = 1
efficiency2 = 12
liters_needed = total_distance * efficiency1 / efficiency2
print ("jawaban soal 2 :")
print (liters_needed, 'liter')

#soal3
tank_capacity = 50
X_refuel = int(liters_needed//tank_capacity)
print ("jawaban soal 3 :")
print (X_refuel, 'kali')

#soal4
print ("jawaban soal 4 :")
jam_start = 6
menit_start = 0
rest_jam = 0
rest_menit = 45
distance_A_B = 125
speed_A_B = 62
distance_B_C = 256
speed_B_C = 70
total_jam = int(distance_A_B/speed_A_B) + int(distance_B_C/speed_B_C)
total_menit = (distance_A_B%speed_A_B)/speed_A_B * 60
total_menit2 = (distance_B_C%speed_B_C)/speed_B_C * 60
total_menit3 = total_menit + total_menit2+rest_menit
end_jam = jam_start + total_jam
end_menit = (total_menit3)
if (end_menit)<60:
    print ('pak amir sampai ke kota c pada pukul ',end_jam,':',end_menit)
if (end_menit)>60:
    add_hour = int(end_menit//60)
    add_menit = end_menit%60
    ext_jam = end_jam + add_hour
    ext_menit = int(add_menit)
    print ('pak amir sampai ke kota c pada pukul ',ext_jam,':',ext_menit)

#soal5
print ("grafik soal 5 :")
mhs_laki = 100
mhs_perempuan = 150
print ("mahasiawa laki laki :")
print ('|' * (mhs_laki//10))
print ("mahasiswa perempuan :")
print ('|' * (mhs_perempuan//10))