import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8827195006:AAEjI6NbHMJWQKrr_kjCGMK4yzMykjaFeEw"
ADMIN_ID = 6533813373

bot = telebot.TeleBot(TOKEN)

# ================= MENU =================
def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = KeyboardButton("📦 Order Now")
    btn2 = KeyboardButton("📜 My Orders")
    btn3 = KeyboardButton("📞 Help")

    markup.add(btn1)
    markup.add(btn2, btn3)

    return markup

# ================= START =================
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🚀 Welcome to Premium Order Bot\n\nChoose an option below:",
        reply_markup=main_menu()
    )

# ================= HANDLER =================
@bot.message_handler(func=lambda message: True)
def handle(message):
    text = message.text
    user = message.from_user.username

    if text == "📦 Order Now":
        bot.send_message(message.chat.id, "👉 Send your TikTok / service link now")

    elif text == "📜 My Orders":
        bot.send_message(message.chat.id, "📦 You have no orders yet.")

    elif text == "📞 Help":
        bot.send_message(message.chat.id, "📞 Contact admin: @SWVRSTD")

    else:
        # order received
        bot.send_message(
            ADMIN_ID,
            f"🔔 NEW ORDER\n\nUser: @{user}\nLink: {text}"
        )

        bot.send_message(
            message.chat.id,
            "✅ Order received successfully!\nWe will process it soon."
        )

bot.polling()    else:
        bot.send_message(ADMIN_ID, f"New Order:\n{text}")
        bot.send_message(message.chat.id, "Order received ✅")
