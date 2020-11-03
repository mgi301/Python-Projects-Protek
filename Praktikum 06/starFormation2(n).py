def starFormation2(n):
    baris = 5
    kolom = 5
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
starFormation2(N)