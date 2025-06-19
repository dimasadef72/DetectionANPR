import requests

# Ganti dengan token dari BotFather
TELEGRAM_BOT_TOKEN = "8193361549:AAES0Hkq1eS5N_MYR92yErQxnPIElgjqCQI"

# Ganti dengan Chat ID dari @userinfobot
TELEGRAM_CHAT_ID = "1115545761"

# Fungsi untuk mengirim gambar ke Telegram dengan plat nomor dan lokasi
def send_telegram_image(image_path, plate_text, location_address):
    caption = f"🚗 Plat Nomor Terdeteksi: {plate_text}\n\n📍 Lokasi Deteksi: {location_address}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    with open(image_path, "rb") as image:
        files = {"photo": image}
        data = {"chat_id": TELEGRAM_CHAT_ID, "caption": caption}
        response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print(f"Gambar terkirim: {image_path} dengan caption: {caption}")
    else:
        print(f"Gagal mengirim gambar: {response.text}")
