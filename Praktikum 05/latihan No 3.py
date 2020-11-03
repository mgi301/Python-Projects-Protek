#Status kelulusan
#range nilai 0-100
Bahasa= int(input("Masukkan nilai Bhs Indonesia : "));
IPA=int(input("Masukkan nilai IPA           : "));
Math=int(input("Masukkan nilai Matematika    : "));
A = "LULUS"
B = "TIDAK LULUS"
if (Bahasa>100)or(Bahasa<0)or(IPA>100)or(IPA<0)or(Math>100)or(Math<0):
    print("Maaf input ada yang tidak valid")
elif (Bahasa>=60)and(IPA>=60)and(Math>=70):
    print("Status Kelulusan             : ",A)
elif (Bahasa<60)or(IPA<60)or(Math<70):
    print("Status Kelulusan             : ", B)
    print("Sebab")
    if(Bahasa<60):
        print("-	Nilai bahasa indonesia kurang dari 60")
    if(IPA<60):
        print("-	Nilai IPA kurang dari 60")
    if(Math<70):
        print("-	Nilai Matematika kurang dari 70")