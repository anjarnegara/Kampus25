
# jawaban nomor 1.A
suku = int(input("input suku:"))

while suku > 50:
    suku -= 25
    suku += 10
else:
    suku += 10
print(suku)


# jawaban nomor 1.B
n = int(input("input bilangan: "))

hasil = 0

if n > 50:
    hasil = n - 25
else:
    hasil = n + 10
print(hasil)





# jawaban nomor 4
sisi_pertama = int(input("isi sisi pertama segitiga = "))
sisi_kedua = int(input("isi sisi kedua segitiga = "))
sisi_ketiga = int(input("isi sisi ketiga segitiga = "))

def cek_sisi(sisi_pertama, sisi_kedua, sisi_ketiga):
    if sisi_pertama == sisi_kedua == sisi_ketiga:
        print("SAMA SISI")
    elif sisi_pertama == sisi_kedua != sisi_ketiga:
        print("SAMA KAKI")
    elif sisi_pertama != sisi_kedua == sisi_ketiga:
        print("SAMA KAKI")
    else:
        print("SEMBARANG")
        

cek_sisi(sisi_pertama, sisi_kedua, sisi_ketiga)





# jawaban nomor 5
def hitung_status_kelulusan():
   
    nilai_mk1 = int(input("Masukkan nilai mata kuliah 1: "))
    nilai_mk2 = int(input("Masukkan nilai mata kuliah 2: "))
    nilai_mk3 = int(input("Masukkan nilai mata kuliah 3: "))

    jumlah_lulus = 0

    if nilai_mk1 >= 60:
        jumlah_lulus += 1
    if nilai_mk2 >= 60:
        jumlah_lulus += 1
    if nilai_mk3 >= 60:
        jumlah_lulus += 1

    if jumlah_lulus == 3:
        print("TIGA")
    elif jumlah_lulus == 2:
        print("DUA")
    elif jumlah_lulus == 1:
        print("SATU")
    else:
        print("NOL")

hitung_status_kelulusan()