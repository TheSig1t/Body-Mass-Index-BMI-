# Program Kalkulator Berat Badan dan Status Berat Badan
# Sigit Arkananta XII RPL D
print("=== Kalkulator Berat Badan ===")
tinggi_cm = float(input("Masukkan tinggi badan Anda (cm): "))
berat_kg = float(input("Masukkan berat badan Anda (kg): "))

# Menghitung BMI (Body Mass Index) / Massa tubuh
tinggi_m = tinggi_cm / 100
bmi = berat_kg / (tinggi_m ** 2) # operator ** yang bearti kuadrat jadi tinggi m²

# Menentukan status berat badan
if bmi < 18.5:
    status = "Kurang berat badan".format(18.5 * (tinggi_m ** 2), 24.9 * (tinggi_m ** 2))
    pesan = "Anda kurang berat badan. Berat badan ideal Anda seharusnya antara {:.2f} kg dan {:.2f} kg."
elif 18.5 <= bmi <= 24.9:
    status = "Berat badan ideal"
    pesan = "Berat badan Anda ideal. Pertahankan!"
else:
    status = "Kelebihan berat badan"
    pesan = "Anda memiliki kelebihan berat badan. Berat badan ideal Anda seharusnya antara {:.2f} kg dan {:.2f} kg.".format(18.5 * (tinggi_m ** 2), 24.9 * (tinggi_m ** 2))

# Menampilkan hasil
print("BMI(Massa Tubuh) Anda:", bmi)
print("Status berat badan Anda:", status)
print(pesan)
