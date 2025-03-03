import telebot
import webbrowser

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start','main','hello'])
def main(message):
    bot.send_message(message.chat.id,f'Привет,{message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'<b>Help</b> <em><u>information</u></em>',parse_mode='html')

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://classroom.google.com')

@bot.message_handler(content_types=["text"])
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'привет,{message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message,f'ID:{message.from_user.id}')
    elif message.text.lower() == '/start':
        bot.send_message(message.chat.id, f'Привет,{message.from_user.first_name} {message.from_user.last_name}')


bot.polling(non_stop=True)