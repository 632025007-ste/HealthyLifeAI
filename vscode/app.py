import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from kalkulator import hitung_bmi
from chatbot import tanya_ai
def menu(tujuan):

    if tujuan=="Menurunkan Berat Badan":

        return """
🥗 Sarapan
• Oatmeal
• Telur rebus

🍗 Siang
• Nasi merah
• Dada ayam
• Sayur

🍎 Malam
• Salad
• Ikan
"""

    elif tujuan=="Menjaga Berat Badan":

        return """
🍚 Sarapan
• Roti gandum
• Susu

🍛 Siang
• Nasi
• Ayam
• Sayur

🥣 Malam
• Sup ayam
"""

    else:

        return """
🥚 Sarapan
• Telur
• Pisang

🍗 Siang
• Nasi
• Daging
• Sayur

🥛 Malam
• Susu
• Kentang
"""
def olahraga(bmi):

    if bmi<18.5:

        return """
🏋 Latihan beban
🚶 Jalan santai
🥛 Fokus menaikkan massa otot
"""

    elif bmi<25:

        return """
🏃 Jogging
🚴 Bersepeda
🏊 Berenang
"""

    elif bmi<30:

        return """
🚶 Jalan cepat
🚴 Sepeda
🏊 Renang
"""

    else:

        return """
🚶 Jalan 30 menit
🧘 Yoga
🚴 Sepeda ringan
"""

st.set_page_config(
    page_title="HealthyLife AI",
    page_icon="assets/logoSYM.jpeg",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background-color:#081C15;
}

h1,h2,h3{
    color:#198754;
}

[data-testid="stSidebar"]{
    background-color:#081C15;
}

.stButton>button{
    background-color:#2D6A4F;
    color:white;
    border-radius:12px;
    border:none;
    height:45px;
    width:100%;
    font-size:16px;
}

.stButton>button:hover{
    background-color:#40916C;
    color:blue;
}

div[data-testid="stMetric"]{
    background-color:blue;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

import os

logo_path = "assets/logoSYM.jpeg"

if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=150)
else:
    st.sidebar.warning("Logo tidak ditemukan")

st.sidebar.title("🏥 HealthyLife AI")

st.sidebar.success("🤖 AI Health Assistant")

st.sidebar.markdown("---")

st.sidebar.info("""
HealthyLife AI membantu Anda:

✅ Menghitung BMI

🥗 Memberikan rekomendasi makanan

🏃 Memberikan rekomendasi olahraga

💬 Menjawab pertanyaan kesehatan
""")

st.sidebar.title("HealthyLife AI")

st.sidebar.success("🤖 AI Health Assistant")

st.sidebar.markdown("---")

st.sidebar.info("""
HealthyLife AI membantu Anda:

✅ Menghitung BMI

🥗 Memberikan rekomendasi makanan

🏃 Memberikan rekomendasi olahraga

💬 Menjawab pertanyaan kesehatan
""")
st.title("🏥 HealthyLife AI")
st.write("Selamat datang di HealthyLife AI!")
tujuan = st.selectbox(
    "Pilih tujuan Anda",
    (
        "Menurunkan Berat Badan",
        "Menjaga Berat Badan",
        "Menaikkan Berat Badan"
    )
)
st.write("Tujuan Anda:", tujuan)

st.subheader("🥗 Rekomendasi Menu")

st.write(menu(tujuan))

st.divider()

st.subheader("💬 Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "riwayat_bmi" not in st.session_state:
        st.session_state.riwayat_bmi = []
st.sidebar.markdown("---")
st.sidebar.subheader("📜 Riwayat")

st.sidebar.write(
    f"Jumlah chat: {len(st.session_state.messages)}"
)

if st.sidebar.button("🗑 Hapus Riwayat"):

    st.session_state.messages = []

    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Tulis pertanyaan Anda...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    jawaban = tanya_ai(prompt)

    with st.chat_message("assistant"):
        st.write(jawaban)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": jawaban
        }
    )
st.divider()

st.header("📊 Hitung BMI")

berat = st.number_input(
    "Berat Badan (kg)",
    30,
    200
)

tinggi = st.number_input(
    "Tinggi Badan (cm)",
    100,
    230
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "⚖ Berat",
        f"{berat} kg"
    )

with col2:
    st.metric(
        "📏 Tinggi",
        f"{tinggi} cm"
    )

if st.button("Hitung BMI"):

    bmi, kategori = hitung_bmi(
        berat,
        tinggi
    )

    st.success(f"BMI Anda : {bmi}")

    st.info(kategori)

    from datetime import datetime

    st.session_state.riwayat_bmi.append({
    "Tanggal": datetime.now().strftime("%d-%m-%Y %H:%M"),
    "Berat": berat,
    "BMI": bmi
    })

    st.subheader("🏃 Rekomendasi Olahraga")

    st.write(olahraga(bmi))
st.divider()

st.header("📈 Grafik Perkembangan BMI")

if len(st.session_state.riwayat_bmi) > 0:

    df = pd.DataFrame(st.session_state.riwayat_bmi)

    st.dataframe(df, use_container_width=True)

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(df["Tanggal"], df["BMI"], marker="o")

    ax.set_xlabel("Tanggal")
    ax.set_ylabel("BMI")
    ax.set_title("Perkembangan BMI")

    plt.xticks(rotation=30)

    st.pyplot(fig)

else:
    st.info("Belum ada data BMI.")

st.header("⚖️ Grafik Berat Badan")

if len(st.session_state.riwayat_bmi) > 0:

    fig2, ax2 = plt.subplots(figsize=(8,4))

    ax2.plot(df["Tanggal"], df["Berat"], marker="o")

    ax2.set_xlabel("Tanggal")
    ax2.set_ylabel("Berat (kg)")
    ax2.set_title("Perkembangan Berat Badan")

    plt.xticks(rotation=30)

    st.pyplot(fig2)