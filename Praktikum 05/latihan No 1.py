#Status kelulusan
#range nilai 0-100
Bahasa= int(input("Masukkan nilai Bhs Indonesia : "));
IPA=int(input("Masukkan nilai IPA           : "));
Math=int(input("Masukkan nilai Matematika    : "));
A = "LULUS"
B = "TIDAK LULUS"
if (Bahasa>=60)and(IPA>=60)and(Math>=60):
    if(Math>70):
        print("Status Kelulusan             : ",A)
else:
    print("Status Kelulusan             : ",B)