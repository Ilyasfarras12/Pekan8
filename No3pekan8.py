def ganjil(n):
    if n % 2 != 0:
        return "Ganjil"
    else:
        return "Genap"

# pemanggilan fungsi
hasil = ganjil(100)
print(hasil)  # Output: Genap

hasil = ganjil(27)
print(hasil)  # Output: Ganjil