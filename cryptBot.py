import telebot
from os.path import join
from os import getcwd, getenv
from encryption import encrypt, decrypt
from passwordGenerator import passwordGenerator
from dotenv import load_dotenv

load_dotenv()
TOKEN: str = getenv('TOKEN')
print('TOKEN:', TOKEN)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, 'Привет! Я бот для шифрования данных!')

@bot.message_handler(commands=['gen'])
def generatePasswords(message):
    filepath = join(getcwd(), 'passwords', 'pass' + str(message.date) + '.txt')
    passwordGenerator(16, 20, filepath)
    bot.send_document(chat_id=message.chat.id, data=open(filepath))

@bot.message_handler(content_types=['document'])
def cryptFile(message):
    opt = message.caption.split()

    filepath = join(getcwd(), 'files', 'file' + str(message.date) + '.txt')
    file_info = bot.get_file(message.document.file_id)
    down_file = bot.download_file(file_info.file_path)
    with open(filepath, 'wb') as file:
        file.write(down_file)

    if opt[1] == '1':
        encrypt(filepath, opt[0])
    elif opt[1] == '2':
        decrypt(filepath, opt[0])

    bot.send_document(chat_id=message.chat.id, data=open(filepath))

bot.polling()