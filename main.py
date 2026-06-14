import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# আপনার টোকেন এবং অ্যাডমিন আইডি বসান
TOKEN = "8827195006:AAEjI6NbHMJWQKrr_kjCGMK4yzMykjaFeEw"
ADMIN_ID = 6533813373

bot = telebot.TeleBot(TOKEN)

# প্রধান মেনু তৈরি
def get_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(KeyboardButton("📦 Order Now"), KeyboardButton("📜 My Orders"))
    markup.add(KeyboardButton("📞 Help"), KeyboardButton("ℹ️ Info"))
    return markup

# স্টার্ট কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        f"👋 হাই {message.from_user.first_name}!\n\nআমাদের প্রিমিয়াম সার্ভিসে আপনাকে স্বাগতম। নিচে থেকে আপনার প্রয়োজনীয় অপশনটি নির্বাচন করুন:",
        reply_markup=get_main_menu()
    )

# বাটন হ্যান্ডেলার
@bot.message_handler(func=lambda message: message.text in ["📦 Order Now", "📜 My Orders", "📞 Help", "ℹ️ Info"])
def handle_menu(message):
    if message.text == "📦 Order Now":
        msg = bot.send_message(message.chat.id, "🔗 দয়া করে আপনার TikTok বা সার্ভিসের লিংকটি পাঠান:", reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, process_order)

    elif message.text == "📜 My Orders":
        bot.send_message(message.chat.id, "📦 বর্তমানে আপনার কোনো অর্ডার পেন্ডিং নেই।")

    elif message.text == "📞 Help":
        bot.send_message(message.chat.id, "🛠 কোনো সমস্যায় অ্যাডমিনের সাথে যোগাযোগ করুন: @SWVRSTD")

    elif message.text == "ℹ️ Info":
        bot.send_message(message.chat.id, "🤖 বট ভার্সন: 2.0 (Stable)\nপ্রিমিয়াম অর্ডারের জন্য আমাদের বটটি ব্যবহার করার জন্য ধন্যবাদ।")

# অর্ডার প্রসেসিং লজিক
def process_order(message):
    user_name = message.from_user.username or message.from_user.first_name
    user_id = message.from_user.id
    link = message.text

    # অ্যাডমিনকে নোটিফিকেশন
    admin_text = (
        f"🔔 **নতুন অর্ডার এসেছে!**\n\n"
        f"👤 ইউজার: @{user_name}\n"
        f"🆔 আইডি: `{user_id}`\n"
        f"🔗 লিংক: {link}"
    )
    bot.send_message(ADMIN_ID, admin_text, parse_mode="Markdown")

    # ইউজারকে কনফার্মেশন
    bot.send_message(
        message.chat.id,
        "✅ আপনার অর্ডারটি সফলভাবে জমা হয়েছে!\nঅ্যাডমিন শীঘ্রই আপনার সাথে যোগাযোগ করবে।",
        reply_markup=get_main_menu()
    )

# ভুল মেসেজ হ্যান্ডেল করা
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "আমি দুঃখিত, আমি বিষয়টি বুঝতে পারছি না। দয়া করে মেনু বাটন ব্যবহার করুন।", reply_markup=get_main_menu())

print("✅ বট সচল হয়েছে...")
bot.polling(none_stop=True)
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
