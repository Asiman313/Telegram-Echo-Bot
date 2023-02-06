import telebot

bot = telebot.TeleBot(".........")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>Привет! Это Эхо-бот. Я первый проект Асимана по созданию телеграм канала :)</b>", parse_mode="html")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__bot__':
    bot.infinity_polling()

bot.polling(none_stop = True)
