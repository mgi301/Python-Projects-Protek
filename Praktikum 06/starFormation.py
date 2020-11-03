def starFormation1(n):
    baris = n
    kolom = n
    i = 0
    while (i < baris):
        j = 0

        while (j < kolom - baris + 1):
            print("* ", end=" ")
            j += 1
        print(" ")
        kolom += 1
        i += 1
N=int(input(" "))
starFormation1(N)