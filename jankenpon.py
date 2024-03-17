import random

def tentukan_pemenang(pilihan_pemain1, pilihan_pemain2):
    if pilihan_pemain1 == pilihan_pemain2:
        return "Seri"
    elif (pilihan_pemain1 == 'batu' and pilihan_pemain2 == 'gunting') or \
         (pilihan_pemain1 == 'gunting' and pilihan_pemain2 == 'kertas') or \
         (pilihan_pemain1 == 'kertas' and pilihan_pemain2 == 'batu'):
        return "Pemain 1"
    else:
        return "Pemain 2"

pilihan = ['batu', 'gunting', 'kertas']
pilihan_pemain1 = random.choice(pilihan)
pilihan_pemain2 = random.choice(pilihan)

print("Pemain 1 memilih:", pilihan_pemain1)
print("Pemain 2 memilih:", pilihan_pemain2)

pemenang = tentukan_pemenang(pilihan_pemain1, pilihan_pemain2)
print("Pemenang:", pemenang)
