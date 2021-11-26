import random
print("=" * 7+"Program test aritmatika dasar "+ "=" * 7 )
print("Pilihan level yang tersedia : " )
print("1. Easy ")
print("2. Medium ")
print("3. Hard")
pilihan = int(input("masukkan tingkatan yang ingin anda coba : "))
operasi = ['+','-','/','*']

def hasil(pilihan):
    hasil = 0
    salah = False
    SOAL = ""

    if pilihan == int("1"):
        x = random.randint(20, 50)
        y = random.randint(20, 50)
        z = random.choice(operasi)
        SOAL = f"{x} {z} {y}"
        print("Berapakah hasil dari ", x, z, y)
        if z == '-':
            jawaban = int(x - y)
        elif  z == '+':
            jawaban = int(x + y)
        elif z == '/':
            jawaban = int(x / y)
        elif z == '*':
            jawaban = int(x * y)
    
    elif pilihan == int("2"):
        w = random.randint(20, 70)
        x = random.randint(20, 70)
        y = random.randint(20, 70)
        z = random.choice(operasi)
        v = random.choice(operasi)
        SOAL = f"{w} {z} {y} {v} {x}"
        print("Berapakah hasil dari ", w, z, y, v, x)
        if z == '-':
            if v == '/':
                jawaban = w - y / x
            elif v == '*':
                jawaban = w - y * x
            elif v == '-':
                jawaban = w - y - x
            elif v == '+':
                jawaban = w - y + x
        elif z == '/':
            if v == '-':
                jawaban = w / y - x
            elif v == '+':
                jawaban = w / y + x
            elif v == '/':
                jawaban = w / y / x
            elif v == '*':
                jawaban = w / y * x
        elif z == '+':
            if v == '-':
                jawaban = w + y - x
            elif v == '+':
                jawaban = w + y + x
            elif v == '/':
                jawaban = w + y / x
            elif v == '*':
                jawaban = w + y * x
        
        elif z == '*':
            if v == '-':
                jawaban = w * y - x
            elif v == '+':
                jawaban = w * y + x
            elif v == '/':
                jawaban = w * y / x
            elif v == '*':
                jawaban = w * y * x
    
    elif pilihan == int("3"):
        k = random.randint(20, 100)
        l = random.randint(20, 100)
        m = random.randint(20, 100)
        n = random.randint(20, 100)
        o = random.choice(operasi)
        p = random.choice(operasi)
        q = random.choice(operasi)
        stringsoal = f"{k} {q} {l} {p} {m} {o} {n}"
        print("Berapakah hasil dari ", k, q, l, p, m, o, n)
        if q == '-':
            if p == '-':
                if o == '-':
                    jawaban = k - l - m - n
                elif o == '+':
                    jawaban = k - l - m + n
                elif o == '/':
                    jawaban = k - l - m / n
                elif o == '*':
                    jawaban = k - l - m * n
            elif p == '+':
                if o == '-':
                    jawaban = k - l + m - n
                elif o == '+':
                    jawaban = k - l + m + n
                elif o == '/':
                    jawaban = k - l + m / n
                elif o == '*':
                    jawaban = k - l + m * n
            elif p == '/':
                if o == '-':
                    jawaban = k - l / m - n
                elif o == '+':
                    jawaban = k - l / m + n
                elif o == '/':
                    jawaban = k - l / m / n
                elif o == '*':
                    jawaban = k - l / m * n
            elif p == '*':
                if o == '-':
                    jawaban = k - l * m - n
                elif o == '+':
                    jawaban = k - l * m + n
                elif o == '/':
                    jawaban = k - l * m / n
                elif o == '*':
                    jawaban = k - l * m * n
        elif q == '+':
            if p == '-':
                if o == '-':
                    jawaban = k + l - m - n
                elif o == '+':
                    jawaban = k + l - m + n
                elif o == '/':
                    jawaban = k + l - m / n
                elif o == '*':
                    jawaban = k + l - m * n
            elif p == '+':
                if o == '-':
                    jawaban = k + l + m - n
                elif o == '+':
                    jawaban = k + l + m + n
                elif o == '/':
                    jawaban = k + l + m / n
                elif o == '*':
                    jawaban = k + l + m * n
            elif p == '/':
                if o == '-':
                    jawaban = k + l / m - n
                elif o == '+':
                    jawaban = k + l / m + n
                elif o == '/':
                    jawaban = k + l / m / n
                elif o == '*':
                    jawaban = k + l / m * n
            elif p == '*':
                if o == '-':
                    jawaban = k + l * m - n
                elif o == '+':
                    jawaban = k + l * m + n
                elif o == '/':
                    jawaban = k + l * m / n
                elif o == '*':
                    jawaban = k + l * m * n
        elif q == '+':
            if p == '-':
                if o == '-':
                    jawaban = k + l - m - n
                elif o == '+':
                    jawaban = k + l - m + n
                elif o == '/':
                    jawaban = k + l - m / n
                elif o == '*':
                    jawaban = k + l - m * n
            elif p == '+':
                if o == '-':
                    jawaban = k + l + m - n
                elif o == '+':
                    jawaban = k + l + m + n
                elif o == '/':
                    jawaban = k + l + m / n
                elif o == '*':
                    jawaban = k + l + m * n
            elif p == '/':
                if o == '-':
                    jawaban = k / l / m - n
                elif o == '+':
                    jawaban = k / l / m + n
                elif o == '/':
                    jawaban = k / l / m / n
                elif o == '*':
                    jawaban = k / l / m * n
            elif p == '*':
                if o == '-':
                    jawaban = k / l * m - n
                elif o == '+':
                    jawaban = k / l * m + n
                elif o == '/':
                    jawaban = k / l * m / n
                elif o == '*':
                    jawaban = k / l * m * n
        elif q == '*':
            if p == '-':
                if o == '-':
                    jawaban = k * l - m - n
                elif o == '+':
                    jawaban = k * l - m + n
                elif c2 == '/':
                    jawaban = k * l - m / n
                elif c2 == '*':
                    jawaban = k * l - m * n
            elif p == '+':
                if o == '-':
                    jawaban = k * l + m - n
                elif o == '+':
                    jawaban = k * l + m + n
                elif o == '/':
                    jawaban = k * l + m / n
                elif o == '*':
                    jawaban = k * l + m * n
            elif p == '/':
                if o == '-':
                    jawaban = k * l / m - n
                elif o == '+':
                    jawaban = k * l / m + n
                elif o == '/':
                    jawaban = k * l / m / n
                elif o == '*':
                    jawaban = k * l / m * n
            elif p == '*':
                if o == '-':
                    jawaban = k * l * m - n
                elif o == '+':
                    jawaban = k * l * m + n
                elif o == '/':
                    jawaban = k * l * m / n
                elif o == '*':
                    jawaban = k * l * m * n
    else:
        print("inputan salah")
        salah= True
    if not salah:
        jawab = float(input("Masukkan jawaban anda: "))
        if (jawaban == jawab or jawab == ("%.3f" % jawaban)):
            print("Jawaban anda benar !")
        else:
            print("Jawaban Anda Masih Salah")
            print("Hasil dari ",SOAL, " = %.3f" % jawaban)
hasil(pilihan)
