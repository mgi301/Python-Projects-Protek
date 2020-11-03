start=0
end=100
total=0
while True:
    if start % 2 == 1:
        print(start)
        start+=1
        total+=1
    else:start+=1
    if start>=end:
        break
print("Banyaknya bilangan ganjil :",total)