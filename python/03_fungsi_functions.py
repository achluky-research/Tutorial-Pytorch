# ===============================================
# TUTORIAL 3: PEMBUATAN DAN PEMANGGILAN FUNGSI
# ===============================================

"""
Fungsi (Functions) adalah blok kode yang dapat digunakan kembali (reusable) 
yang melakukan tugas tertentu. Fungsi membantu kita mengorganisir kode, 
mengurangi duplikasi, dan membuat program lebih modular.

MANFAAT FUNGSI:
- Code reusability (dapat digunakan berulang kali)
- Modularity (memecah program menjadi bagian-bagian kecil)
- Abstraction (menyembunyikan detail implementasi)
- Easy testing dan debugging
- Better code organization

STRUKTUR FUNGSI:
def nama_fungsi(parameter1, parameter2, ...):
    '''Docstring (opsional)'''
    # Body fungsi
    return nilai  # Opsional
"""

print("="*50)
print("TUTORIAL 3: FUNGSI (FUNCTIONS)")
print("="*50)

# ==================
# 1. FUNGSI DASAR TANPA PARAMETER
# ==================
print("\n1. FUNGSI DASAR TANPA PARAMETER")
print("-" * 20)

def sapa():
    """
    Fungsi sederhana untuk menyapa
    """
    print("Halo! Selamat datang di tutorial Python!")

def garis_pemisah():
    """
    Fungsi untuk membuat garis pemisah
    """
    print("-" * 40)

# Memanggil fungsi
print("Memanggil fungsi sapa():")
sapa()
garis_pemisah()

# ==================
# 2. FUNGSI DENGAN PARAMETER
# ==================
print("\n2. FUNGSI DENGAN PARAMETER")
print("-" * 20)

def sapa_nama(nama):
    """
    Fungsi dengan satu parameter
    """
    print(f"Halo {nama}! Selamat datang!")

def perkalian(a, b):
    """
    Fungsi dengan dua parameter
    """
    hasil = a * b
    print(f"{a} x {b} = {hasil}")

def profil_lengkap(nama, umur, kota):
    """
    Fungsi dengan tiga parameter
    """
    print(f"Nama: {nama}")
    print(f"Umur: {umur} tahun")
    print(f"Kota: {kota}")

# Memanggil fungsi dengan parameter
print("Fungsi dengan parameter:")
sapa_nama("Budi")
perkalian(5, 8)
print("\nProfil:")
profil_lengkap("Siti", 25, "Jakarta")

# ==================
# 3. FUNGSI DENGAN RETURN VALUE
# ==================
print("\n3. FUNGSI DENGAN RETURN VALUE")
print("-" * 20)

def tambah(a, b):
    """
    Fungsi yang mengembalikan hasil penjumlahan
    """
    return a + b

def luas_lingkaran(radius):
    """
    Fungsi untuk menghitung luas lingkaran
    """
    pi = 3.14159
    return pi * radius * radius

def cek_ganjil_genap(angka):
    """
    Fungsi yang mengembalikan string
    """
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"

def faktorial(n):
    """
    Fungsi untuk menghitung faktorial
    """
    if n == 0 or n == 1:
        return 1
    else:
        hasil = 1
        for i in range(2, n + 1):
            hasil *= i
        return hasil

# Menggunakan fungsi yang mengembalikan nilai
print("Fungsi dengan return value:")
hasil_tambah = tambah(10, 20)
print(f"10 + 20 = {hasil_tambah}")

luas = luas_lingkaran(7)
print(f"Luas lingkaran dengan radius 7: {luas:.2f}")

print(f"Angka 15 adalah: {cek_ganjil_genap(15)}")
print(f"Angka 20 adalah: {cek_ganjil_genap(20)}")

print(f"Faktorial 5 = {faktorial(5)}")

# ==================
# 4. PARAMETER DEFAULT
# ==================
print("\n4. PARAMETER DEFAULT")
print("-" * 20)

def sapa_dengan_sapaan(nama, sapaan="Halo"):
    """
    Fungsi dengan parameter default
    """
    print(f"{sapaan} {nama}!")

def hitung_pangkat(base, pangkat=2):
    """
    Fungsi dengan parameter default untuk pangkat
    """
    return base ** pangkat

def buat_profil(nama, umur, kota="Jakarta", pekerjaan="Belum diisi"):
    """
    Fungsi dengan multiple parameter default
    """
    return {
        "nama": nama,
        "umur": umur,
        "kota": kota,
        "pekerjaan": pekerjaan
    }

# Menggunakan parameter default
print("Parameter default:")
sapa_dengan_sapaan("Ali")  # Menggunakan default "Halo"
sapa_dengan_sapaan("Sari", "Selamat pagi")  # Override default

print(f"5^2 = {hitung_pangkat(5)}")  # Default pangkat=2
print(f"2^5 = {hitung_pangkat(2, 5)}")  # Override pangkat

profil1 = buat_profil("Budi", 30)
profil2 = buat_profil("Ani", 25, "Surabaya", "Engineer")
print("Profil 1:", profil1)
print("Profil 2:", profil2)

# ==================
# 5. KEYWORD ARGUMENTS
# ==================
print("\n5. KEYWORD ARGUMENTS")
print("-" * 20)

def info_mahasiswa(nama, nim, jurusan, ipk):
    """
    Fungsi untuk menampilkan info mahasiswa
    """
    print(f"Nama: {nama}")
    print(f"NIM: {nim}")
    print(f"Jurusan: {jurusan}")
    print(f"IPK: {ipk}")
    print()

# Memanggil dengan keyword arguments (bisa tidak berurutan)
print("Keyword arguments:")
info_mahasiswa(jurusan="Informatika", nama="John", ipk=3.8, nim="2021001")
info_mahasiswa("Jane", nim="2021002", jurusan="Sistem Informasi", ipk=3.9)

# ==================
# 6. *ARGS DAN **KWARGS
# ==================
print("\n6. *ARGS DAN **KWARGS")
print("-" * 20)

def jumlah_semua(*args):
    """
    Fungsi yang menerima jumlah argumen yang tidak terbatas
    """
    total = 0
    for angka in args:
        total += angka
    return total

def cetak_info(**kwargs):
    """
    Fungsi yang menerima keyword arguments yang tidak terbatas
    """
    print("Informasi yang diterima:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

def fungsi_lengkap(nama, *hobi, **info):
    """
    Fungsi yang mengkombinasikan parameter biasa, *args, dan **kwargs
    """
    print(f"Nama: {nama}")
    
    if hobi:
        print("Hobi:")
        for i, h in enumerate(hobi, 1):
            print(f"  {i}. {h}")
    
    if info:
        print("Info tambahan:")
        for key, value in info.items():
            print(f"  {key}: {value}")

# Menggunakan *args dan **kwargs
print("Menggunakan *args:")
print(f"Jumlah: {jumlah_semua(1, 2, 3, 4, 5)}")
print(f"Jumlah: {jumlah_semua(10, 20)}")

print("\nMenggunakan **kwargs:")
cetak_info(nama="Ali", umur=25, kota="Bandung")

print("\nKombinasi semua:")
fungsi_lengkap("Budi", "Membaca", "Coding", "Gaming", umur=28, kota="Yogya")

# ==================
# 7. LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ==================
print("\n7. LAMBDA FUNCTIONS")
print("-" * 20)

# Lambda dasar
kuadrat = lambda x: x ** 2
penjumlahan = lambda a, b: a + b

print("Lambda functions:")
print(f"Kuadrat 5: {kuadrat(5)}")
print(f"Penjumlahan 3 + 7: {penjumlahan(3, 7)}")

# Lambda dengan built-in functions
angka_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Menggunakan map()
kuadrat_list = list(map(lambda x: x**2, angka_list))
print(f"Kuadrat dari {angka_list[:5]}: {kuadrat_list[:5]}")

# Menggunakan filter()
genap_list = list(filter(lambda x: x % 2 == 0, angka_list))
print(f"Angka genap: {genap_list}")

# Menggunakan sorted()
mahasiswa_list = [("Ali", 85), ("Budi", 92), ("Citra", 78), ("Dina", 96)]
sorted_by_nama = sorted(mahasiswa_list, key=lambda x: x[0])
sorted_by_nilai = sorted(mahasiswa_list, key=lambda x: x[1], reverse=True)

print(f"Sorted by nama: {sorted_by_nama}")
print(f"Sorted by nilai: {sorted_by_nilai}")

# ==================
# 8. NESTED FUNCTIONS
# ==================
print("\n8. NESTED FUNCTIONS")
print("-" * 20)

def kalkulator_lanjut(operasi):
    """
    Fungsi yang memiliki nested functions
    """
    def tambah(a, b):
        return a + b
    
    def kurang(a, b):
        return a - b
    
    def kali(a, b):
        return a * b
    
    def bagi(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian dengan nol!"
    
    # Dictionary untuk mapping operasi ke fungsi
    operations = {
        "+": tambah,
        "-": kurang,
        "*": kali,
        "/": bagi
    }
    
    return operations.get(operasi, None)

# Menggunakan nested functions
print("Nested functions:")
plus_func = kalkulator_lanjut("+")
minus_func = kalkulator_lanjut("-")

print(f"15 + 25 = {plus_func(15, 25)}")
print(f"30 - 12 = {minus_func(30, 12)}")

# ==================
# 9. CLOSURES
# ==================
print("\n9. CLOSURES")
print("-" * 20)

def pembuat_pengali(faktor):
    """
    Closure - inner function mengakses variable dari outer function
    """
    def pengali(angka):
        return angka * faktor
    return pengali

def counter():
    """
    Closure untuk membuat counter
    """
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

# Menggunakan closures
print("Closures:")
kali_2 = pembuat_pengali(2)
kali_5 = pembuat_pengali(5)

print(f"5 x 2 = {kali_2(5)}")
print(f"7 x 5 = {kali_5(7)}")

# Counter closure
counter1 = counter()
counter2 = counter()

print(f"Counter1: {counter1()}")  # 1
print(f"Counter1: {counter1()}")  # 2
print(f"Counter2: {counter2()}")  # 1 (independent)
print(f"Counter1: {counter1()}")  # 3

# ==================
# 10. DECORATORS
# ==================
print("\n10. DECORATORS")
print("-" * 20)

def timing_decorator(func):
    """
    Decorator untuk mengukur waktu eksekusi fungsi
    """
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        hasil = func(*args, **kwargs)
        end = time.time()
        print(f"Fungsi {func.__name__} selesai dalam {end - start:.6f} detik")
        return hasil
    return wrapper

def log_decorator(func):
    """
    Decorator untuk logging
    """
    def wrapper(*args, **kwargs):
        print(f"Memanggil fungsi: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        hasil = func(*args, **kwargs)
        print(f"Hasil: {hasil}")
        return hasil
    return wrapper

# Menggunakan decorator dengan @ syntax
@timing_decorator
def hitung_fibonacci(n):
    """
    Fungsi untuk menghitung fibonacci dengan decorator
    """
    if n <= 1:
        return n
    else:
        return hitung_fibonacci(n-1) + hitung_fibonacci(n-2)

@log_decorator
def kali_dua(angka):
    """
    Fungsi sederhana dengan log decorator
    """
    return angka * 2

# Multiple decorators
@log_decorator
@timing_decorator
def operasi_kompleks(a, b):
    """
    Fungsi dengan multiple decorators
    """
    import time
    time.sleep(0.1)  # Simulasi operasi yang memakan waktu
    return a ** b

print("Decorators:")
print(f"Fibonacci ke-10: {hitung_fibonacci(10)}")
print()

kali_dua(15)
print()

operasi_kompleks(2, 10)

# ==================
# 11. GENERATOR FUNCTIONS
# ==================
print("\n11. GENERATOR FUNCTIONS")
print("-" * 20)

def countdown_generator(start):
    """
    Generator function untuk countdown
    """
    while start > 0:
        yield start
        start -= 1
    yield "Selesai!"

def fibonacci_generator():
    """
    Generator untuk deret fibonacci tanpa batas
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def range_genap(start, end):
    """
    Generator untuk angka genap dalam range
    """
    current = start if start % 2 == 0 else start + 1
    while current < end:
        yield current
        current += 2

print("Generator functions:")

# Countdown generator
print("Countdown dari 5:")
countdown = countdown_generator(5)
for nilai in countdown:
    print(nilai)

print("\nFibonacci 10 angka pertama:")
fib_gen = fibonacci_generator()
fib_list = [next(fib_gen) for _ in range(10)]
print(fib_list)

print("\nAngka genap dari 1 sampai 20:")
for angka in range_genap(1, 20):
    print(angka, end=" ")
print()

# ==================
# 12. FUNGSI REKURSIF
# ==================
print("\n12. FUNGSI REKURSIF")
print("-" * 20)

def faktorial_rekursif(n):
    """
    Menghitung faktorial menggunakan rekursi
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial_rekursif(n - 1)

def fibonacci_rekursif(n):
    """
    Menghitung fibonacci menggunakan rekursi
    """
    if n <= 1:
        return n
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)

def gcd_rekursif(a, b):
    """
    Mencari Greatest Common Divisor menggunakan rekursi
    """
    if b == 0:
        return a
    else:
        return gcd_rekursif(b, a % b)

def palindrome_check(text):
    """
    Mengecek palindrome menggunakan rekursi
    """
    # Bersihkan string dari spasi dan ubah ke lowercase
    text = text.replace(" ", "").lower()
    
    # Base case
    if len(text) <= 1:
        return True
    
    # Recursive case
    if text[0] == text[-1]:
        return palindrome_check(text[1:-1])
    else:
        return False

print("Fungsi rekursif:")
print(f"Faktorial 6: {faktorial_rekursif(6)}")
print(f"Fibonacci ke-8: {fibonacci_rekursif(8)}")
print(f"GCD(48, 18): {gcd_rekursif(48, 18)}")
print(f"'radar' palindrome: {palindrome_check('radar')}")
print(f"'level' palindrome: {palindrome_check('level')}")
print(f"'hello' palindrome: {palindrome_check('hello')}")

# ==================
# 13. HIGHER ORDER FUNCTIONS
# ==================
print("\n13. HIGHER ORDER FUNCTIONS")
print("-" * 20)

def apply_operation(func, numbers):
    """
    Higher order function yang menerima function sebagai parameter
    """
    return [func(x) for x in numbers]

def create_multiplier(factor):
    """
    Function yang mengembalikan function
    """
    return lambda x: x * factor

def filter_and_transform(data, filter_func, transform_func):
    """
    HOF yang melakukan filtering dan transformasi
    """
    filtered = filter(filter_func, data)
    transformed = map(transform_func, filtered)
    return list(transformed)

# Menggunakan higher order functions
print("Higher Order Functions:")
numbers = [1, 2, 3, 4, 5]

# Apply different operations
squared = apply_operation(lambda x: x**2, numbers)
doubled = apply_operation(lambda x: x*2, numbers)

print(f"Original: {numbers}")
print(f"Squared: {squared}")
print(f"Doubled: {doubled}")

# Create multiplier
multiply_by_3 = create_multiplier(3)
print(f"5 x 3 = {multiply_by_3(5)}")

# Filter and transform
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_and_transform(
    data,
    lambda x: x % 2 == 0,  # Filter genap
    lambda x: x ** 2       # Kuadratkan
)
print(f"Genap dikuadratkan: {result}")

# ==================
# 14. CONTOH PRAKTIS: SISTEM VALIDASI
# ==================
print("\n14. CONTOH PRAKTIS: SISTEM VALIDASI")
print("-" * 20)

def validate_email(email):
    """
    Validasi sederhana untuk email
    """
    return "@" in email and "." in email.split("@")[-1]

def validate_password(password, min_length=8):
    """
    Validasi password
    """
    if len(password) < min_length:
        return False, f"Password minimal {min_length} karakter"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if not has_upper:
        return False, "Password harus mengandung huruf besar"
    if not has_lower:
        return False, "Password harus mengandung huruf kecil"
    if not has_digit:
        return False, "Password harus mengandung angka"
    
    return True, "Password valid"

def validate_phone(phone):
    """
    Validasi nomor telepon Indonesia
    """
    # Hapus spasi dan tanda hubung
    clean_phone = phone.replace(" ", "").replace("-", "")
    
    # Cek format Indonesia
    if clean_phone.startswith("08") and len(clean_phone) >= 10:
        return True
    elif clean_phone.startswith("+62") and len(clean_phone) >= 12:
        return True
    else:
        return False

def validate_form(data, validators):
    """
    Fungsi untuk memvalidasi form dengan berbagai validator
    """
    errors = {}
    
    for field, value in data.items():
        if field in validators:
            validator = validators[field]
            if not validator(value):
                errors[field] = f"Validasi gagal untuk {field}"
    
    return len(errors) == 0, errors

# Test sistem validasi
print("Sistem Validasi:")

# Test individual validators
print("Test Email:")
emails = ["test@example.com", "invalid-email", "user@domain.co.id"]
for email in emails:
    valid = validate_email(email)
    print(f"  {email}: {'Valid' if valid else 'Invalid'}")

print("\nTest Password:")
passwords = ["weak", "StrongPass123", "NoDigits"]
for pwd in passwords:
    valid, message = validate_password(pwd)
    print(f"  '{pwd}': {message}")

print("\nTest Phone:")
phones = ["081234567890", "+6281234567890", "123456"]
for phone in phones:
    valid = validate_phone(phone)
    print(f"  {phone}: {'Valid' if valid else 'Invalid'}")

# Test form validation
form_data = {
    "email": "user@example.com",
    "password": "StrongPass123",
    "phone": "081234567890"
}

form_validators = {
    "email": validate_email,
    "password": lambda p: validate_password(p)[0],
    "phone": validate_phone
}

is_valid, errors = validate_form(form_data, form_validators)
print(f"\nValidasi Form: {'Berhasil' if is_valid else 'Gagal'}")
if errors:
    for field, error in errors.items():
        print(f"  {error}")

# ==================
# 15. CONTOH PRAKTIS: KALKULATOR SCIENTIFIC
# ==================
print("\n15. CONTOH PRAKTIS: KALKULATOR SCIENTIFIC")
print("-" * 20)

import math

def basic_operations():
    """
    Mengembalikan dictionary dengan operasi dasar
    """
    return {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "multiply": lambda a, b: a * b,
        "divide": lambda a, b: a / b if b != 0 else "Error: Division by zero",
        "power": lambda a, b: a ** b,
        "modulo": lambda a, b: a % b if b != 0 else "Error: Modulo by zero"
    }

def scientific_operations():
    """
    Mengembalikan dictionary dengan operasi scientific
    """
    return {
        "sqrt": lambda x: math.sqrt(x) if x >= 0 else "Error: Negative number",
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "log": lambda x: math.log10(x) if x > 0 else "Error: Invalid input",
        "ln": lambda x: math.log(x) if x > 0 else "Error: Invalid input",
        "factorial": lambda x: math.factorial(int(x)) if x >= 0 and x == int(x) else "Error: Invalid input"
    }

def calculate(operation, *args):
    """
    Fungsi utama kalkulator
    """
    all_ops = {**basic_operations(), **scientific_operations()}
    
    if operation not in all_ops:
        return f"Error: Operation '{operation}' not found"
    
    try:
        return all_ops[operation](*args)
    except Exception as e:
        return f"Error: {str(e)}"

# Test kalkulator scientific
print("Kalkulator Scientific:")

# Test operasi dasar
print("Operasi Dasar:")
print(f"10 + 5 = {calculate('add', 10, 5)}")
print(f"10 - 3 = {calculate('subtract', 10, 3)}")
print(f"4 * 7 = {calculate('multiply', 4, 7)}")
print(f"15 / 3 = {calculate('divide', 15, 3)}")
print(f"2^8 = {calculate('power', 2, 8)}")

print("\nOperasi Scientific:")
print(f"√16 = {calculate('sqrt', 16)}")
print(f"sin(30°) = {calculate('sin', 30):.4f}")
print(f"cos(60°) = {calculate('cos', 60):.4f}")
print(f"log(100) = {calculate('log', 100)}")
print(f"5! = {calculate('factorial', 5)}")

# ==================
# TIPS DAN BEST PRACTICES
# ==================
print("\n" + "="*50)
print("TIPS DAN BEST PRACTICES:")
print("="*50)
print("""
1. Gunakan docstring untuk mendokumentasikan fungsi
2. Berikan nama fungsi yang deskriptif dan meaningful
3. Fungsi sebaiknya melakukan satu tugas saja (Single Responsibility)
4. Gunakan type hints untuk parameter dan return value
5. Hindari side effects dalam fungsi (pure functions)
6. Gunakan default parameters dengan bijak
7. Validasi input parameter jika diperlukan
8. Return consistent data types
9. Gunakan lambda untuk fungsi sederhana one-liner
10. Pertimbangkan performance untuk recursive functions
11. Gunakan generators untuk data yang besar
12. Manfaatkan decorators untuk cross-cutting concerns
""")

# ==================
# TYPE HINTS EXAMPLE
# ==================
print("\n" + "="*50)
print("TYPE HINTS EXAMPLE:")
print("="*50)

def hitung_rata_rata(numbers: list[float]) -> float:
    """
    Menghitung rata-rata dari list angka
    
    Args:
        numbers (list[float]): List berisi angka-angka
        
    Returns:
        float: Nilai rata-rata
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def format_nama(first_name: str, last_name: str, middle_name: str = "") -> str:
    """
    Format nama lengkap
    
    Args:
        first_name (str): Nama depan
        last_name (str): Nama belakang  
        middle_name (str, optional): Nama tengah. Defaults to "".
        
    Returns:
        str: Nama yang sudah diformat
    """
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

# Test type hints
nilai_list = [85.5, 90.0, 78.5, 92.0, 88.5]
rata_rata = hitung_rata_rata(nilai_list)
print(f"Rata-rata nilai: {rata_rata:.2f}")

nama_lengkap = format_nama("John", "Doe", "Smith")
print(f"Nama lengkap: {nama_lengkap}")

print("\n" + "="*50)
print("LATIHAN:")
print("="*50)
print("""
Coba buat fungsi untuk:
1. Konverter suhu (Celsius, Fahrenheit, Kelvin)
2. Validasi dan parsing tanggal
3. Generator bilangan prima
4. Sistem scoring dengan berbagai metode
5. Text analyzer (word count, character frequency)
6. Simple encryption/decryption
7. Data structure operations (stack, queue)
8. Mathematical series calculations
9. File operations wrapper functions
10. API response formatter functions
""")
