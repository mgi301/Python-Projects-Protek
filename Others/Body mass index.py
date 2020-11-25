#C0de by:Ahmad Mishbahuddin_K3520007
print ('=======Body Mass Index========')
weight = float(input("Masukkan berat badan (dalam Kg)       : "))
height = float(input("Masukkan tinggi badan (dalam Meter)   : "))
print ('==============================')
BMI=weight/(height * height)
if BMI<18:
    result="KURUS"
elif (BMI<23):
    result="IDEAL"
elif (BMI<27):
    result="GEMUK"
elif (BMI<35):
    result="OBESITAS"
elif (BMI>=35):
    result="OBESITAS MORBID"
print('Status berat badan   :', result)
print ('------------------------------')