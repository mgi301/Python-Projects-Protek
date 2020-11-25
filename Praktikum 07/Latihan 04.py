name = input(str("Masukkan nama file: "))
print ('isi file', name, 'adalah:')
try :
    file = open(name, 'r')
    print (file.read())
except (FileNotFoundError):
    print('File tidak ditemukan')