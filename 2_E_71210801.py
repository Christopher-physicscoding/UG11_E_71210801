kata = str(input("Masukkan kata: "))
jumlah = len (kata)
def kata_tengah(kata):
    return kata[(len(kata)-1)//2:(len(kata)+2)//2]

def kata_tengah2(kata):
    return kata[(len(kata)-2)//2:(len(kata)+3)//2]
def kata_tengah3(kata):
    return kata[(len(kata)-3)//2:(len(kata)+4)//2]

if jumlah < 7:
    print("huruf tengah pada kata", kata, "adalah", kata_tengah(kata))
elif jumlah > 6 and jumlah < 8:
    print("huruf tengah pada kata", kata, "adalah", kata_tengah2(kata))
elif jumlah > 7:
    print("huruf tengah pada kata", kata, "adalah", kata_tengah3(kata))
