#TEST WOrk
import datetime
sekarang = datetime.datetime.now()
sekarang = str(sekarang)
print(type(sekarang))
print(sekarang)
from datetime import *
skrg = datetime.now()
tglnow = str(skrg.day)
print(skrg.day,skrg.month,skrg.year,skrg.hour)
skrg = datetime.today()
print(skrg.day,skrg.month,skrg.year,skrg.hour)
skrg=datetime.date(datetime.today())
print(skrg.day,skrg.month,skrg.year)
skrg=datetime.time(datetime.today())
print(skrg)
#TIme delta
import datetime
skrg= datetime.datetime.now()
print(skrg)
selisih=skrg-timedelta(days=1)+timedelta(hours=2)
print(selisih)
print(type(selisih))
from datetime import *
new='Wednesday,26 December,2020'
date1=datetime.strptime(new, '%A,%d %B,%Y')
print(date1)
date2=datetime.strftime(date1, '%A %B %y %Y')
print(date2)