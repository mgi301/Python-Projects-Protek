#file tester
#write
myfile = open ('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/file editor.txt', 'w')
myfile.write('hello world\n'*3)
myfile.close()
#append
myfile = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/file editor.txt', 'a')
myfile.write('belajar phython menyenangkan\n')
myfile.close()
#read
myfile = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/file editor.txt', 'r')

while True:
    text=myfile.read(1)
    if not text:
        break
    print(text,end="")
#read #2
myfile.close()
myfile = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/file editor.txt', 'r')
teks = myfile.read()
print(teks,end='')
myfile.close()
#FILE CUMA BISA DI READ SEKALI AFAIK
#read advanced
myfile = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/file editor.txt', 'r')
line = myfile.readlines()
print(line)
myfile.close()
#NVM TERNYATA CARA KERJA FILE PAKE POINTER
myfile = open('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/file editor.txt', 'a+')
myfile.write('FINE')
myfile.seek(0,0)
read=myfile.read()
print(read,end='Ganti nama')
myfile.close()
#gantinama
import os
os.remove('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/file editor.txt')
os.mkdir('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/myfile')
os.rmdir('D:\KULIAH\PROTEK\Python Projects\Python-Projects-Protek\Praktikum 10/myfile')