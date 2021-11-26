print("=" * 7+"Program Manipulasi String"+ "=" * 7 )
print("Pilihan Menu : " )
print("1. Hitung kata ")
print("2. cek kata ")
print("3. ubah kata")
pilihan = int(input("Pilihan anda : "))

def hitung_kata():
    kalimat = str(input("masukkan sebuah kalimmat/kata : "))
    hitung = str(input("masukkan kata yang ingin dihitung : "))
    kata1= kalimat.lower()
    kata2= hitung.lower()
    if kata2 in kata1:
        a = kata1.count(kata2)
        print("Terdapat sebanyak",a,"kata",hitung,"di dalam string")
    
def cek_kata():
    kata= str(input("Masukan sebuah kalimat/kata : "))
    cek= str(input("Masukan kata yang ingin di cek : "))
    if cek in kata:
        print("kata",cek,"terdapat di dalam string")
        print("String diubah menjadi : ")
        x = kata.replace(cek,cek.upper())
        print(x)
    
    else:
        print("Kata",cek,"tidak terdapat di dalam string ")
        print("String diubah menjadi : ")
        print(kata,cek)

def ubah_kata():
    kata= input("Masukan sebuah kalimat/kata : ")
    ubah= input("Masukan kata yang ingin di ubah : ")
    ganti= input("Masukan kata pengganti :")
    print("Anda akan mengubah kata",ubah,"Menjadi",ganti,"Sebanyak 1x")
    cek2= input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")
    if cek2=="no":
        print("String berhasil diubah menjadi : ")
        print(kata.replace(ubah,ganti,1))

    elif cek2== "yes":
        jumlahganti= int(input("Masukan jumlah total penggantian : "))
        print("String berhasil diubah menjadi : ")
        print(kata.replace(ubah,ganti,jumlahganti))




if pilihan == int("1"):
    hitung_kata()
elif pilihan == int("2"):
    cek_kata()
elif pilihan == int("3"):
    ubah_kata()
else:
    print("gagal, coba lagi")
    
                    
    
