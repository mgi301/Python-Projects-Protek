#Soal 6
file=open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/File soal 6_1.txt', 'r')
tulis=open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/File soal 6 encoded.txt','w')
#PLESE DOWNLOAD FILENYA
#ENCODER
for line in file:
    line = line.rstrip('\n')
    line = line.split(' ')
    for value in line:
        try:
            angka=(int(value))
            save=str(angka)
        except ValueError:
            continue
        del line[line.index(save)]
    word = line
    newword = []
    for letter in word:
        character=letter.split()
        fixit = []
        for kata in character:
            for huruf in kata:
                geser = angka
                if ord(huruf)+geser>90:
                    geser=ord(huruf)+geser-90+64
                    new=chr(geser)
                if ord(huruf)+geser<=90:
                    geser=ord(huruf)+geser
                    new=chr(geser)
                fixit.append(new)
                done=''.join(fixit)
            newword.append(done)
            hasil=' '.join(newword)
    hasil = ' '.join(newword) + ' ' + save + '\n'
    print('Spoler! Encoded: \n', hasil)
    tulis.write(hasil)
file.close()
tulis.close()