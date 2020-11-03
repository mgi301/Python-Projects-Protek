start=0
end=100
total=0
count=0
while True:
    if start % 2 == 1:
        count+=start
        print(start)
        start+=1
        total+=1

    else:start+=1
    if start>=end:
        break
print("Banyaknya bilangan ganjil :",total)
print("Jumlah seluruh bilangan :",count)