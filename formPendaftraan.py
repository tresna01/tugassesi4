nama = str(input("masukan nama anda :"))
tempat_lahir = str(input("tempat lahir :"))
tanggal_lahir = int(input("tanggal lahir :"))
tahun_lahir = int(input("tahun lahir :"))
jenis_kelamin = str(input("jenis kelamin :"))
tahun_sekarang = int(input("tahun sekarang :"))

umur = tahun_sekarang-tahun_lahir

## 3 mapel
nilai_englis =float(input("masukan nilai englis anda :"))
nilai_matematika =float(input("masukan nilai matematika anda :"))
nilai_indonesia = float(input("masukan nilai indonesia anda :"))

nilai_rata_rata = (nilai_englis + nilai_matematika + nilai_indonesia) / 3

print("Nilai rata-rata anda adalah : %.2f" % nilai_rata_rata)

## seleksi masuk jurusan
if nilai_rata_rata >= 80 and jenis_kelamin == "laki laki" and umur <=25:
    print("SELAMAT ANDA DITERIMA JURUSAN TEKNIK INFORMATIKA")
elif nilai_rata_rata >=80 and jenis_kelamin == "Perempuan" and umur <=25
    print("SELAMAT ANDA DITERIMA DI JURUSAN SISTEM INFORMASI")
elif umur <=25:
    print("ANDA DITERIMA DI JURUSAN DKV")
else:
    print("MAAF ANDA TIDAK DITERIMA DI JURUSAN MANA PUN")