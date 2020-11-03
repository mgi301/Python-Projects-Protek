def starFormation3(n):
    baris = n-1
    kolom = n-1
    i = 0
    while (i < baris):
        j = 0

        while (j < kolom - baris + 1):
            print("* ", end=" ")
            j += 1
        print(" ")
        kolom += 1
        i += 1
def starFormation4(n):
    baris = n
    kolom = n
    i = 0
    while (i < baris):
        j = 0
        while (j < kolom):
            print("* ", end=" ")
            j += 1
        print(" ")
        kolom -= 1
        i += 1
N=int(input(" "))
M=N/2
starFormation3(M)
starFormation4(M)