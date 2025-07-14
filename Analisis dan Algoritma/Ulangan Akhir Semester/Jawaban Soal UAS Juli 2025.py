"""
                SOAL UAS ANALISIS DAN ALGORITMA


1. Sudah ada array satu dimensi yang dibuat dengan int A[11].Sudah ada isinya dengan ilustrasi
sebagai berikut:

[12, 17, 10, 5, 15, 25, 11, 7, 25, 16, 19]

Susun program untuk:
a. Mencari dan mencetak isi array yang nilainya TERKECIL. Untuk contoh data diatas, bila
rogram dijalankan maka akan tercetak :5.
b. Mencetak ada berapa nilai TERKECIL dalam array tersebut. Untuk contoh data diatas, bila
program dijalankan maka akan tercetak :1.
c. Mencetak berada diposisi (index) berapa, nilai TERKECIL dalam array tersebut. Untuk contoh
data diatas, bila program dijalankan maka akan tercetak :3.





2. Sudah ada array NILAI satu dimensi yang dibuat dengan int NILAI[12], sudah adaisinya yang
merupakan nilai mahasiswa, dengan ilustrasi sebagai berikut:

[65, 70, 50, 45, 60, 80, 90, 55, 75, 85, 40, 70]

Sudah ada array LULUS[12] dan GAGAL[12] yang (dianggap) masih belum ada isinya.
Susun program untuk memindahkan setiap isi array NILAI yang lebih besar atau sama
dengan 60 ke array LULUS dan sebaliknya ke array GAGAL. Selanjutnya tampilkan isi
array LULUS dan GAGAL serta jumlah mahasiswa yang LULUS dan GAGAL!





3. Sudah ada array A satu dimensi yang dibuat dengan int A[12], sudah ada isinya yang
merupakan nilai mahasiswa, dengan ilustrasi sebagai berikut:

[ 60, 80, 55, 90, 75, 40, 50, 85, 70, 65, 45, 55 ]

Sudah ada array B[12] dan C[12] yang (dianggap) masih belum ada isinya. Susun
program untuk menghitung rata-rata nilai mahasiswa dari array A. Selanjutnya periksaisi array
A. Jika isi array A lebih dari nilai rata-rata, maka pindahkan nilainya ke array
B. Sedangkan jika isi array A kurang dari nilai rata-rata, maka pindahkan ke array
C. Tampilkan isi array A, B dan C!





4. Diberikan array A = [5, 8, 12, 20, 25, 30].
Pisahkan array ini menjadi dua bagian: bagian pertama berisi elemen indeks 0 sampai 2, dan bagian
kedua indeks 3 sampai 5. Tulis hasilnya!





5. Tulislah program Python untuk memecah array [1, 2, 3, 4, 5, 6, 7, 8] menjadi 4 bagian yang
masing-masing berisi 2 elemen!


"""

print("------------------------Soal NO 1 -----------------------------\n\n")
# mencari nilai terkecil
Angka_array = [12, 17, 10, 5, 15, 25, 11, 7, 25, 16, 19]
Terkecil = min(Angka_array) 
print(f"angka terkecil dari array {Terkecil}")




# mencari jumlah nilai terkecil dalam array
res = 0
for a in Angka_array:
    if a == Terkecil:
        res += 1

print(f"ada {res} angka kecil dalam array yang ditemukan ")



# mencari posisi index
nilai_terkecil = []
for b in range(len(Angka_array)):
    if Angka_array[b] == Terkecil:
        nilai_terkecil.append(b)

if len(nilai_terkecil) == 1:
    print(f"Index angka terkecil: {nilai_terkecil[0]}")
else:
    print(f"Index angka terkecil: {nilai_terkecil}\n\n\n")





print("------------------------ Soal NO 2 -----------------------------\n")

nilai_ujian = [65, 70, 50, 45, 60, 80, 90, 55, 75, 85, 40, 70]

yang_lulus = []  
yang_gagal = []  

for nilai_mahasiswa in nilai_ujian:
    if nilai_mahasiswa >= 60:
        yang_lulus.append(nilai_mahasiswa)
    else:
        yang_gagal.append(nilai_mahasiswa)

print("Isi Array LULUS:")
print(yang_lulus)

print("\nIsi Array GAGAL:")
print(yang_gagal)

# Menampilkan jumlah mahasiswa yang LULUS dan GAGAL
print(f"\nJumlah Mahasiswa LULUS: {len(yang_lulus)}")
print(f"Jumlah Mahasiswa GAGAL: {len(yang_gagal)}\n\n\n")










print("------------------------ Soal NO 3 -----------------------------")

A = [ 60, 80, 55, 90, 75, 40, 50, 85, 70, 65, 45, 55 ]

B = []
C = []


total_nilai = sum(A)    # menjumlah total nilai
jumlah_mahasiswa = len(A)   # jumlah mahasiswa (12)
rata_rata = total_nilai / jumlah_mahasiswa  # hitung rata-rata


print(f" jawaban no 3 Rata-rata nilai mahasiswa: {rata_rata:.2f}") # biar komanya gk banyak

for nilai_mahasiswa in A:
    if nilai_mahasiswa > rata_rata:
        B.append(nilai_mahasiswa)   # klo nilai  mahasiswa lebih dari rata-rata masukin ke B
    elif nilai_mahasiswa < rata_rata:
        C.append(nilai_mahasiswa)   # klo dibawah masukin ke C
    

"""
        A. Jika isi array A lebih dari nilai rata-rata, maka pindahkan nilainya ke array

        dibuktikan dengan program
"""
print(f"nilai yang lebih dari {rata_rata:.2f} berada dalam array = {B}")  


"""
        B.Sedangkan jika isi array A kurang dari nilai rata-rata, maka pindahkan ke array

        dibuktikan dengan program
"""
print(f"nilai yang kurang dari {rata_rata:.2f} berada dalam array = {C}")

"""
        C. Tampilkan isi array A, B dan C!

        dibuktikan dengan program
"""
print(f"isi array A = {A}")
print(f"isi array B = {B}")
print(f"isi array C = {C}\n\n")








print("------------------------ Soal NO 4 -----------------------------")

A = [5, 8, 12, 20, 25, 30]

# 0 - 2
bagian_pertama = A[0:3]

# 3 - 5 
bagian_kedua = A[3:6] # ditulis 6 karena indeks dari 0

print(f"Array original: {A}")
print(f"Array pisahan pertama (indeks 0-2): {bagian_pertama}")
print(f"Array pisahan kedua (indeks 3-5): {bagian_kedua}\n\n")












print("------------------------ Soal NO 5 -----------------------------\n")

array_awal = [1, 2, 3, 4, 5, 6, 7, 8]

# 0 dan 1
bagian1 = array_awal[0:2]

# 2 dan 3
bagian2 = array_awal[2:4]

# 4 dan 5
bagian3 = array_awal[4:6]

# 6 dan 7
bagian4 = array_awal[6:8]

print(f"Array Original: {array_awal}")
print(f"Bagian 1: {bagian1}")
print(f"Bagian 2: {bagian2}")
print(f"Bagian 3: {bagian3}")
print(f"Bagian 4: {bagian4}")