import easyocr
import google.generativeai as genai
from PIL import Image
import os

# -------------------------------
# CONFIG
# -------------------------------
GEMINI_API_KEY = "AIzaSyAN-vXi49_aCs2pJCYw65XhbyXTYBcbm54"   # <-- put your Gemini free-tier API key here
genai.configure(api_key=GEMINI_API_KEY)

# Gemini text-only free model
MODEL_NAME = "gemini-2.0-flash"  # works on free tier


# -------------------------------
# OCR FUNCTION
# -------------------------------
def extract_text_from_image(image_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image_path, detail=0)
    text = "\n".join(result)
    return text


# -------------------------------
# LAYMAN EXPLANATION FUNCTION
# -------------------------------
def explain_in_layman(text):
    model = genai.GenerativeModel(MODEL_NAME)

    prompt = f"""
You are a medical AI assistant.
Explain the following medical report in **very simple layman terms**.
Avoid medical jargon.
Explain line by line, and add a final summary.

Report Text:
{text}
"""

    response = model.generate_content(prompt)
    return response.text


# -------------------------------
# MAIN FUNCTION
# -------------------------------
def analyze_report(image_path):
    print("\n🔍 Extracting text from image...")
    extracted = extract_text_from_image(image_path)

    print("\n📄 Extracted Text:")
    print("EXTRACTED:\n", extracted)
    print(extracted)

    print("\n🧠 Generating layman explanation...")
    explanation = explain_in_layman(extracted)

    return explanation


# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    image_path = "image.png"   # <-- put your test image here

    if not os.path.exists(image_path):
        print("❌ Image not found! Please check the file path.")
    else:
        output = analyze_report(image_path)
        print("\n\n✅ FINAL LAYMAN EXPLANATION:\n")
        print(output)
