#1
a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
#2
a.insert(2,10)
b.insert(1,15)
print('====================')
print('NO 2')
print('a ',a)
print('b ',b)
#3
a.append(4)
b.append(8)
print('====================')
print('NO 3')
print('a ',a)
print('b ',b)
#4
a.sort()
b.sort()
print('====================')
print('NO 4')
print('a ',a)
print('b ',b)
#5
c = a[:7]
d = b [1:9]
print('====================')
print('NO 5')
print (c)
print (d)
print('====================')
#6
e=[]
for i in range (len(c)):
    e.insert(i,c[i]+d[i])
for x in range (len(c)):
    continue
for y in range (len(d)):
    continue
if x>y:
    e.insert(x,d[x]) #khusus masalah ini
if y>x:
    e.insert(y,d[y]) #hanya khusus masalah ini
print('====================')
print('NO 6')
print (e)
#7
e=tuple(e)
print('====================')
print('NO 7')
print (e)
print('====================')
print('NO 8')
print(min(e))
print(max(e))
print(sum(e))
print('====================')
print('NO 10')
#9
myString='phyton adalah bahasa pemrograman yang menyenangkan'
myString=set(myString)
#10
print (myString)
print('====================')
#11
print('NO 11')
myString=list(myString)
myString.sort()
print(myString)
