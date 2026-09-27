import os
import telebot
import google.generativeai as genai

# Bot ve Gemini API Ayarları
TELEGRAM_TOKEN = '8947672500:AAEz13FwQC_IEhTOLIvtcZhoJ6ui98VwHqA'
GEMINI_API_KEY = 'AQ.Ab8RN6KgrTCaHrE7EjsSIf7nIhV7Fb44qwK-KRl1gRHR1tkJiQ' 

bot = telebot.TeleBot(TELEGRAM_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)

# Gemini modelini ayarlıyoruz (Koçluk karakteri veriyoruz)
generation_config = {
    "temperature": 0.7,
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest"
)
    generation_config=generation_config,
    system_instruction="Sen profesyonel, motive edici, samimi ve bilgili bir kişisel spor ve beslenme koçusun. Kullanıcılara antrenman, kalori takibi, beslenme ve sağlıklı yaşam konularında rehberlik ediyorsun. Türkçe yanıtlar veriyorsun."
)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Selam! Ben senin 7/24 bulutta çalışan kişisel yapay zeka spor ve beslenme koçunum. Hedeflerine ulaşman için buradayım! Bana antrenman, beslenme veya diyet hakkında her şeyi sorabilirsin. 🚀💪")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    try:
        user_message = message.text
        response = model.generate_content(user_message)
        ai_reply = response.text
        bot.reply_to(message, ai_reply)
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu koçum: {str(e)}")

if __name__ == "__main__":
    print("Gemini destekli bot 7/24 çalışmaya hazır...")
    bot.infinity_polling()
