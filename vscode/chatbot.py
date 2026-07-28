from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def tanya_ai(prompt):

    sistem = f"""
Anda adalah HealthyLife AI.

Aturan:

- Jawab hanya tentang kesehatan.
- Fokus pada pola hidup sehat.
- Berikan jawaban sederhana.
- Jika ditanya selain kesehatan, jawab:
"Maaf, saya hanya membantu pertanyaan mengenai kesehatan dan pola hidup sehat."

Pertanyaan pengguna:

{prompt}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=sistem
    )

    return response.text