#Status kelulusan
#range nilai 0-100
A = "LULUS"
B = "TIDAK LULUS"
Bahasa= int(input("Masukkan nilai Bhs Indonesia : "));
IPA=int(input("Masukkan nilai IPA           : "));
Math=int(input("Masukkan nilai Matematika    : "));
if (Bahasa>100)or(Bahasa<0)or(IPA>100)or(IPA<0)or(Math>100)or(Math<0):
    print("Maaf input ada yang tidak valid")
elif (Bahasa>=60)and(IPA>=60)and(Math>=70):
    print("Status Kelulusan             : ",A)
else:
    print("Status Kelulusan             : ",B)