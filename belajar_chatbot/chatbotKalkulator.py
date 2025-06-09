import re

def kalkulator_chatbot(input_user):
    input_user = input_user.lower()
    angka = list(map(int, re.findall(r'\d+', input_user)))

    if len(angka) < 2:
        return "Masukkan dua angka untuk dihitung yaa"

    if "tambah" in input_user or "plus" in input_user:
        hasil = angka[0] + angka[1]
    elif "kurang" in input_user or "minus" in input_user:
        hasil = angka[0] - angka[1]
    elif "kali" in input_user or "x" in input_user:
        hasil = angka[0] * angka[1]
    elif "bagi" in input_user or "/" in input_user:
        if angka[1] == 0:
            return "Ups, Tidak bisa membagi dengan nol."
        hasil = angka[0] / angka[1]
    else:
        return "Maaf, saya tidak mengerti operasi itu..."

    return f"Hasilnya adalah {hasil}"

# Program utama
print("Selamat datang di Chatbot Kalkulator <3 (Ketik 'keluar' kapan saja untuk berhenti)\n")

while True:
    user_input = input("Kamu: ")
    if user_input.lower() in ["exit", "keluar", "stop"]:
        print("Bot: Sampai jumpa!")
        break

    response = kalkulator_chatbot(user_input)
    print("Bot:", response)

    # Pertanyaan ulang
    ulang = input("Bot: Ada yang Ingin Dihitung lagi? (ya/tidak): ")
    if ulang.lower() not in ["ya", "y"]:
        print("Bot: Baiklah, sampai bertemu kembali^.^")
        break
