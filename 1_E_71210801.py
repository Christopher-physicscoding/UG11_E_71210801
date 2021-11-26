print ("Menu Program Yang Tersedia ")
print ("1. pangkatkan angka ")
print ("2. akarkan bilangan ")
pilihan = int(input("masukkan pilihan yang diinginkan: "))

def mat_pangkat():
    print("masukkan angka yang ingin di Pangkatkan")
    angka = float(input("Angka: "))
    print("ingin memodifikasi pangkat ? (yes/no)")
    jawaban = str(input(": "))
    if jawaban == 'yes':
        x = float(input("masukkan nilai pangkat: "))
        y = angka ** x
        print("hasil dari",str(angka)+("^")+str(x),'=',y)
    elif  jawaban == 'no':
        y = angka ** 2
        print("hasil dari",str(angka)+"^"+str(2),'=',y)
    else:
        print(" gagal, coba lagi")
        mat_pangkat()
        
def mat_akar():
    print("masukkan angka yang ingin di Akar")
    angka = float(input("Angka: "))
    print("ingin memodifikasi akar ? (yes/no) ")
    jawaban = str(input(": "))
    if jawaban == "yes":
        x = float(input("masukkan nilai akar: "))
        y = angka ** (1/ x )
        print("hasil akar pangkat", str(x),"dari", str(angka), "=", round(y,2))
    elif jawaban == "no":
        y = angka ** (1/2)
        print("hasil akar pangkat", str(2),"dari", str(angka), "=", round(y,2))
    else:
        print("gagal coba lagi")
        mat_akar()

if pilihan == int("1"):
    mat_pangkat()
elif pilihan == int("2"):
    mat_akar()
else:
    print("gagal mohon coba lagi")
        
