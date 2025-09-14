
# ==================
# 1. BASIC IF STATEMENT
# ==================
print("\n1. BASIC IF STATEMENT")
print("-" * 20)

umur = 18
if umur >= 18:
    print(f"Anda berumur {umur} tahun, Anda sudah dewasa!")

# Contoh dengan input
nama = "Budi"
if nama == "Budi":
    print(f"Halo {nama}, selamat datang!")

# ==================
# 2. IF-ELSE STATEMENT
# ==================
print("\n2. IF-ELSE STATEMENT")
print("-" * 20)

nilai = 75
if nilai >= 70:
    print(f"Nilai {nilai}: LULUS")
else:
    print(f"Nilai {nilai}: TIDAK LULUS")

# Contoh dengan boolean
cuaca_cerah = True
if cuaca_cerah:
    print("Hari ini cerah, cocok untuk jalan-jalan!")
else:
    print("Hari ini mendung, lebih baik di rumah saja.")

# ==================
# 3. IF-ELIF-ELSE STATEMENT
# ==================
print("\n3. IF-ELIF-ELSE STATEMENT")
print("-" * 20)

nilai_siswa = 85

if nilai_siswa >= 90:
    grade = "A"
elif nilai_siswa >= 80:
    grade = "B"
elif nilai_siswa >= 70:
    grade = "C"
elif nilai_siswa >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Nilai: {nilai_siswa}, Grade: {grade}")

# Contoh dengan kategori umur
umur_pengguna = 25

if umur_pengguna < 13:
    kategori = "Anak-anak"
elif umur_pengguna < 20:
    kategori = "Remaja"
elif umur_pengguna < 60:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

print(f"Umur: {umur_pengguna}, Kategori: {kategori}")

# ==================
# 4. OPERATOR PERBANDINGAN
# ==================
print("\n4. OPERATOR PERBANDINGAN")
print("-" * 20)

a = 10
b = 5

print(f"a = {a}, b = {b}")
print(f"a > b: {a > b}")      # Lebih besar
print(f"a < b: {a < b}")      # Lebih kecil
print(f"a >= b: {a >= b}")    # Lebih besar atau sama dengan
print(f"a <= b: {a <= b}")    # Lebih kecil atau sama dengan
print(f"a == b: {a == b}")    # Sama dengan
print(f"a != b: {a != b}")    # Tidak sama dengan

# ==================
# 5. OPERATOR LOGIKA
# ==================
print("\n5. OPERATOR LOGIKA")
print("-" * 20)

# AND - semua kondisi harus True
umur = 20
punya_sim = True

if umur >= 17 and punya_sim:
    print("Boleh mengendarai mobil")
else:
    print("Belum boleh mengendarai mobil")

# OR - salah satu kondisi harus True
cuaca_cerah = False
libur_kerja = True

if cuaca_cerah or libur_kerja:
    print("Bisa pergi berlibur!")
else:
    print("Lebih baik tetap di rumah")

# NOT - membalik kondisi
hujan = True
if not hujan:
    print("Tidak hujan, bisa pergi keluar")
else:
    print("Sedang hujan, lebih baik di dalam")

# ==================
# 6. NESTED CONDITIONS (IF BERSARANG)
# ==================
print("\n6. NESTED CONDITIONS")
print("-" * 20)

umur = 22
punya_ktp = True
punya_pekerjaan = True

if umur >= 17:
    print("Umur memenuhi syarat")
    if punya_ktp:
        print("Memiliki KTP")
        if punya_pekerjaan:
            print("Memiliki pekerjaan")
            print("✓ LOLOS semua persyaratan untuk mengajukan kredit!")
        else:
            print("✗ Belum memiliki pekerjaan")
    else:
        print("✗ Belum memiliki KTP")
else:
    print("✗ Umur belum memenuhi syarat")

# ==================
# 7. MULTIPLE CONDITIONS
# ==================
print("\n7. MULTIPLE CONDITIONS")
print("-" * 20)

suhu = 25
kelembaban = 60
angin = 10

# Menggunakan multiple conditions
if 20 <= suhu <= 30 and kelembaban < 70 and angin < 15:
    print("Cuaca sempurna untuk outdoor activity!")
    print(f"Suhu: {suhu}°C, Kelembaban: {kelembaban}%, Angin: {angin}km/h")
elif suhu > 30:
    print("Terlalu panas untuk aktivitas outdoor")
elif suhu < 20:
    print("Terlalu dingin untuk aktivitas outdoor")
elif kelembaban >= 70:
    print("Terlalu lembab untuk aktivitas outdoor")
else:
    print("Cuaca cukup baik, tapi berhati-hatilah")

# ==================
# 8. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ==================
print("\n8. TERNARY OPERATOR")
print("-" * 20)

# Syntax: nilai_jika_true if kondisi else nilai_jika_false
umur = 16
status = "Dewasa" if umur >= 18 else "Belum Dewasa"
print(f"Umur: {umur}, Status: {status}")

# Contoh dengan fungsi
def cek_genap_ganjil(angka):
    return "Genap" if angka % 2 == 0 else "Ganjil"

angka = 7
print(f"Angka {angka} adalah: {cek_genap_ganjil(angka)}")

# ==================
# 9. MEMBERSHIP OPERATORS (in, not in)
# ==================
print("\n9. MEMBERSHIP OPERATORS")
print("-" * 20)

# Mengecek apakah suatu nilai ada dalam sequence
buah_favorit = ["apel", "jeruk", "pisang", "anggur"]
buah = "jeruk"

if buah in buah_favorit:
    print(f"{buah} adalah salah satu buah favorit saya!")
else:
    print(f"{buah} bukan buah favorit saya")

# Mengecek karakter dalam string
kalimat = "Python adalah bahasa pemrograman yang mudah"
if "Python" in kalimat:
    print("Kalimat ini membahas tentang Python")

# ==================
# 10. IDENTITY OPERATORS (is, is not)
# ==================
print("\n10. IDENTITY OPERATORS")
print("-" * 20)

# is dan is not mengecek apakah objek adalah objek yang sama
x = None
if x is None:
    print("x adalah None")

y = []
z = []
print(f"y is z: {y is z}")  # False, karena objek berbeda
print(f"y == z: {y == z}")  # True, karena nilai sama

# ==================
# 11. CONTOH PRAKTIS: SISTEM LOGIN SEDERHANA
# ==================
print("\n11. CONTOH PRAKTIS: SISTEM LOGIN SEDERHANA")
print("-" * 20)

def sistem_login(username, password, is_admin=False):
    """
    Fungsi untuk mensimulasikan sistem login sederhana
    """
    # Database pengguna sederhana
    users = {
        "admin": {"password": "admin123", "role": "admin"},
        "user1": {"password": "user123", "role": "user"},
        "user2": {"password": "mypass", "role": "user"}
    }
    
    if username in users:
        if users[username]["password"] == password:
            if users[username]["role"] == "admin":
                print(f"✓ Login berhasil! Selamat datang Admin {username}")
                print("Anda memiliki akses penuh ke sistem")
            else:
                print(f"✓ Login berhasil! Selamat datang {username}")
                print("Anda memiliki akses user biasa")
        else:
            print("✗ Password salah!")
    else:
        print("✗ Username tidak ditemukan!")

# Test sistem login
print("Testing sistem login:")
sistem_login("admin", "admin123")
sistem_login("user1", "user123")
sistem_login("user1", "salah")
sistem_login("tidak_ada", "password")

# ==================
# 12. CONTOH PRAKTIS: KALKULATOR SEDERHANA
# ==================
print("\n12. CONTOH PRAKTIS: KALKULATOR SEDERHANA")
print("-" * 20)

def kalkulator(angka1, operator, angka2):
    """
    Fungsi kalkulator sederhana menggunakan conditions
    """
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            return "Error: Tidak bisa membagi dengan nol!"
    elif operator == "**":
        hasil = angka1 ** angka2
    elif operator == "%":
        if angka2 != 0:
            hasil = angka1 % angka2
        else:
            return "Error: Tidak bisa modulo dengan nol!"
    else:
        return "Error: Operator tidak dikenal!"
    
    return f"{angka1} {operator} {angka2} = {hasil}"

# Test kalkulator
print("Testing kalkulator:")
print(kalkulator(10, "+", 5))
print(kalkulator(10, "-", 3))
print(kalkulator(8, "*", 7))
print(kalkulator(15, "/", 3))
print(kalkulator(10, "/", 0))  # Test error handling
print(kalkulator(2, "**", 3))
print(kalkulator(10, "%", 3))

# ==================
# TIPS DAN BEST PRACTICES
# ==================
print("\n" + "="*50)
print("TIPS DAN BEST PRACTICES:")
print("="*50)
print("""
1. Gunakan operator perbandingan yang tepat (==, !=, <, >, <=, >=)
2. Kombinasikan kondisi dengan and, or, not untuk logika yang kompleks
3. Gunakan elif untuk multiple conditions yang berurutan
4. Hindari nested if yang terlalu dalam (maksimal 3-4 level)
5. Gunakan ternary operator untuk kondisi sederhana
6. Selalu pertimbangkan edge cases (nilai None, 0, string kosong)
7. Gunakan parentheses untuk memperjelas prioritas operasi
8. Buat fungsi untuk logika yang kompleks agar kode lebih readable
""")

print("\n" + "="*50)
print("LATIHAN:")
print("="*50)
print("""
Coba buat program dengan conditions untuk:
1. Sistem penilaian mahasiswa (A, B, C, D, E)
2. Penentuan diskon berdasarkan total belanja
3. Validasi input form (nama, email, password)
4. Game sederhana (tebak angka)
5. Konverter suhu dengan multiple pilihan
""")
