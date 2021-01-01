#soal 01
import datetime
from datetime import *
def diffDate(x):
    #STRIPTIME saya dapat dari stackoverflow
    when=datetime.date(datetime.strptime(x,'%Y-%m-%d'))
    sekarang=datetime.date(datetime.now())
    selisih=(sekarang-when).days
    if selisih>=0:
        return selisih
    if selisih<0:
        return selisih*-1
today='2018-12-30'
print(diffDate(today))