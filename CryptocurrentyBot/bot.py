import telebot
from telebot import types
from getdata import get_data
from config import config
from loguru import logger
from text import *
from getpass import getuser
from database import Database

bot = telebot.TeleBot(config.TOKEN)
logger.add(f"/home/{getuser()}/.config/bot.log")
logger.debug("Starting bot")

CRYPTOCURRENTYES: list = ["Bitcoin", "Ethereum", "USDT", "BNB", "Solana", "USDC", "XRP", "Dogecoin", "Toncoin", "Cardano", "Notcoin", "Litecoin", "Lifeform"]


@logger.catch
@bot.message_handler(commands=['start'])
def start(message):
    keyboard_lang = types.ReplyKeyboardMarkup()
    ru_btn = types.KeyboardButton("Русский")
    en_btn = types.KeyboardButton("English")
    keyboard_lang.add(ru_btn, en_btn)

    logger.debug(message)

    bot.send_message(message.chat.id, f'Добро пожаловать в Криптовалютного бота, {message.from_user.first_name}', reply_markup=keyboard_lang)


@logger.catch
@bot.message_handler(commands=['menu'])
def menu_g(message):
    lang = Database().get_lang(message.from_user.id)
    if lang == "Русский":
        instruction_for_using_bot = INSTRUCTION_FOR_USING_BOT_RUS
        cryptocurrency_search = CRYPTOCURRENCY_SEARCH_RUS
        menu = MENU_RUS
        go_to_the_stock_exchange = GO_TO_THE_STOCK_EXCHANGE_RUS
    elif lang == "English":
        instruction_for_using_bot = INSTRUCTION_FOR_USING_BOT_ENG
        cryptocurrency_search = CRYPTOCURRENCY_SEARCH_ENG
        menu = MENU_ENG
        go_to_the_stock_exchange = GO_TO_THE_STOCK_EXCHANGE_ENG

    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton(instruction_for_using_bot)
    markup.row(button1)
    button2 = types.KeyboardButton(cryptocurrency_search)
    markup.row(button2)
    button4 = types.KeyboardButton(go_to_the_stock_exchange)
    markup.row(button4)
    bot.send_message(message.chat.id, menu, reply_markup=markup)


@logger.catch
@bot.message_handler(content_types=["text"])
def buttons_and_help(message):
    lang = Database().get_lang(message.from_user.id)
    logger.debug(lang)
    if lang == "Русский":
        instruction = INSTRUCTION_0_RUS
        instruction_1 = INSTRUCTION_1_RUS
        instruction_2 = INSTRUCTION_2_RUS
        instruction_3 = INSTRUCTION_3_RUS
        instruction_4 = INSTRUCTION_4_RUS
        instruction_5 = INSTRUCTION_5_RUS

        instruction_for_using_bot = INSTRUCTION_FOR_USING_BOT_RUS
        cryptocurrency_search = CRYPTOCURRENCY_SEARCH_RUS
        select_one_cryptocurrency_from_the_list = SELECT_ONE_CRYPTOCURRENCY_FROM_THE_LIST_RUS
        menu = MENU_RUS
        go_to_the_stock_exchange = GO_TO_THE_STOCK_EXCHANGE_RUS
        select_one_exchange_from_the_list = SELECT_ONE_EXCHANGE_FROM_THE_LIST_RUS

        current_price: str = CURRENT_PRICE_RUS
    elif lang == "English":
        instruction = INSTRUCTION_0_ENG
        instruction_1 = INSTRUCTION_1_ENG
        instruction_2 = INSTRUCTION_2_ENG
        instruction_3 = INSTRUCTION_3_ENG
        instruction_4 = INSTRUCTION_4_ENG
        instruction_5 = INSTRUCTION_5_ENG

        instruction_for_using_bot = INSTRUCTION_FOR_USING_BOT_ENG
        cryptocurrency_search = CRYPTOCURRENCY_SEARCH_ENG
        select_one_cryptocurrency_from_the_list = SELECT_ONE_CRYPTOCURRENCY_FROM_THE_LIST_ENG
        menu = MENU_ENG
        go_to_the_stock_exchange = GO_TO_THE_STOCK_EXCHANGE_ENG
        select_one_exchange_from_the_list = SELECT_ONE_EXCHANGE_FROM_THE_LIST_ENG

        current_price: str = CURRENT_PRICE_ENG
    else:
        instruction = INSTRUCTION_0_ENG
        instruction_1 = INSTRUCTION_1_ENG
        instruction_2 = INSTRUCTION_2_ENG
        instruction_3 = INSTRUCTION_3_ENG
        instruction_4 = INSTRUCTION_4_ENG
        instruction_5 = INSTRUCTION_5_ENG

        instruction_for_using_bot = INSTRUCTION_FOR_USING_BOT_ENG
        cryptocurrency_search = CRYPTOCURRENCY_SEARCH_ENG
        select_one_cryptocurrency_from_the_list = SELECT_ONE_CRYPTOCURRENCY_FROM_THE_LIST_ENG
        menu = MENU_ENG
        go_to_the_stock_exchange = GO_TO_THE_STOCK_EXCHANGE_ENG
        select_one_exchange_from_the_list = SELECT_ONE_EXCHANGE_FROM_THE_LIST_ENG

        current_price: str = CURRENT_PRICE_ENG

    if message.text == instruction_for_using_bot:
        bot.send_message(message.chat.id, instruction, parse_mode="html")
    elif message.text == '1':
        bot.send_message(message.chat.id, instruction_1, parse_mode="html")
    elif message.text == '2':
        bot.send_message(message.chat.id, instruction_2, parse_mode="html")
    elif message.text == '3':
        bot.send_message(message.chat.id, instruction_3, parse_mode="html")
    elif message.text == '4':
        bot.send_message(message.chat.id, instruction_4, parse_mode="html")
    elif message.text == '5':
        bot.send_message(message.chat.id, instruction_5, parse_mode="html")

    elif message.text == cryptocurrency_search:
        markup = types.ReplyKeyboardMarkup()
        menu = types.KeyboardButton(menu)
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
        cryptocurrency11 = types.KeyboardButton("Notcoin")
        cryptocurrency12 = types.KeyboardButton("Litecoin")
        cryptocurrency13 = types.KeyboardButton("Lifeform")
        markup.row(cryptocurrency6, cryptocurrency7, cryptocurrency8, cryptocurrency9, cryptocurrency10, cryptocurrency11, cryptocurrency12, cryptocurrency13)

        bot.send_message(message.chat.id, select_one_cryptocurrency_from_the_list, reply_markup=markup)

    elif message.text == menu:
        bot.send_message(message.chat.id, "" + menu_g(message))

    elif message.text == CRYPTOCURRENTYES[0]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[0], "bitcoin"))

    elif message.text == CRYPTOCURRENTYES[1]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[1], "ethereum"))

    elif message.text == CRYPTOCURRENTYES[2]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[2], "tether"))

    elif message.text == CRYPTOCURRENTYES[3]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[3], "binancecoin"))

    elif message.text == CRYPTOCURRENTYES[4]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[4], "solana"))

    elif message.text == CRYPTOCURRENTYES[5]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[5], "usd-coin"))

    elif message.text == CRYPTOCURRENTYES[6]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[6], "ripple"))

    elif message.text == CRYPTOCURRENTYES[7]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[7], "dogecoin"))

    elif message.text == CRYPTOCURRENTYES[8]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[8], "the-open-network"))

    elif message.text == CRYPTOCURRENTYES[9]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[9], "cardano"))

    elif message.text == CRYPTOCURRENTYES[10]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[10], "notcoin"))

    elif message.text == CRYPTOCURRENTYES[11]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[11], "litecoin"))

    elif message.text == CRYPTOCURRENTYES[12]:
        bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[12], "lifeform"))

    elif message.text == "Русский":
        db = Database()
        is_user_db = db.check_user(int(message.from_user.id))
        if is_user_db:
            if db.get_lang(message.from_user.id) == "English":
                db.set_lang(message.from_user.id, "Русский")
        else:
            db.set_lang(message.from_user.id, "Русский")

        bot.send_message(message.chat.id, "" + menu_g(message))

    elif message.text == "English":
        db = Database()
        is_user_db = db.check_user(int(message.from_user.id))
        logger.debug(is_user_db)
        if is_user_db:
            if db.get_lang(message.from_user.id) == "Русский":
                db.set_lang(message.from_user.id, "English")
        else:
            db.set_lang(message.from_user.id, "English")

        bot.send_message(message.chat.id, "" + menu_g(message))

    elif message.text == go_to_the_stock_exchange:
        markup = types.InlineKeyboardMarkup()

        button1_exchange = types.InlineKeyboardButton(text="Bybit", url="https://www.bybit.com/ru-RU/")
        button2_exchange = types.InlineKeyboardButton(text='OKX', url="https://okx.com")
        button3_exchange = types.InlineKeyboardButton(text='Binance', url="https://binance.com")
        markup.row(button1_exchange, button2_exchange, button3_exchange)

        button4_exchange = types.InlineKeyboardButton(text='MEXC', url="https://mexc.com")
        button5_exchange = types.InlineKeyboardButton(text='BingX', url="https://bingX.com")
        button6_exchange = types.InlineKeyboardButton(text='KuCoin', url="https://kucoin.com")

        markup.row(button4_exchange, button5_exchange, button6_exchange)
        bot.send_message(message.chat.id, select_one_exchange_from_the_list, reply_markup=markup)
