import math

def hitung_luas_segitiga(a, b, c):
    # Menghitung setengah keliling segitiga
    s = (a + b + c) / 2
    
    # Menghitung luas segitiga menggunakan rumus Heron
    luas = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return luas

def hitung_keliling_segitiga(a, b, c):
    # Menghitung keliling segitiga
    keliling = a + b + c
    return keliling

# Meminta input panjang sisi-sisi segitiga dari pengguna
sisi_a = float(input("Masukkan panjang sisi a: "))
sisi_b = float(input("Masukkan panjang sisi b: "))
sisi_c = float(input("Masukkan panjang sisi c: "))

# Menghitung luas segitiga dan keliling
luas = hitung_luas_segitiga(sisi_a, sisi_b, sisi_c)
keliling = hitung_keliling_segitiga(sisi_a,sisi_b,sisi_c)

print("luas segitiga adalah",luas)
print("keliling segitiga adalah",keliling)
