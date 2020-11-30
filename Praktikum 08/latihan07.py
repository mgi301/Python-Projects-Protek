#PHYTON PROJECT
#Terinspirasi dari SOAL 3
#Soal6
#Saya memeahami bahwa program ini belum 100% berhasil
def sortStringByChar(bil):
    total = len(bil)
    e=[]
    index=0
    while True:
        for data in bil:
            var=tuple(data)
            got = len(data)
            e.insert(index,data)
            help=index+1
            e.insert(help,got)
            index+=2
            total-=1
        if total==0:
            break
    print('==============================')
    #test index
    index = 1
    while True:
        y=len(e)-2
        if e[index]>e[index+2]: #TIDAK BERFUNGSI SELAIN SOAL INI
            e.insert(index-1,e[index+1])
            e.insert(index+2,e[index])
            del e[index]
            del e[index+2]
        index += 2
        if index>y:
            break
    index=1
    while True: #PEMBERSIHAN
        y =len(e)-1
        del e[index]
        index+=1
        if index>y:
            break
    print (e)
listMyData = ['apel', 'rambutan','jeruk']
sortStringByChar(listMyData)