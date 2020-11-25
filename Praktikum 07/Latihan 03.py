file = open("d:/KULIAH/PROTEK/Python Projects/Python-Projects-Protek/Praktikum 07/data2.txt", "r")
sum = 0
for value in file:
    try:
        sum = sum + int(value)
        print(sum)
    except ValueError:
        print ('Input bukan bilangan bulat')