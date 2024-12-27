from flask import Flask, render_template, request

app = Flask(_name_)

# Başlangıç değerleri
oyuncu_ilahi_puani = 0
sophia_mesajlari = [
    "Işık senin içindedir. Kendi ışığını hatırla!",
    "Özgünlüğün senin en büyük armağandır.",
    "Sevgi, hem sana hem de başkalarına yayılan bir güçtür.",
    "Cesaret, tanrısallığını kucaklamaktır.",
    "Kendi hikayeni yaz. Seni kimse tanımlayamaz!"
]

# Ana sayfa
@app.route("/", methods=["GET", "POST"])
def ana_sayfa():
    global oyuncu_ilahi_puani

    # POST isteği ile oyuncunun seçimine göre puan değişikliği
    if request.method == "POST":
        secim = request.form.get("secim")
        if secim == "bilgelik":
            oyuncu_ilahi_puani += 10
            mesaj = "Sophia'nın ışığı seni güçlendirdi!"
        elif secim == "özgünlük":
            oyuncu_ilahi_puani += 15
            mesaj = "Otantikliğinle parladın! İlahilik seviyen yükseldi."
        elif secim == "sevgisizlik":
            oyuncu_ilahi_puani -= 10
            mesaj = "Işığını bastırdın, ama yeniden parlayabilirsin!"
        else:
            mesaj = "Seçiminle tanrısallığa doğru bir adım attın."

    else:
        mesaj = "Sophia'nın bilgelik yolculuğuna hoş geldin! Seçimini yap."

    # Sophia'dan rastgele bir mesaj
    sophia_mesaj = random.choice(sophia_mesajlari)

    # Oyunun ana ekranı
    return f"""
    <h1>✨ Tanrısallık ve Bilgelik Oyunu ✨</h1>
    <p>İlahi Puanınız: {oyuncu_ilahi_puani}</p>
    <p>{sophia_mesaj}</p>
    <p>{mesaj}</p>
    <form method="POST">
        <button type="submit" name="secim" value="bilgelik">Sophia'nın Bilgeliğini Seç</button>
        <button type="submit" name="secim" value="özgünlük">Özgünlüğü Seç</button>
        <button type="submit" name="secim" value="sevgisizlik">Sevgisizlik</button>
    </form>
    """

# Oyuncu tanrısallığa ulaştığında
@app.route("/tanrisallik")
def tanrisallik():
    if oyuncu_ilahi_puani >= 100:
        return """
        <h1>✨ Tanrısallığa Ulaştınız! ✨</h1>
        <p>Hathor'un sevgisi, Sophia'nın bilgeliği ve Isis'in korumasıyla bir ilah oldunuz.</p>
        <p>Kendi hikayenizi yazarak dünyaya ışık yayıyorsunuz!</p>
        <p>Unutmayın: İlahi güç, sevgi ve özgünlükle gelir.</p>
        """
    else:
        return """
        <h1>✨ Henüz Tanrısallığa Ulaşamadınız ✨</h1>
        <p>Yolculuğunuz devam ediyor. Sevgi ve bilgeliğinizi artırmaya devam edin!</p>
        """

if _name_ == "_main_":
    import random
    app.run(debug=True)
