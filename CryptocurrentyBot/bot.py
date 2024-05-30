from typing import Any
import telebot
from telebot import types
from getdata import get_data
from config import config
from loguru import logger
from text import *
from getpass import getuser
from database import Database
from requests import Response
from time import sleep
import requests
from threading import Thread

bot = telebot.TeleBot(config.TOKEN)
logger.add(f"/home/{getuser()}/.config/bot.log")
logger.debug("Запуск бота")

CRYPTOCURRENTYES: list = ["Bitcoin", "Ethereum", "USDT", "BNB", "Solana", "USDC", "XRP", "Dogecoin", "Toncoin", "Cardano", "Notcoin", "Litecoin", "Lifeform"]
CRYPTOCURRENTYES_API_NAME: list = ["bitcoin", "ethereum", "tether", "binancecoin", "solana", "usd-coin", "ripple", "dogecoin", "the-open-network", "cardano", "notcoin", "litecoin", "lifeform"]


@logger.catch
@bot.message_handler(commands=['start'])
def start(message):
    keyboard_lang: types.ReplyKeyboardMarkup = types.ReplyKeyboardMarkup()
    ru_btn: types.KeyboardButton = types.KeyboardButton("Русский")
    en_btn: types.KeyboardButton = types.KeyboardButton("English")
    keyboard_lang.add(ru_btn, en_btn)

    logger.debug(message)

    bot.send_message(message.chat.id, f'Добро пожаловать в Криптовалютного бота, {message.from_user.first_name}', reply_markup=keyboard_lang)


@logger.catch
@bot.message_handler(commands=['menu'])
def menu_g(message):
    lang: str = Database().get_lang(message.chat.id)
    if lang == "Русский":
        instruction_for_using_bot = INSTRUCTION_FOR_USING_BOT_RUS
        cryptocurrency_search = CRYPTOCURRENCY_SEARCH_RUS
        menu = MENU_RUS
    elif lang == "English":
        instruction_for_using_bot = INSTRUCTION_FOR_USING_BOT_ENG
        cryptocurrency_search = CRYPTOCURRENCY_SEARCH_ENG
        menu = MENU_ENG

    markup: types.ReplyKeyboardMarkup = types.ReplyKeyboardMarkup()
    button1: types.KeyboardButton = types.KeyboardButton(instruction_for_using_bot)
    markup.row(button1)
    button2: types.KeyboardButton = types.KeyboardButton(cryptocurrency_search)
    markup.row(button2)
    bot.send_message(message.chat.id, menu, reply_markup=markup)


@bot.message_handler(commands=["setnotify"])
def setnotify(message):
    try:
        data: list = message.text.split(" ")
        coin: str = data[1]
        price: int = data[2]
        user_id: int = message.from_user.id

        if coin.title() in CRYPTOCURRENTYES:
            logger.debug(f"Монета {coin} существует")

            Database().set_notify(user_id, coin, price)

            bot.send_message(message.chat.id, "Установлено уведомление на {coin}")
        else:
            logger.error("Монеты не существует")

    except IndexError:
        bot.send_message(message.chat.id, "Пример /setnotify [имя монеты] [цена]")


@logger.catch
@bot.message_handler(content_types=["text"])
def buttons_and_help(message):
    lang: str = Database().get_lang(message.from_user.id)

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
        markup: types.ReplyKeyboardMarkup = types.ReplyKeyboardMarkup()
        menu: types.KeyboardButton = types.KeyboardButton(menu)
        markup.row(menu)

        for cryptocurrency in CRYPTOCURRENTYES:
            markup.add(cryptocurrency)

        bot.send_message(message.chat.id, select_one_cryptocurrency_from_the_list, reply_markup=markup)

    elif message.text == menu:
        bot.send_message(message.chat.id, menu_g(message))

    elif message.text == "Русский":
        db = Database()
        is_user_db = db.check_user(int(message.from_user.id))
        if is_user_db:
            if db.get_lang(message.from_user.id) == "English":
                db.set_lang(message.from_user.id, "Русский")
        else:
            db.set_lang(message.from_user.id, "Русский")

        bot.send_message(message.chat.id, menu_g(message))

    elif message.text == "English":
        db = Database()
        is_user_db = db.check_user(int(message.from_user.id))
        logger.debug(is_user_db)
        if is_user_db:
            if db.get_lang(message.from_user.id) == "Русский":
                db.set_lang(message.from_user.id, "English")
        else:
            db.set_lang(message.from_user.id, "English")

        bot.send_message(message.chat.id, menu_g(message))

    # elif message.text == go_to_the_stock_exchange:
    #     markup = types.InlineKeyboardMarkup()
    #
    #     button1_exchange = types.InlineKeyboardButton(text="Bybit", url="https://www.bybit.com/ru-RU/")
    #     button2_exchange = types.InlineKeyboardButton(text='OKX', url="https://okx.com")
    #     button3_exchange = types.InlineKeyboardButton(text='Binance', url="https://binance.com")
    #     markup.row(button1_exchange, button2_exchange, button3_exchange)
    #
    #     button4_exchange = types.InlineKeyboardButton(text='MEXC', url="https://mexc.com")
    #     button5_exchange = types.InlineKeyboardButton(text='BingX', url="https://bingX.com")
    #     button6_exchange = types.InlineKeyboardButton(text='KuCoin', url="https://kucoin.com")
    #
    #     markup.row(button4_exchange, button5_exchange, button6_exchange)
    #     bot.send_message(message.chat.id, select_one_exchange_from_the_list, reply_markup=markup)

    # Вывод цен криптовалют
    for i in range(len(CRYPTOCURRENTYES)):
        if message.text == CRYPTOCURRENTYES[i]:
            bot.send_message(message.chat.id, current_price + " " + get_data(CRYPTOCURRENTYES[i], CRYPTOCURRENTYES_API_NAME[i]))


@logger.catch
def check_price():
    while True:
        logger.debug("Проверка цен криптовалют")
        logger.debug("-"*20)
        for coin in CRYPTOCURRENTYES_API_NAME:
            response: Response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd')
            if response.status_code == 200:
                data: Any = response.json()
                price: float = float(data[f'{coin}']['usd'])
                logger.debug(f"{coin} - ${price}")

                data = Database().get_notify()

                for i in range(len(data)):
                    user_id: str = data[i][0]
                    coin_target: str = data[i][2]
                    price_target: float = float(data[i][3])

                    if price >= price_target and coin == coin_target:
                        logger.debug(f"Уведомление о {coin}:{coin_target} отправлено!")
                        bot.send_message(user_id, f"Цена {coin} достигла ${price_target}!\nТекущая цена: ${price}")

                        # Удаление уведомления т.к оно было отправлено
                        Database().del_notify(user_id, coin_target, price_target)

            else:
                logger.error(f"Ошибка при получении данных о {coin} с coingecko! Status: ({response.status_code}) {response.text}")

            sleep(5)
        logger.debug("-"*20)

        sleep(config.TIMEOUT_CHECK_NOTIFY_USER)


Thread(target=check_price).start()
