#soal1
def ubahhuruf(matematik,a,b):
    newlist=[]
    for huruf in matematik:
        if huruf==a:
            huruf=b
        newlist.append(huruf)
        hasil=''.join(newlist)
    print(hasil)
    print(matematik.replace(a,b))
teks="MATEMATIKA"
test="T"
edit="S"
ubahhuruf(teks,test,edit);