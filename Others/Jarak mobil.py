#C0de by:Ahmad Mishbahuddin_K3520007
print ('=======Kecepatan Per Detik=======')
speed_start= float(input('Masukkan kecepatan awal (dalam m/s): '))
acceleration= float(input('Masukkan percepatan (dalam m/s^2)  : '))
print ('=================================')
T_end = 10 #Rubah value ini bila ingin daftar lebih panjang
t=1 #JANGAN RUBAH INI
while True:
    S = (speed_start * t) + (0.5 * acceleration * t * t)
    if t<10:
        print('t =', t, ',    S(t) = ', S, 'Meter')
    if t>=10: #Untuk merapikan saja
        print('t =', t, ',   S(t) = ', S, 'Meter')
    t+=1
    if t == T_end+1:
        break
print ('--------------------------------')