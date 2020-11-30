#PHYTON PROJECT
#Terinspirasi dari no2
#Soal5
def kuadrat(bil):
    index=0
    hasil=[]
    for nilai in bil:
        pangkat=nilai**2
        hasil.insert(index,pangkat)
        index+=1
    print(hasil)
x=[2,4,5,6]
kuadrat(x)
