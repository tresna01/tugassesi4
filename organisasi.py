jenis_kelamin = input("Jenis Kelamin (Laki-laki/Perempuan): ")
berat_badan = float(input("Berat Badan (kg): "))
tinggi_badan = int(input("Tinggi Badan (cm): "))
usia = int(input("Usia: "))
nilai_akademis = float(input("Nilai Akademis: "))
skill = input("Memiliki Skill (Menembak/Memanah/Berkuda): ")
cacat = input("Memiliki Cacat Tubuh (Ya/Tidak): ")

def cek_kelayakan(jenis_kelamin, berat_badan, tinggi_badan, usia, nilai_akademis, skill, cacat):
    if jenis_kelamin == "perempuan" :
        if berat_badan >= 45 and berat_badan <= 50 and tinggi_badan >= 165 and usia <= 20 and not cacat:
           return "lolos"
        elif nilai_akademis >= 90 and usia <= 30 and not cacat :
           return "lolos"
        elif skill.lower() in ['menembak', 'memanah', 'berkuda']:
            return "lolos"
        elif cacat == "tidak" :
            return "lolos"
        else:
            return "tidak lolos"
        
    elif jenis_kelamin == "laki-laki" :
        if berat_badan <= 70 and tinggi_badan >= 170 and usia < 25 and not cacat:
            return "lolos"
        elif nilai_akademis >= 90 and usia <= 30 and not cacat :
               return "lolos"
        elif skill.lower() in ['menembak', 'memanah', 'berkuda']:
            return "lolos"
        elif cacat == "tidak" :
            return "lolos"
        else:
            return "tidak lolos"
        
hasil_kelayakan = (jenis_kelamin, berat_badan,tinggi_badan,usia.skill.nilai_akademis,cacat)
print ("kelayakan anda :", hasil_kelayakan)