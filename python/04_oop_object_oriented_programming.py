# ===============================================
# TUTORIAL 4: OBJECT-ORIENTED PROGRAMMING (OOP)
# ===============================================

"""
Object-Oriented Programming (OOP) adalah paradigma pemrograman yang menggunakan
"objek" untuk mendesain aplikasi. OOP memungkinkan kita untuk mengorganisir
kode dengan cara yang lebih natural dan modular.

PRINSIP UTAMA OOP:
1. Encapsulation - Menyembunyikan detail implementasi
2. Inheritance - Pewarisan sifat dari class lain
3. Polymorphism - Kemampuan objek untuk mengambil berbagai bentuk
4. Abstraction - Menyederhanakan kompleksitas

KEUNTUNGAN OOP:
- Code reusability
- Modularity dan organization
- Easy maintenance
- Real-world modeling
- Data security
"""

print("="*60)
print("TUTORIAL 4: OBJECT-ORIENTED PROGRAMMING (OOP)")
print("="*60)

# ==================
# 1. CLASS DAN OBJECT DASAR
# ==================
print("\n1. CLASS DAN OBJECT DASAR")
print("-" * 30)

class Mobil:
    """
    Class sederhana untuk merepresentasikan mobil
    """
    
    def __init__(self, merk, model, tahun):
        """
        Constructor - method yang dipanggil saat object dibuat
        """
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.kecepatan = 0
        self.mesin_hidup = False
    
    def info(self):
        """
        Method untuk menampilkan informasi mobil
        """
        return f"{self.merk} {self.model} ({self.tahun})"
    
    def nyalakan_mesin(self):
        """
        Method untuk menyalakan mesin
        """
        self.mesin_hidup = True
        return "Mesin dinyalakan!"
    
    def matikan_mesin(self):
        """
        Method untuk mematikan mesin
        """
        self.mesin_hidup = False
        self.kecepatan = 0
        return "Mesin dimatikan!"
    
    def gas(self, kecepatan_tambah):
        """
        Method untuk menambah kecepatan
        """
        if self.mesin_hidup:
            self.kecepatan += kecepatan_tambah
            return f"Kecepatan sekarang: {self.kecepatan} km/h"
        else:
            return "Nyalakan mesin terlebih dahulu!"

# Membuat object (instance) dari class
print("Membuat objects dari class Mobil:")
mobil1 = Mobil("Toyota", "Avanza", 2020)
mobil2 = Mobil("Honda", "Civic", 2019)

print(f"Mobil 1: {mobil1.info()}")
print(f"Mobil 2: {mobil2.info()}")

# Menggunakan method
print(f"\n{mobil1.nyalakan_mesin()}")
print(f"{mobil1.gas(50)}")
print(f"{mobil1.gas(20)}")
print(f"{mobil1.matikan_mesin()}")

# ==================
# 2. ATTRIBUTES DAN METHODS
# ==================
print("\n2. ATTRIBUTES DAN METHODS")
print("-" * 30)

class Mahasiswa:
    """
    Class untuk merepresentasikan mahasiswa dengan berbagai jenis attributes
    """
    
    # Class attribute - shared oleh semua instance
    universitas = "Universitas Indonesia"
    jumlah_mahasiswa = 0
    
    def __init__(self, nama, nim, jurusan):
        # Instance attributes - unik untuk setiap instance
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = []
        
        # Increment class attribute
        Mahasiswa.jumlah_mahasiswa += 1
    
    def tambah_nilai(self, nilai):
        """Instance method untuk menambah nilai"""
        self.nilai.append(nilai)
    
    def hitung_ipk(self):
        """Instance method untuk menghitung IPK"""
        if not self.nilai:
            return 0.0
        return sum(self.nilai) / len(self.nilai)
    
    def info_lengkap(self):
        """Instance method untuk info lengkap"""
        return f"""
        Nama: {self.nama}
        NIM: {self.nim}
        Jurusan: {self.jurusan}
        Universitas: {self.universitas}
        IPK: {self.hitung_ipk():.2f}
        """
    
    @classmethod
    def dari_string(cls, mahasiswa_str):
        """
        Class method - alternative constructor
        """
        nama, nim, jurusan = mahasiswa_str.split('-')
        return cls(nama, nim, jurusan)
    
    @staticmethod
    def validasi_nim(nim):
        """
        Static method - tidak memerlukan instance atau class
        """
        return len(nim) == 10 and nim.isdigit()
    
    def __str__(self):
        """
        Magic method untuk representasi string
        """
        return f"Mahasiswa({self.nama}, {self.nim})"
    
    def __repr__(self):
        """
        Magic method untuk representasi developer
        """
        return f"Mahasiswa('{self.nama}', '{self.nim}', '{self.jurusan}')"

# Test class Mahasiswa
print("Testing class Mahasiswa:")
mhs1 = Mahasiswa("Ali Rahman", "2021001234", "Informatika")
mhs2 = Mahasiswa("Sari Dewi", "2021005678", "Sistem Informasi")

# Menambah nilai
mhs1.tambah_nilai(3.5)
mhs1.tambah_nilai(3.8)
mhs1.tambah_nilai(3.7)

mhs2.tambah_nilai(3.9)
mhs2.tambah_nilai(3.6)

print(f"Jumlah mahasiswa: {Mahasiswa.jumlah_mahasiswa}")
print(f"IPK {mhs1.nama}: {mhs1.hitung_ipk():.2f}")
print(f"IPK {mhs2.nama}: {mhs2.hitung_ipk():.2f}")

# Class method
mhs3 = Mahasiswa.dari_string("Budi Santoso-2021009999-Teknik Elektro")
print(f"Mahasiswa dari string: {mhs3}")

# Static method
print(f"NIM valid: {Mahasiswa.validasi_nim('2021001234')}")
print(f"NIM tidak valid: {Mahasiswa.validasi_nim('123')}")

# ==================
# 3. ENCAPSULATION (PRIVATE ATTRIBUTES/METHODS)
# ==================
print("\n3. ENCAPSULATION")
print("-" * 30)

class RekeningBank:
    """
    Class yang mendemonstrasikan encapsulation
    """
    
    def __init__(self, nomor_rekening, nama_pemilik, saldo_awal=0):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self.__saldo = saldo_awal  # Private attribute
        self.__pin = "1234"        # Private attribute
        self._riwayat = []         # Protected attribute
    
    def info_rekening(self):
        """Public method"""
        return f"Rekening: {self.nomor_rekening}, Pemilik: {self.nama_pemilik}"
    
    def cek_saldo(self, pin):
        """Method untuk cek saldo dengan validasi PIN"""
        if self.__validasi_pin(pin):
            return f"Saldo Anda: Rp{self.__saldo:,}"
        else:
            return "PIN salah!"
    
    def setor(self, jumlah, pin):
        """Method untuk setor uang"""
        if self.__validasi_pin(pin):
            if jumlah > 0:
                self.__saldo += jumlah
                self._tambah_riwayat(f"Setor: +Rp{jumlah:,}")
                return f"Setor berhasil! Saldo: Rp{self.__saldo:,}"
            else:
                return "Jumlah setor harus positif!"
        else:
            return "PIN salah!"
    
    def tarik(self, jumlah, pin):
        """Method untuk tarik uang"""
        if self.__validasi_pin(pin):
            if jumlah > 0:
                if jumlah <= self.__saldo:
                    self.__saldo -= jumlah
                    self._tambah_riwayat(f"Tarik: -Rp{jumlah:,}")
                    return f"Tarik berhasil! Saldo: Rp{self.__saldo:,}"
                else:
                    return "Saldo tidak mencukupi!"
            else:
                return "Jumlah tarik harus positif!"
        else:
            return "PIN salah!"
    
    def ubah_pin(self, pin_lama, pin_baru):
        """Method untuk ubah PIN"""
        if self.__validasi_pin(pin_lama):
            self.__pin = pin_baru
            return "PIN berhasil diubah!"
        else:
            return "PIN lama salah!"
    
    def __validasi_pin(self, pin):
        """Private method untuk validasi PIN"""
        return pin == self.__pin
    
    def _tambah_riwayat(self, transaksi):
        """Protected method untuk menambah riwayat"""
        from datetime import datetime
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._riwayat.append(f"{waktu}: {transaksi}")
    
    def riwayat_transaksi(self, pin):
        """Method untuk melihat riwayat transaksi"""
        if self.__validasi_pin(pin):
            if self._riwayat:
                return "\n".join(self._riwayat[-5:])  # 5 transaksi terakhir
            else:
                return "Belum ada transaksi"
        else:
            return "PIN salah!"

# Test encapsulation
print("Testing Encapsulation:")
rekening = RekeningBank("1234567890", "John Doe", 1000000)

print(rekening.info_rekening())
print(rekening.cek_saldo("1234"))
print(rekening.setor(500000, "1234"))
print(rekening.tarik(200000, "1234"))
print(rekening.tarik(2000000, "1234"))  # Saldo tidak cukup
print(rekening.cek_saldo("1234"))

# Coba akses private attribute (tidak disarankan)
print(f"\nAkses langsung private attribute: {rekening._RekeningBank__saldo}")

# ==================
# 4. INHERITANCE (PEWARISAN)
# ==================
print("\n4. INHERITANCE")
print("-" * 30)

class Kendaraan:
    """
    Parent class untuk semua kendaraan
    """
    
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.kecepatan = 0
    
    def info(self):
        return f"{self.merk} {self.model} ({self.tahun})"
    
    def gas(self, tambah_kecepatan):
        self.kecepatan += tambah_kecepatan
        return f"Kecepatan: {self.kecepatan} km/h"
    
    def rem(self, kurang_kecepatan):
        self.kecepatan = max(0, self.kecepatan - kurang_kecepatan)
        return f"Kecepatan: {self.kecepatan} km/h"

class Mobil(Kendaraan):
    """
    Child class yang inherit dari Kendaraan
    """
    
    def __init__(self, merk, model, tahun, jumlah_pintu):
        super().__init__(merk, model, tahun)  # Panggil constructor parent
        self.jumlah_pintu = jumlah_pintu
        self.ac_hidup = False
    
    def info(self):
        # Override method parent
        return f"{super().info()} - {self.jumlah_pintu} pintu"
    
    def nyalakan_ac(self):
        self.ac_hidup = True
        return "AC dinyalakan"
    
    def matikan_ac(self):
        self.ac_hidup = False
        return "AC dimatikan"

class Motor(Kendaraan):
    """
    Child class lain dari Kendaraan
    """
    
    def __init__(self, merk, model, tahun, cc):
        super().__init__(merk, model, tahun)
        self.cc = cc
        self.standar_samping = True
    
    def info(self):
        return f"{super().info()} - {self.cc}cc"
    
    def angkat_standar(self):
        self.standar_samping = False
        return "Standar samping diangkat"
    
    def turunkan_standar(self):
        self.standar_samping = True
        return "Standar samping diturunkan"

class Truk(Kendaraan):
    """
    Child class untuk truk
    """
    
    def __init__(self, merk, model, tahun, kapasitas_muat):
        super().__init__(merk, model, tahun)
        self.kapasitas_muat = kapasitas_muat
        self.muatan = 0
    
    def info(self):
        return f"{super().info()} - Kapasitas: {self.kapasitas_muat} ton"
    
    def muat_barang(self, berat):
        if self.muatan + berat <= self.kapasitas_muat:
            self.muatan += berat
            return f"Berhasil memuat {berat} ton. Total muatan: {self.muatan} ton"
        else:
            return "Kapasitas muat terlampaui!"
    
    def bongkar_barang(self, berat):
        if berat <= self.muatan:
            self.muatan -= berat
            return f"Berhasil bongkar {berat} ton. Sisa muatan: {self.muatan} ton"
        else:
            return "Tidak cukup barang untuk dibongkar!"

# Test inheritance
print("Testing Inheritance:")
mobil = Mobil("Toyota", "Camry", 2022, 4)
motor = Motor("Honda", "CBR", 2021, 250)
truk = Truk("Mitsubishi", "Fuso", 2020, 10)

print(f"Mobil: {mobil.info()}")
print(f"Motor: {motor.info()}")
print(f"Truk: {truk.info()}")

print(f"\n{mobil.gas(60)}")
print(f"{mobil.nyalakan_ac()}")

print(f"\n{motor.gas(80)}")
print(f"{motor.angkat_standar()}")

print(f"\n{truk.gas(40)}")
print(f"{truk.muat_barang(8)}")
print(f"{truk.muat_barang(3)}")  # Akan gagal

# ==================
# 5. MULTIPLE INHERITANCE
# ==================
print("\n5. MULTIPLE INHERITANCE")
print("-" * 30)

class Terbang:
    """
    Mixin class untuk kemampuan terbang
    """
    
    def __init__(self):
        self.ketinggian = 0
    
    def lepas_landas(self):
        self.ketinggian = 100
        return "Lepas landas!"
    
    def terbang_tinggi(self, tambah_tinggi):
        self.ketinggian += tambah_tinggi
        return f"Ketinggian: {self.ketinggian} meter"
    
    def mendarat(self):
        self.ketinggian = 0
        return "Mendarat!"

class Berenang:
    """
    Mixin class untuk kemampuan berenang
    """
    
    def __init__(self):
        self.kedalaman = 0
    
    def menyelam(self, kedalaman):
        self.kedalaman = kedalaman
        return f"Menyelam pada kedalaman {self.kedalaman} meter"
    
    def naik_ke_permukaan(self):
        self.kedalaman = 0
        return "Kembali ke permukaan"

class Bebek(Terbang, Berenang):
    """
    Class yang inherit dari multiple parents
    """
    
    def __init__(self, nama):
        self.nama = nama
        Terbang.__init__(self)
        Berenang.__init__(self)
    
    def suara(self):
        return "Kwek kwek!"
    
    def info(self):
        return f"Bebek {self.nama} - Tinggi: {self.ketinggian}m, Kedalaman: {self.kedalaman}m"

# Test multiple inheritance
print("Testing Multiple Inheritance:")
bebek = Bebek("Donald")
print(bebek.info())
print(bebek.suara())
print(bebek.lepas_landas())
print(bebek.terbang_tinggi(50))
print(bebek.mendarat())
print(bebek.menyelam(5))
print(bebek.naik_ke_permukaan())

# ==================
# 6. POLYMORPHISM
# ==================
print("\n6. POLYMORPHISM")
print("-" * 30)

class Hewan:
    """
    Base class untuk demonstrasi polymorphism
    """
    
    def __init__(self, nama):
        self.nama = nama
    
    def suara(self):
        return "Hewan membuat suara"
    
    def info(self):
        return f"Ini adalah {self.nama}"

class Anjing(Hewan):
    def suara(self):
        return "Guk guk!"

class Kucing(Hewan):
    def suara(self):
        return "Meow!"

class Sapi(Hewan):
    def suara(self):
        return "Moo!"

class Ayam(Hewan):
    def suara(self):
        return "Petok petok!"

def buat_suara(hewan):
    """
    Fungsi yang mendemonstrasikan polymorphism
    """
    print(f"{hewan.info()}: {hewan.suara()}")

# Test polymorphism
print("Testing Polymorphism:")
hewan_list = [
    Anjing("Buddy"),
    Kucing("Whiskers"),
    Sapi("Moo-dy"),
    Ayam("Clucky")
]

for hewan in hewan_list:
    buat_suara(hewan)

# ==================
# 7. ABSTRACT BASE CLASS
# ==================
print("\n7. ABSTRACT BASE CLASS")
print("-" * 30)

from abc import ABC, abstractmethod

class Bentuk(ABC):
    """
    Abstract base class untuk bentuk geometri
    """
    
    @abstractmethod
    def luas(self):
        pass
    
    @abstractmethod
    def keliling(self):
        pass
    
    def info(self):
        return f"Ini adalah {self.__class__.__name__}"

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi ** 2
    
    def keliling(self):
        return 4 * self.sisi

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
        self.pi = 3.14159
    
    def luas(self):
        return self.pi * self.jari_jari ** 2
    
    def keliling(self):
        return 2 * self.pi * self.jari_jari

class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        return self.panjang * self.lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

# Test abstract class
print("Testing Abstract Base Class:")
bentuk_list = [
    Persegi(5),
    Lingkaran(3),
    PersegiPanjang(4, 6)
]

for bentuk in bentuk_list:
    print(f"{bentuk.info()}")
    print(f"  Luas: {bentuk.luas():.2f}")
    print(f"  Keliling: {bentuk.keliling():.2f}")
    print()

# ==================
# 8. PROPERTY DECORATORS
# ==================
print("\n8. PROPERTY DECORATORS")
print("-" * 30)

class Termometer:
    """
    Class yang mendemonstrasikan penggunaan property decorators
    """
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter untuk celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter untuk celsius dengan validasi"""
        if value < -273.15:
            raise ValueError("Suhu tidak bisa lebih rendah dari absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property untuk fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter untuk fahrenheit yang mengupdate celsius"""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Computed property untuk kelvin"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Setter untuk kelvin yang mengupdate celsius"""
        self.celsius = value - 273.15
    
    def info(self):
        return f"Suhu: {self.celsius:.1f}°C / {self.fahrenheit:.1f}°F / {self.kelvin:.1f}K"

# Test property decorators
print("Testing Property Decorators:")
termo = Termometer(25)
print(termo.info())

# Update menggunakan setter
termo.fahrenheit = 100  # Set ke 100°F
print(f"Setelah set ke 100°F: {termo.info()}")

termo.kelvin = 300  # Set ke 300K
print(f"Setelah set ke 300K: {termo.info()}")

# ==================
# 9. MAGIC METHODS (DUNDER METHODS)
# ==================
print("\n9. MAGIC METHODS")
print("-" * 30)

class Vektor:
    """
    Class yang mendemonstrasikan berbagai magic methods
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation untuk user"""
        return f"Vektor({self.x}, {self.y})"
    
    def __repr__(self):
        """String representation untuk developer"""
        return f"Vektor({self.x}, {self.y})"
    
    def __add__(self, other):
        """Overload operator +"""
        return Vektor(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Overload operator -"""
        return Vektor(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Overload operator * untuk scalar multiplication"""
        return Vektor(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Overload operator =="""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """Magnitude vektor"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)
    
    def __getitem__(self, index):
        """Akses seperti list/tuple"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vektor hanya memiliki 2 komponen")
    
    def __setitem__(self, index, value):
        """Set nilai seperti list"""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Vektor hanya memiliki 2 komponen")

# Test magic methods
print("Testing Magic Methods:")
v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")
print(f"len(v1): {len(v1)}")
print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")

# ==================
# 10. CONTOH PRAKTIS: SISTEM MANAJEMEN PERPUSTAKAAN
# ==================
print("\n10. CONTOH PRAKTIS: SISTEM MANAJEMEN PERPUSTAKAAN")
print("-" * 50)

class Item:
    """Base class untuk semua item di perpustakaan"""
    
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.tersedia = True
        self.peminjam = None
    
    def info(self):
        status = "Tersedia" if self.tersedia else f"Dipinjam oleh {self.peminjam}"
        return f"{self.judul} - {self.penulis} ({self.tahun}) - {status}"
    
    def pinjam(self, nama_peminjam):
        if self.tersedia:
            self.tersedia = False
            self.peminjam = nama_peminjam
            return f"Berhasil meminjam {self.judul}"
        else:
            return f"Item tidak tersedia (dipinjam oleh {self.peminjam})"
    
    def kembalikan(self):
        if not self.tersedia:
            self.tersedia = True
            peminjam_lama = self.peminjam
            self.peminjam = None
            return f"Berhasil mengembalikan {self.judul} dari {peminjam_lama}"
        else:
            return f"Item {self.judul} sudah tersedia"

class Buku(Item):
    def __init__(self, judul, penulis, tahun, isbn, jumlah_halaman):
        super().__init__(judul, penulis, tahun)
        self.isbn = isbn
        self.jumlah_halaman = jumlah_halaman
    
    def info(self):
        return f"Buku: {super().info()} - ISBN: {self.isbn}, {self.jumlah_halaman} hal"

class Majalah(Item):
    def __init__(self, judul, penulis, tahun, edisi, bulan):
        super().__init__(judul, penulis, tahun)
        self.edisi = edisi
        self.bulan = bulan
    
    def info(self):
        return f"Majalah: {super().info()} - Edisi {self.edisi}, {self.bulan}"

class DVD(Item):
    def __init__(self, judul, sutradara, tahun, durasi):
        super().__init__(judul, sutradara, tahun)
        self.durasi = durasi
    
    def info(self):
        return f"DVD: {super().info()} - Durasi: {self.durasi} menit"

class Anggota:
    def __init__(self, nama, nomor_anggota):
        self.nama = nama
        self.nomor_anggota = nomor_anggota
        self.item_dipinjam = []
    
    def info(self):
        return f"Anggota: {self.nama} ({self.nomor_anggota}) - {len(self.item_dipinjam)} item dipinjam"

class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi = []
        self.anggota = []
    
    def tambah_item(self, item):
        self.koleksi.append(item)
        return f"Item ditambahkan: {item.judul}"
    
    def daftar_anggota(self, anggota):
        self.anggota.append(anggota)
        return f"Anggota terdaftar: {anggota.nama}"
    
    def cari_item(self, keyword):
        hasil = []
        for item in self.koleksi:
            if (keyword.lower() in item.judul.lower() or 
                keyword.lower() in item.penulis.lower()):
                hasil.append(item)
        return hasil
    
    def pinjam_item(self, judul, nama_peminjam):
        for item in self.koleksi:
            if item.judul.lower() == judul.lower():
                return item.pinjam(nama_peminjam)
        return "Item tidak ditemukan"
    
    def kembalikan_item(self, judul):
        for item in self.koleksi:
            if item.judul.lower() == judul.lower():
                return item.kembalikan()
        return "Item tidak ditemukan"
    
    def laporan_koleksi(self):
        print(f"\n=== KOLEKSI PERPUSTAKAAN {self.nama} ===")
        tersedia = sum(1 for item in self.koleksi if item.tersedia)
        dipinjam = len(self.koleksi) - tersedia
        
        print(f"Total item: {len(self.koleksi)}")
        print(f"Tersedia: {tersedia}")
        print(f"Dipinjam: {dipinjam}")
        print("\nDaftar item:")
        
        for item in self.koleksi:
            print(f"  {item.info()}")

# Test sistem perpustakaan
print("Testing Sistem Perpustakaan:")
perpus = Perpustakaan("Perpustakaan Kota")

# Tambah item
buku1 = Buku("Python Programming", "John Smith", 2023, "978-123456789", 350)
buku2 = Buku("Data Science Handbook", "Jane Doe", 2022, "978-987654321", 500)
majalah1 = Majalah("Tech Today", "Editor Team", 2024, "Vol. 15", "Januari")
dvd1 = DVD("Programming Tutorial", "Tech Corp", 2023, 180)

print(perpus.tambah_item(buku1))
print(perpus.tambah_item(buku2))
print(perpus.tambah_item(majalah1))
print(perpus.tambah_item(dvd1))

# Daftar anggota
anggota1 = Anggota("Ali Rahman", "A001")
anggota2 = Anggota("Sari Dewi", "A002")
print(perpus.daftar_anggota(anggota1))
print(perpus.daftar_anggota(anggota2))

# Pinjam dan kembalikan
print(f"\n{perpus.pinjam_item('Python Programming', 'Ali Rahman')}")
print(f"{perpus.pinjam_item('Data Science Handbook', 'Sari Dewi')}")

# Laporan
perpus.laporan_koleksi()

# Kembalikan item
print(f"\n{perpus.kembalikan_item('Python Programming')}")
perpus.laporan_koleksi()

# ==================
# TIPS DAN BEST PRACTICES
# ==================
print("\n" + "="*60)
print("TIPS DAN BEST PRACTICES OOP:")
print("="*60)
print("""
1. SINGLE RESPONSIBILITY PRINCIPLE
   - Setiap class harus memiliki satu alasan untuk berubah
   - Fokus pada satu tugas/tanggung jawab

2. ENCAPSULATION
   - Gunakan private/protected attributes untuk data sensitif
   - Gunakan properties untuk kontrol akses
   - Hide implementation details

3. INHERITANCE
   - Gunakan inheritance untuk "is-a" relationship
   - Hindari deep inheritance hierarchies
   - Favor composition over inheritance

4. POLYMORPHISM
   - Gunakan abstract base classes untuk interface
   - Implement method overriding yang konsisten
   - Duck typing untuk fleksibilitas

5. NAMING CONVENTIONS
   - Class names: PascalCase (e.g., MyClass)
   - Method/variable names: snake_case (e.g., my_method)
   - Private attributes: _private atau __very_private
   - Constants: UPPER_CASE

6. DOCSTRINGS DAN TYPE HINTS
   - Dokumentasikan class dan method dengan docstring
   - Gunakan type hints untuk clarity
   - Contoh: def method(self, param: int) -> str:

7. COMPOSITION
   - Gunakan composition untuk "has-a" relationship
   - Lebih fleksibel daripada inheritance
   - Easier testing dan maintenance

8. TESTING
   - Test setiap method secara individual
   - Mock dependencies untuk unit testing
   - Test edge cases dan error handling
""")

print("\n" + "="*60)
print("LATIHAN OOP:")
print("="*60)
print("""
Coba buat sistem OOP untuk:
1. E-commerce (Product, Customer, Order, Payment)
2. School Management (Student, Teacher, Course, Grade)
3. Banking System (Account, Transaction, Customer)
4. Game RPG (Character, Weapon, Skill, Inventory)
5. Social Media (User, Post, Comment, Like)
6. Restaurant POS (Menu, Order, Customer, Payment)
7. Hospital Management (Patient, Doctor, Appointment)
8. Library System (yang lebih kompleks)
9. Car Rental System
10. Hotel Booking System
""")
