import telebot
import datetime

# এখানে তোমার Token বসাবে (নিজে বসাবে)
TOKEN = "8827195006:AAEjI6NbHMJWQKrr_kjCGMK4yzMykjaFeEw"

ADMIN_ID = 6533813373

bot = telebot.TeleBot(TOKEN)

orders = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
    "🚀 Welcome to Order Bot\n\nSend your service link to place order.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user = message.from_user.username
    text = message.text

    order_id = len(orders) + 1001

    orders[order_id] = {
        "user": user,
        "link": text,
        "status": "Pending",
        "date": str(datetime.datetime.now())
    }

    bot.send_message(message.chat.id,
    f"✅ Order Received!\nOrder ID: #{order_id}\nStatus: Pending")

    bot.send_message(ADMIN_ID,
    f"🔔 New Order\n\nID: #{order_id}\nUser: @{user}\nLink: {text}")

bot.polling()
