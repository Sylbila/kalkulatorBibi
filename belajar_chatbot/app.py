from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

def ubah_ke_operator(teks):
    teks = teks.lower() 
    teks = teks.replace("tambah", "+").replace("plus", "+")
    teks = teks.replace("kurang", "-").replace("minus", "-")
    teks = teks.replace("kali", "*").replace("x", "*")
    teks = teks.replace("bagi", "/")
    return teks

def kalkulator_lanjutan(input_user):
    ekspresi = ubah_ke_operator(input_user)
    ekspresi_bersih = re.sub(r"[^0-9+\-*/.]", " ", ekspresi)
    jumlah_operator = len(re.findall(r"[+\-*/]", ekspresi_bersih))

    if jumlah_operator < 2:
        return "Masukkan minimal 2 operasi hitung, ya! Contoh: 2 tambah 3 kali 4"
    
    try:
        hasil = eval(ekspresi_bersih)
        return f"Hasilnya adalah {hasil}"
    except:
        return "Maaf, saya tidak bisa memahami input itu."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = kalkulator_lanjutan(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
