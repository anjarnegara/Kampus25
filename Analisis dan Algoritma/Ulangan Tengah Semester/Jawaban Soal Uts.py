"""
        Deret Geometri

        rumus: Un = ar**n-1

        un = suku ke n
        a  = suku pertama
        r  = rasio
        n  = banyaknya suku
"""
def deret_geometri(a, r, n):
  if n >= 0:
   return [a * (r ** i) for i in range(n)]

suku_pertama = 5
rasio = 3
jumlah_suku = 10
hasil_deret = deret_geometri(suku_pertama, rasio, jumlah_suku)
print(f"Deret geometri: {hasil_deret}")

"""
    U1 = 1.2**1-1
       = 1.1
       = 1

    U2 = 1.2**2-1
       = 1.2
       = 2
"""