import re

def ubah_ke_operator(teks):
    # Ganti kata-kata jadi simbol
    teks = teks.lower()
    teks = teks.replace("tambah", "+")
    teks = teks.replace("plus", "+")
    teks = teks.replace("kurang", "-")
    teks = teks.replace("minus", "-")
    teks = teks.replace("kali", "*")
    teks = teks.replace("x", "*")
    teks = teks.replace("bagi", "/")
    return teks 

def kalkulator_lanjutan(input_user):
        ekspresi = ubah_ke_operator(input_user)
        # Hapus karakter selain angka dan operator
        ekspresi_bersih = re.sub(r"[^0-9+\-*/.]", " ", ekspresi)
         # Hitung jumlah operator
        jumlah_operator = len(re.findall(r"[+\-*/]", ekspresi_bersih))
        if jumlah_operator < 2:
            return "Masukkan minimal 2 operasi hitung, ya! Contoh: 2 tambah 3 kali 4"
        try:
            hasil = eval(ekspresi_bersih)
            return f"Hasilnya adalah {hasil}"
        except:
            return "Maaf, saya tidak bisa memahami input itu."

# Program utama
print("Selamat datang di Chatbot Kalkulator2 <3 (Ketik 'keluar' kapan saja untuk berhenti)\n")

# Contoh penggunaan
while True:
    user_input = input("Kamu: ")
    if user_input.lower() in ["keluar", "exit"]:
        print("Bot: Sampai jumpa!")
        break
    print("Bot:", kalkulator_lanjutan(user_input))
