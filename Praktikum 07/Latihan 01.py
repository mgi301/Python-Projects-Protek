try :
    file = open("D:/KULIAH/PROTEK/Python Projects/Python-Projects-Protek/Praktikum 07/yfile.txt", 'r')
    print (file.read())
except (FileNotFoundError):
    print('File tidak ditemukan')
#test
#except (FileNotFoundError, FileNotFoundError(2, 'No such file or directory'):
