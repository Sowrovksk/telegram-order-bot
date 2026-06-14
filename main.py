import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8827195006:AAEjI6NbHMJWQKrr_kjCGMK4yzMykjaFeEw"
ADMIN_ID = 6533813373

bot = telebot.TeleBot(TOKEN)

# ===== MENU =====
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("📦 Order Now"))
    markup.add(KeyboardButton("📜 My Orders"), KeyboardButton("📞 Help"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🚀 Welcome to Premium Bot\n\nChoose an option below:",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda message: True)
def handle(message):
    text = message.text

    if text == "📦 Order Now":
        bot.send_message(message.chat.id, "Send your TikTok link now 👇")

    elif text == "📞 Help":
        bot.send_message(message.chat.id, "Contact admin: @SWVRSTD")

    elif text == "📜 My Orders":
        bot.send_message(message.chat.id, "No orders found yet.")

    else:
        bot.send_message(ADMIN_ID, f"New Order:\n{text}")
        bot.send_message(message.chat.id, "Order received ✅")
