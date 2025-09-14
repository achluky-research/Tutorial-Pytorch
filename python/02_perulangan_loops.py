# ==================
# 1. FOR LOOP - BASIC
# ==================
print("\n1. FOR LOOP - BASIC")
print("-" * 20)

# Loop dengan range()
print("Loop dengan range(5):")
for i in range(5):
    print(f"Iterasi ke-{i}")

print("\nLoop dengan range(2, 8):")
for i in range(2, 8):
    print(f"Angka: {i}")

print("\nLoop dengan range(0, 10, 2) - step 2:")
for i in range(0, 10, 2):
    print(f"Angka genap: {i}")

# ==================
# 2. FOR LOOP DENGAN LIST
# ==================
print("\n2. FOR LOOP DENGAN LIST")
print("-" * 20)

buah_buahan = ["apel", "jeruk", "pisang", "anggur", "mangga"]

print("Iterasi langsung pada elemen:")
for buah in buah_buahan:
    print(f"Saya suka makan {buah}")

print("\nIterasi dengan index menggunakan enumerate:")
for index, buah in enumerate(buah_buahan):
    print(f"{index + 1}. {buah}")

print("\nIterasi hanya index:")
for i in range(len(buah_buahan)):
    print(f"Index {i}: {buah_buahan[i]}")

# ==================
# 3. FOR LOOP DENGAN STRING
# ==================
print("\n3. FOR LOOP DENGAN STRING")
print("-" * 20)

kata = "Python"
print(f"Mengiterasi karakter dalam '{kata}':")
for huruf in kata:
    print(f"Huruf: {huruf}")

# Menghitung karakter
nama = "Budi Santoso"
jumlah_vokal = 0
vokal = "aeiouAEIOU"

for huruf in nama:
    if huruf in vokal:
        jumlah_vokal += 1

print(f"\nDalam nama '{nama}' terdapat {jumlah_vokal} huruf vokal")

# ==================
# 4. FOR LOOP DENGAN DICTIONARY
# ==================
print("\n4. FOR LOOP DENGAN DICTIONARY")
print("-" * 20)

mahasiswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika",
    "ipk": 3.75
}

print("Iterasi key:")
for key in mahasiswa:
    print(f"Key: {key}")

print("\nIterasi key dan value:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

print("\nHanya value:")
for value in mahasiswa.values():
    print(f"Value: {value}")

# ==================
# 5. NESTED FOR LOOP
# ==================
print("\n5. NESTED FOR LOOP")
print("-" * 20)

print("Tabel perkalian 3x3:")
for i in range(1, 4):
    for j in range(1, 4):
        hasil = i * j
        print(f"{i} x {j} = {hasil:2d}", end="  ")
    print()  # New line setelah setiap baris

print("\nPola segitiga:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # New line setelah setiap baris

# ==================
# 6. WHILE LOOP - BASIC
# ==================
print("\n6. WHILE LOOP - BASIC")
print("-" * 20)

print("Countdown dengan while loop:")
counter = 5
while counter > 0:
    print(f"Counter: {counter}")
    counter -= 1
print("Selesai!")

# Input validation dengan while loop
print("\nValidasi input dengan while loop:")
password = ""
while len(password) < 8:
    password = "password123"  # Simulasi input
    if len(password) < 8:
        print("Password terlalu pendek, minimal 8 karakter")
        break  # Keluar dari simulasi
    else:
        print("Password valid!")

# ==================
# 7. WHILE LOOP DENGAN KONDISI KOMPLEKS
# ==================
print("\n7. WHILE LOOP DENGAN KONDISI KOMPLEKS")
print("-" * 20)

# Game tebak angka (simulasi)
import random

target = random.randint(1, 10)
tebakan = 0
attempts = 0
max_attempts = 3

print(f"Game tebak angka! (Target: {target} - untuk simulasi)")
while tebakan != target and attempts < max_attempts:
    attempts += 1
    tebakan = random.randint(1, 10)  # Simulasi tebakan
    print(f"Attempt {attempts}: Menebak {tebakan}")
    
    if tebakan == target:
        print(f"Benar! Angka {target} ditebak dalam {attempts} percobaan")
    elif attempts == max_attempts:
        print(f"Game over! Angka yang benar adalah {target}")
    elif tebakan < target:
        print("Terlalu kecil!")
    else:
        print("Terlalu besar!")

# ==================
# 8. BREAK DAN CONTINUE
# ==================
print("\n8. BREAK DAN CONTINUE")
print("-" * 20)

print("Contoh BREAK - berhenti ketika menemukan angka 7:")
for i in range(1, 11):
    if i == 7:
        print(f"Menemukan angka {i}, berhenti!")
        break
    print(f"Angka: {i}")

print("\nContoh CONTINUE - skip angka genap:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip angka genap
    print(f"Angka ganjil: {i}")

print("\nCombined break dan continue:")
for i in range(1, 21):
    if i % 3 == 0:  # Skip kelipatan 3
        continue
    if i > 15:  # Berhenti setelah 15
        break
    print(f"Angka: {i}")

# ==================
# 9. ELSE DALAM LOOP
# ==================
print("\n9. ELSE DALAM LOOP")
print("-" * 20)

# Else dengan for loop
print("Mencari angka prima pertama > 20:")
start = 21
for num in range(start, 30):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(f"Menemukan bilangan prima: {num}")
        break
else:
    print("Tidak menemukan bilangan prima dalam range")

# Else dengan while loop
print("\nWhile loop dengan else:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop selesai normal (tanpa break)")

# ==================
# 10. ENUMERATE() DAN ZIP()
# ==================
print("\n10. ENUMERATE() DAN ZIP()")
print("-" * 20)

# Enumerate
print("Menggunakan enumerate():")
makanan = ["nasi", "ayam", "sayur", "buah"]
for index, item in enumerate(makanan, start=1):
    print(f"{index}. {item}")

# Zip
print("\nMenggunakan zip():")
nama_siswa = ["Ali", "Budi", "Citra", "Dina"]
nilai_siswa = [85, 90, 78, 95]
kelas = ["A", "B", "A", "B"]

for nama, nilai, kls in zip(nama_siswa, nilai_siswa, kelas):
    print(f"{nama} (Kelas {kls}): {nilai}")

# ==================
# 11. LIST COMPREHENSION
# ==================
print("\n11. LIST COMPREHENSION")
print("-" * 20)

# Basic list comprehension
print("List comprehension dasar:")
squares = [x**2 for x in range(1, 6)]
print(f"Kuadrat 1-5: {squares}")

# List comprehension dengan kondisi
print("List comprehension dengan kondisi:")
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Kuadrat bilangan genap 1-10: {even_squares}")

# List comprehension dari string
print("List comprehension dari string:")
nama = "Python Programming"
vokal_dalam_nama = [huruf for huruf in nama if huruf.lower() in 'aeiou']
print(f"Vokal dalam '{nama}': {vokal_dalam_nama}")

# Nested list comprehension
print("Nested list comprehension untuk matrix:")
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix 3x3:")
for row in matrix:
    print(row)

# ==================
# 12. DICTIONARY DAN SET COMPREHENSION
# ==================
print("\n12. DICTIONARY DAN SET COMPREHENSION")
print("-" * 20)

# Dictionary comprehension
print("Dictionary comprehension:")
angka = [1, 2, 3, 4, 5]
dict_kuadrat = {x: x**2 for x in angka}
print(f"Dictionary kuadrat: {dict_kuadrat}")

# Set comprehension
print("Set comprehension:")
kalimat = "hello world"
unique_chars = {char for char in kalimat if char != ' '}
print(f"Karakter unik dalam '{kalimat}': {unique_chars}")

# ==================
# 13. CONTOH PRAKTIS: ANALISIS DATA SEDERHANA
# ==================
print("\n13. CONTOH PRAKTIS: ANALISIS DATA SEDERHANA")
print("-" * 20)

def analisis_nilai(data_mahasiswa):
    """
    Fungsi untuk menganalisis data nilai mahasiswa
    """
    print("=== ANALISIS NILAI MAHASISWA ===")
    
    total_nilai = 0
    jumlah_lulus = 0
    nilai_tertinggi = 0
    nilai_terendah = 100
    nama_terbaik = ""
    
    for nama, nilai in data_mahasiswa.items():
        total_nilai += nilai
        
        # Cek kelulusan
        if nilai >= 70:
            jumlah_lulus += 1
            status = "LULUS"
        else:
            status = "TIDAK LULUS"
        
        # Update nilai tertinggi dan terendah
        if nilai > nilai_tertinggi:
            nilai_tertinggi = nilai
            nama_terbaik = nama
        
        if nilai < nilai_terendah:
            nilai_terendah = nilai
        
        print(f"{nama}: {nilai} - {status}")
    
    # Hitung statistik
    jumlah_mahasiswa = len(data_mahasiswa)
    rata_rata = total_nilai / jumlah_mahasiswa
    persentase_lulus = (jumlah_lulus / jumlah_mahasiswa) * 100
    
    print(f"\n=== STATISTIK ===")
    print(f"Jumlah mahasiswa: {jumlah_mahasiswa}")
    print(f"Rata-rata nilai: {rata_rata:.2f}")
    print(f"Nilai tertinggi: {nilai_tertinggi} ({nama_terbaik})")
    print(f"Nilai terendah: {nilai_terendah}")
    print(f"Jumlah lulus: {jumlah_lulus}")
    print(f"Persentase lulus: {persentase_lulus:.1f}%")

# Test analisis data
data_nilai = {
    "Andi": 85,
    "Budi": 67,
    "Citra": 92,
    "Dina": 78,
    "Eko": 55,
    "Fani": 88
}

analisis_nilai(data_nilai)

# ==================
# 14. CONTOH PRAKTIS: GENERATOR PATTERN
# ==================
print("\n14. CONTOH PRAKTIS: GENERATOR PATTERN")
print("-" * 20)

def generate_fibonacci(n):
    """
    Generator untuk menghasilkan deret Fibonacci
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Deret Fibonacci 10 angka pertama:")
fibonacci_numbers = list(generate_fibonacci(10))
print(fibonacci_numbers)

# Generator expression
print("\nGenerator expression untuk bilangan genap:")
even_gen = (x for x in range(20) if x % 2 == 0)
print("5 bilangan genap pertama:", [next(even_gen) for _ in range(5)])

# ==================
# 15. CONTOH PRAKTIS: PENCARIAN DAN FILTERING
# ==================
print("\n15. CONTOH PRAKTIS: PENCARIAN DAN FILTERING")
print("-" * 20)

def cari_dan_filter_data(data_list, keyword="", min_value=0):
    """
    Fungsi untuk mencari dan memfilter data
    """
    hasil_pencarian = []
    
    for item in data_list:
        # Jika item adalah dictionary
        if isinstance(item, dict):
            # Cek apakah keyword ada di salah satu value
            found_keyword = any(keyword.lower() in str(v).lower() for v in item.values())
            
            # Cek nilai minimum jika ada field 'nilai' atau 'score'
            nilai_field = item.get('nilai', item.get('score', 0))
            meets_min_value = nilai_field >= min_value
            
            if found_keyword and meets_min_value:
                hasil_pencarian.append(item)
    
    return hasil_pencarian

# Test data
produk_data = [
    {"nama": "Laptop Gaming", "harga": 15000000, "kategori": "Elektronik", "nilai": 9.2},
    {"nama": "Mouse Gaming", "harga": 500000, "kategori": "Aksesoris", "nilai": 8.5},
    {"nama": "Keyboard Mechanical", "harga": 1200000, "kategori": "Aksesoris", "nilai": 8.8},
    {"nama": "Monitor 4K", "harga": 8000000, "kategori": "Elektronik", "nilai": 9.0},
    {"nama": "Headset Gaming", "harga": 800000, "kategori": "Audio", "nilai": 7.5},
]

print("Mencari produk Gaming dengan nilai >= 8.0:")
hasil = cari_dan_filter_data(produk_data, keyword="Gaming", min_value=8.0)
for produk in hasil:
    print(f"- {produk['nama']}: Rp{produk['harga']:,} (Rating: {produk['nilai']})")

# ==================
# TIPS DAN BEST PRACTICES
# ==================
print("\n" + "="*50)
print("TIPS DAN BEST PRACTICES:")
print("="*50)
print("""
1. Gunakan for loop untuk iterasi dengan jumlah yang diketahui
2. Gunakan while loop untuk iterasi berdasarkan kondisi
3. Gunakan enumerate() ketika butuh index dan value
4. Gunakan zip() untuk mengiterasi multiple sequences
5. Gunakan list comprehension untuk kode yang lebih singkat
6. Hati-hati dengan infinite loop pada while
7. Gunakan break dan continue dengan bijak
8. Pertimbangkan generator untuk data yang besar
9. Hindari nested loop yang terlalu dalam
10. Gunakan meaningful variable names dalam loop
""")

# ==================
# PERFORMA COMPARISON
# ==================
print("\n" + "="*50)
print("PERFORMA COMPARISON:")
print("="*50)

import time

def test_performance():
    """
    Membandingkan performa berbagai metode loop
    """
    data = list(range(100000))
    
    # Method 1: Traditional for loop
    start_time = time.time()
    result1 = []
    for i in data:
        if i % 2 == 0:
            result1.append(i * 2)
    time1 = time.time() - start_time
    
    # Method 2: List comprehension
    start_time = time.time()
    result2 = [i * 2 for i in data if i % 2 == 0]
    time2 = time.time() - start_time
    
    # Method 3: Filter + map
    start_time = time.time()
    result3 = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, data)))
    time3 = time.time() - start_time
    
    print(f"Traditional loop: {time1:.6f} seconds")
    print(f"List comprehension: {time2:.6f} seconds")
    print(f"Filter + map: {time3:.6f} seconds")
    print(f"List comprehension adalah {time1/time2:.2f}x lebih cepat")

print("Testing performance (100,000 elements):")
test_performance()

print("\n" + "="*50)
print("LATIHAN:")
print("="*50)
print("""
Coba buat program dengan loops untuk:
1. Menghitung faktorial suatu angka
2. Mencari bilangan prima dalam range tertentu
3. Membalik string tanpa menggunakan [::-1]
4. Membuat pattern segitiga dengan angka
5. Simulasi ATM dengan menu berulang
6. Menghitung frekuensi karakter dalam string
7. Validasi input dengan while loop
8. Game sederhana (rock paper scissors)
""")
