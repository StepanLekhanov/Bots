import telebot
import webbrowser
from telebot import types
import requests

bot = telebot.TeleBot('Твой api-token')

@bot.message_handler(commands='start')
def start(message):
    bot.send_message(message.chat.id, f'Добро пожаловать в Криптовалютного бота, {message.from_user.first_name}')
    
@bot.message_handler(commands=['menu'])
def menu_g(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Инструкция по использованию бота')
    markup.row(button1)
    button2 = types.KeyboardButton('Поиск криптовалюты')
    markup.row(button2)
    button3 = types.KeyboardButton('Перейти на Tradingview')
    button4 = types.KeyboardButton('Выбрать биржу')
    markup.row(button3, button4)
    bot.send_message(message.chat.id,'Главное меню',reply_markup=markup)

@bot.message_handler()
def buttons_and_help(message):
    if message.text == 'Инструкция по использованию бота':
        bot.send_message(message.chat.id,  'Выберите из предложенного списка какой вопрос\n'
                                           'вас интересует. После выбора напишите номер\n'
                                           '(цифру) вопроса, который выбрали:\n'
                                           '\n'
                                           '1. Для чего нужен бот?\n'
                                           '2. Как пользоваться ботом?\n'
                                           '3. Как посмотреть информацию по интересующей\n'
                                           'меня криптовалюте?\n'
                                           '4. Для чего здесь нужен Tradingview и что\n'
                                           'это такое?\n'
                                           '5. Для чего здесь используются биржи?', parse_mode= "html")

    elif message.text == '1':
        bot.send_message(message.chat.id,  'Криптовалютный бот - это бот, с помощью\n' 
                                           'которого вы можете узнать информацию о\n' 
                                           'интересующей вас криптовалюте, далее вы\n' 
                                           'можете открыть график криптовалют,\n' 
                                           'затем перейти на одну из\n' 
                                           'представленных в боте криптобирж для\n'
                                           'покупки/продажи', parse_mode = "html")
    
    elif message.text == '2':
        bot.send_message(message.chat.id,  'Для работы с ботом используются 4 кнопки:\n'
                                           '\n'
                                           '<b>Инструкция по использованию бота</b>,\n'
                                           '<b>Поиск криптовалюты</b>, <b>Перейти на Tradingview</b>,\n'
                                           '<b>Выбрать биржу</b>\n'
                                           '\n'
                                           'При нажатии на кнопку <b>Инструкция по использованию бота</b>\n'
                                           'открывается список вопросов, которые помогут пользователю\n'
                                           'с возникшими трудностями. При нажатии на кнопку\n'
                                           '<b>Поиск криптовалюты</b>откроется список криптовалют,\n'
                                           'среди которых надо выбрать нужную вам. <b>Меню</b>\n'
                                           'позволяет вернуться на главную страницу. Кнопка\n'
                                           '<b>Перейти на Tradingview</b> позволяет перейти на сайт\n'
                                           'для просмотра графика криптовалют. С помощью <b>Выбрать биржу</b>\n'
                                           'можно выбрать 1 биржу из списка, после чего перейти на неё.\n'
                                           '\n'
                                           'В следующих обновлениях будут добавлены новые функции', parse_mode= "html")
    
    elif message.text == '3':
        bot.send_message(message.chat.id, 'Поиск осуществляется посредством выбора необходимой криптовалюты из списка.\n'
                                          'После будет выведена информация о выбранной криптовалюте.\n')
    elif message.text == '4':
        bot.send_message(message.chat.id,  'TradingView — веб-сервис и социальная\n' 
                                           'сеть для трейдеров, в основе которой\n' 
                                           'лежит платформа технического анализа.\n' 
                                           'В бота он был добавлен для того\n'
                                           'чтобы пользователь мог максимально\n'
                                           'быстро попасть на сайт и посмотреть\n' 
                                           'график криптовалюты', parse_mode= "html")

    elif message.text == '5':
        bot.send_message(message.chat.id,  'Биржи были добавлены для того чтобы\n' 
                                           'пользователь мог перейти с помощью\n'
                                           'команды на необходимую биржу.\n' 
                                           'После чего останется зайти в свой аккаунт\n' 
                                           'и можно приступить к торговле', parse_mode= "html")
    
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
        bot.send_message(message.chat.id,'Выберите одну криптовалюту из списка', reply_markup=markup)
    
    elif message.text == 'Меню':
        bot.send_message(message.chat.id, menu_g(message))

    elif message.text == 'Bitcoin':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        data = response.json()
        price = data['bitcoin']['usd']
        bot.send_message(message.chat.id, f'Текущая цена Bitcoin: ${price}')

    elif message.text == 'Ethereum':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
        data = response.json()
        price = data['ethereum']['usd']
        bot.send_message(message.chat.id, f'Текущая цена Ethereum: ${price}')
    
    elif message.text == 'USDT':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd')
        data = response.json()
        price = data['tether']['usd']
        bot.send_message(message.chat.id, f'Текущая цена USDT(Tether): ${price}')

    elif message.text == 'BNB':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd')
        data = response.json()
        price = data['binancecoin']['usd']
        bot.send_message(message.chat.id, f'Текущая цена BNB: ${price}')

    elif message.text == 'Solana':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd')
        data = response.json()
        price = data['solana']['usd']
        bot.send_message(message.chat.id, f'Текущая цена Solana: ${price}')

    elif message.text == 'USDC':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=usd')
        data = response.json()
        price = data['usd-coin']['usd']
        bot.send_message(message.chat.id, f'Текущая цена USDC: ${price}')

    elif message.text == 'XRP':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd')
        data = response.json()
        price = data['ripple']['usd']
        bot.send_message(message.chat.id, f'Текущая цена XRP: ${price}')

    elif message.text == 'Dogecoin':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd')
        data = response.json()
        price = data['dogecoin']['usd']
        bot.send_message(message.chat.id, f'Текущая цена Dogecoin: ${price}')

    elif message.text == 'Toncoin':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd')
        data = response.json()
        price = data['the-open-network']['usd']
        bot.send_message(message.chat.id, f'Текущая цена Toncoin: ${price}')

    elif message.text == 'Cardano':
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd')
        data = response.json()
        price = data['cardano']['usd']
        bot.send_message(message.chat.id, f'Текущая цена Cardano: ${price}')

    elif message.text == 'Перейти на Tradingview':
        webbrowser.open('https://tradingview.com')

    elif message.text == 'Выбрать биржу':
        markup = types.ReplyKeyboardMarkup()
        menu = types.KeyboardButton('Меню')
        markup.row(menu)
        button1_exchange = types.KeyboardButton('Bybit')
        button2_exchange = types.KeyboardButton('OKX')
        button3_exchange = types.KeyboardButton('Binance')
        markup.row(button1_exchange, button2_exchange, button3_exchange)
        button4_exchange = types.KeyboardButton('MEXC')
        button5_exchange = types.KeyboardButton('BingX')
        button6_exchange = types.KeyboardButton('KuCoin')
        markup.row(button4_exchange, button5_exchange, button6_exchange)
        bot.send_message(message.chat.id,'Выберите одну биржу из списка', reply_markup=markup)

    elif message.text == 'Bybit':
        webbrowser.open('https://bybit.com')

    elif message.text == 'OKX':
        webbrowser.open('https://okx.com')

    elif message.text == 'Binance':
        webbrowser.open('https://binance.com')

    elif message.text == 'MEXC':
        webbrowser.open('https://mexc.com') 

    elif message.text == 'BingX':
        webbrowser.open('https://bingX.com')

    elif message.text == 'KuCoin':
        webbrowser.open('https://kucoin.com')              

if __name__ == '__main__':
    bot.polling(non_stop=True)