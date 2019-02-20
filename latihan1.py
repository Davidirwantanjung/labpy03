print("********latihan1********")
print("menampilkan bilangan acak yang lebih kecil dari 0,5")
print("nama :davidirwantanjung")
print("nim  :311810336")
print("kelas:18.B.2")

import random

jumlah = int(input("masukan jumlah n : "))
a = 0

for i in range(jumlah):
    a +=1
    b = random.uniform(.0,.5)
    print('data ke :',a,'"==>',b)
print("********finish**********")