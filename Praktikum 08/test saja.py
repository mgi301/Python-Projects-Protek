hargabuah = {'jeruk':10000, 'mangga':5000}
hargabuah['nangka'] = 6000
print(hargabuah.items())
for x,y in (hargabuah.items()):
    print(x ,'halo', y)
data = list(hargabuah.values())
print (data)
for a in hargabuah.values():
    print (a)
buah = 'nangka'
print(hargabuah.get(buah,500))
print (hargabuah)
print (hargabuah['jeruk'])