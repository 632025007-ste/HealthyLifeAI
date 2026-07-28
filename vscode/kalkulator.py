def hitung_bmi(berat, tinggi):

    tinggi = tinggi / 100

    bmi = round(berat/(tinggi**2),2)

    if bmi < 18.5:
        kategori = "Kurus"

    elif bmi <25:
        kategori="Normal"

    elif bmi <30:
        kategori="Overweight"

    else:
        kategori="Obesitas"

    return bmi,kategori
