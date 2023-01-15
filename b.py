import openai
import telebot
#можете изменить api ключ, но можете оставить этот просто вставив токен бота.
openai.api_key = "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"
bot = telebot.TeleBot("5898589916:AAF4bWmwncJSfW19Q46-f2XgTDlkUVMFIfU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "How can i help you Miss Li?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Tell me about о ' + message.text + '?',
        max_tokens=2048,
        n = 1,
        stop=None,
        temperature=0.5,
    )
    bot.reply_to(message, response["choices"][0]["text"])

bot.polling()
