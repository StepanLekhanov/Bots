import telebot
from telebot import types
from getdata import get_data
from config import config
from loguru import logger
from text import *
from getpass import getuser

bot = telebot.TeleBot(config.TOKEN)
logger.add(f"/home/{getuser()}/.config/bot.log")
logger.debug("Starting bot")

CRYPTOCURRENTYES: list = ["Bitcoin", "Ethereum", "USDT", "BNB", "Solana", "USDC", "XRP", "Dogecoin", "Toncoin", "Cardano"]


@logger.catch
@bot.message_handler(commands=['start'])
def start(message):
    logger.debug(message)
    bot.send_message(message.chat.id, f'Добро пожаловать в Криптовалютного бота, {message.from_user.first_name}')


@logger.catch
@bot.message_handler(commands=['menu'])
def menu_g(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Инструкция по использованию бота')
    markup.row(button1)
    button2 = types.KeyboardButton('Поиск криптовалюты')
    markup.row(button2)
    button3 = types.KeyboardButton('Перейти на TradingView')
    button4 = types.KeyboardButton('Перейти на биржу')
    markup.row(button3, button4)
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


@logger.catch
@bot.message_handler(content_types=["text"])
def buttons_and_help(message):
    # Bot instruction
    if message.text == 'Инструкция по использованию бота':
        bot.send_message(message.chat.id, INSTRUCTION, parse_mode="html")
    elif message.text == '1':
        bot.send_message(message.chat.id, INSTRUCTION_1, parse_mode="html")
    elif message.text == '2':
        bot.send_message(message.chat.id, INSTRUCTION_2, parse_mode="html")
    elif message.text == '3':
        bot.send_message(message.chat.id, INSTRUCTION_3, parse_mode="html")
    elif message.text == '4':
        bot.send_message(message.chat.id, INSTRUCTION_4, parse_mode="html")
    elif message.text == '5':
        bot.send_message(message.chat.id, INSTRUCTION_5, parse_mode="html")

    elif message.text == 'Поиск криптовалюты':
        markup = types.ReplyKeyboardMarkup()
        menu = types.KeyboardButton('Меню')
        markup.row(menu)

        cryptocurrency1 = types.KeyboardButton('Bitcoin')
        cryptocurrency2 = types.KeyboardButton('Ethereum')
        cryptocurrency3 = types.KeyboardButton('USDT')
        cryptocurrency4 = types.KeyboardButton('BNB')
        cryptocurrency5 = types.KeyboardButton('Solana')
        markup.row(cryptocurrency1, cryptocurrency2, cryptocurrency3, cryptocurrency4, cryptocurrency5)

        cryptocurrency6 = types.KeyboardButton('USDC')
        cryptocurrency7 = types.KeyboardButton('XRP')
        cryptocurrency8 = types.KeyboardButton('Dogecoin')
        cryptocurrency9 = types.KeyboardButton('Toncoin')
        cryptocurrency10 = types.KeyboardButton('Cardano')
        markup.row(cryptocurrency6, cryptocurrency7, cryptocurrency8, cryptocurrency9, cryptocurrency10)

        bot.send_message(message.chat.id, 'Выберите одну криптовалюту из списка', reply_markup=markup)

    elif message.text == 'Меню':
        bot.send_message(message.chat.id, menu_g(message))

    elif message.text == CRYPTOCURRENTYES[0]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[0], "bitcoin"))

    elif message.text == CRYPTOCURRENTYES[1]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[1], "ethereum"))

    elif message.text == CRYPTOCURRENTYES[2]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[2], "tether"))

    elif message.text == CRYPTOCURRENTYES[3]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[3], "binancecoin"))

    elif message.text == CRYPTOCURRENTYES[4]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[4], "solana"))

    elif message.text == CRYPTOCURRENTYES[5]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[5], "usd-coin"))

    elif message.text == CRYPTOCURRENTYES[6]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[6], "ripple"))

    elif message.text == CRYPTOCURRENTYES[7]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[7], "dogecoin"))

    elif message.text == CRYPTOCURRENTYES[8]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[8], "the-open-network"))

    elif message.text == CRYPTOCURRENTYES[9]:
        bot.send_message(message.chat.id, get_data(CRYPTOCURRENTYES[9], "cardano"))

    elif message.text == 'Перейти на TradingView':
        bot.send_message(message.chat.id, "Функционал не реализован.")

    elif message.text == 'Перейти на биржу':
        markup = types.InlineKeyboardMarkup()

        button1_exchange = types.InlineKeyboardButton(text="Bybit", url="https://www.bybit.com/ru-RU/")
        button2_exchange = types.InlineKeyboardButton(text='OKX', url="https://okx.com")
        button3_exchange = types.InlineKeyboardButton(text='Binance', url="https://binance.com")
        markup.row(button1_exchange, button2_exchange, button3_exchange)

        button4_exchange = types.InlineKeyboardButton(text='MEXC', url="https://mexc.com")
        button5_exchange = types.InlineKeyboardButton(text='BingX', url="https://bingX.com")
        button6_exchange = types.InlineKeyboardButton(text='KuCoin', url="https://kucoin.com")

        markup.row(button4_exchange, button5_exchange, button6_exchange)
        bot.send_message(message.chat.id, 'Выберите одну биржу из списка: ', reply_markup=markup)
