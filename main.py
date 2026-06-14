import telebot
import datetime

TOKEN = "YOUR_BOT_TOKEN"
ADMIN_ID = 6533813373

bot = telebot.TeleBot(8827195006:AAEjI6NbHMJWQKrr_kjCGMK4yzMykjaFeEw)

orders = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
    "🚀 Welcome!\nSend your order link.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user = message.from_user.username
    text = message.text

    order_id = len(orders) + 1001
    orders[order_id] = {
        "user": user,
        "link": text,
        "status": "Pending"
    }

    bot.send_message(message.chat.id,
    f"Order Received ✅\nID: #{order_id}")

    bot.send_message(ADMIN_ID,
    f"New Order\nID: #{order_id}\nUser: @{user}\nLink: {text}")

bot.polling()
