#PHYTON PROJECT
#Soal2
def dataStat(x):
    list=[]
    x = tuple(x)
    sum=0
    for total in range (len(x)):
        continue
    for bil in x:
        sum+=bil
        all=total+1
    avg=sum/all
    halo=(min(x))
    waloo=(max(x))
    list.append(avg)
    list.append(waloo)
    list.append(halo)
    print (list)
a=[1,2,3,4,5,6,7,8,9,10]
dataStat(a)