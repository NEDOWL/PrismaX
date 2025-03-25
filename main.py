import telebot
from telebot import types
import sqlite3
import time
import random

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()

tocen = '8156778620:AAGDqv6M3xzOH75owFRtTGU59EPaz_Mz0II'
bot = telebot.TeleBot(token=tocen)
admin = 2146048678



def db(user_id: int, user_name: str):
    times = time.time()
    admin = 0
    cursor.execute('INSERT INTO user (user_id, user_name, admin, balanse) VALUES (?, ?, ?, ?)', (user_id, user_name, admin, 0))
    cursor.execute('INSERT INTO time (user_id, times) VALUES (?, ?)', (user_id, times))
    print(cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_id,)).fetchone())
    if cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_id,)).fetchone() == [(None,)]:
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (0, user_id))
    conn.commit()
    id_admin = cursor.execute('SELECT user_id FROM user').fetchall()
    id_admin = [i[0] for i in id_admin]
    if user_id in id_admin:
        admin = 1
        cursor.execute('UPDATE user SET admin = ? WHERE user_id = ?', (admin, user_id))
        conn.commit()
    

@bot.message_handler(commands=['start'])
def start(message):
    id = cursor.execute('SELECT user_id FROM user').fetchall()
    id = [i[0] for i in id]
    print(id)
    if message.from_user.id in id:
        menu(message)
    else: 
        bot.send_message(message.chat.id, text= "Hi")
        us_id = message.from_user.id
        us_name = message.from_user.username
        print(us_id, us_name) 
        db(user_id=us_id, user_name=us_name)
        menu(message)

@bot.message_handler(commands=['menu'])
def menu(message):
    print(cursor.execute('SELECT * FROM user').fetchall())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    profile = types.KeyboardButton('Профиль')
    balance = types.KeyboardButton('Пополнить Баланс')
    admin = types.KeyboardButton('Админ')
    shop = types.KeyboardButton('Магазин')
    bir = types.KeyboardButton('Биржа')
    admins = cursor.execute('SELECT admin FROM user WHERE user_id = ?', (int(message.from_user.id),)).fetchall()
    print(admins)
    print(cursor.execute('SELECT * FROM user').fetchall())
    if admins == [(1,)]:
        markup.add(profile, balance, shop, bir, admin)
    else:
        markup.add(profile, balance, shop, bir)
    bot.send_message(message.chat.id, text='Меню', reply_markup=markup)

def profile(message):
    cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,))
    balanse = cursor.fetchone()[0]
    bot.send_message(message.chat.id, text=f'Профиль\nusername: {message.from_user.username}\nid: {message.from_user.id}\nбаланс: {balanse}')

def give_balanse(user_id: int, balanse: int):
    cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse, user_id))
    conn.commit()

def pay(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sto = types.KeyboardButton('100')
    dves = types.KeyboardButton('200')
    tris = types.KeyboardButton('300')
    chet = types.KeyboardButton('400')
    five = types.KeyboardButton('500')
    beck = types.KeyboardButton('Назад')
    markup.add(sto, dves, tris, chet, five, beck)
    bot.send_message(message.chat.id, text='Выберите сумму', reply_markup=markup)

def shop_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rtx_5090 = types.KeyboardButton('RTX 5090')
    rtx_4090 = types.KeyboardButton('RTX 4090')
    rtx_3090_ti = types.KeyboardButton('RTX 3090 TI')
    rtx_3090 = types.KeyboardButton('RTX 3090')
    rtx_3080_ti = types.KeyboardButton('RTX 3080 TI')
    rtx_3080 = types.KeyboardButton('RTX 3080')
    next = types.KeyboardButton('Следующая страница')
    beck = types.KeyboardButton('Назад')
    markup.add(beck, rtx_5090, rtx_4090, rtx_3090_ti, rtx_3090, rtx_3080_ti, rtx_3080, next)
    bot.send_message(message.chat.id, text='Магазин', reply_markup=markup)

def shop_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ice_river = types.KeyboardButton('Ice River AEO')
    gl_shell = types.KeyboardButton('Goldshell AE BOX')
    gl_shell_pro = types.KeyboardButton('Goldshell AE BOX PRO')
    gl_shell_ii = types.KeyboardButton('Goldshell AE BOX II')
    back_1 = types.KeyboardButton('Предыдущая страница')
    beck = types.KeyboardButton('Назад')
    markup.add(beck, ice_river, gl_shell, gl_shell_pro, gl_shell_ii, back_1)
    bot.send_message(message.chat.id, text='Магазин', reply_markup=markup)    

def bir(message):
    timess = cursor.execute('SELECT times FROM time WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    times = time.time()-timess
    if times > 3600:
        btc = random.randint(10000, 20000)
        eth = random.randint(100, 1000)
        ltc = random.randint(10, 1000)
        xrp = random.randint(200, 20000)
        doge = random.randint(1, 100)
        hmstr = random.randint(1, 10)
        cursor.execute('UPDATE time SET times = ? WHERE user_id = ?', (time.time(), message.from_user.id))
        cursor.execute('UPDATE crypto_price SET btc = ?, eth = ?, ltc = ?, xrp = ?, doge = ?, hmstr = ?', (btc, eth, ltc, xrp, doge, hmstr))
        conn.commit()
        print('Курс обновлен')
        print(cursor.execute('SELECT * FROM crypto_price').fetchall())
    else:
        btc = cursor.execute('SELECT btc FROM crypto_price').fetchone()[0]
        eth = cursor.execute('SELECT eth FROM crypto_price').fetchone()[0]
        ltc = cursor.execute('SELECT ltc FROM crypto_price').fetchone()[0]
        xrp = cursor.execute('SELECT xrp FROM crypto_price').fetchone()[0]
        doge = cursor.execute('SELECT doge FROM crypto_price').fetchone()[0]
        hmstr = cursor.execute('SELECT hmstr FROM crypto_price').fetchone()[0]
    marcet = types.InlineKeyboardMarkup()
    sale = types.InlineKeyboardButton(text='Продать монеты', callback_data='sale')
    buy = types.InlineKeyboardButton(text='Купить монеты', callback_data='buy')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    marcet.add(sale, buy, back)
    bot.send_message(message.chat.id, text=f'Добро пожаловать на биржу!\n\nКурс криптовалют:\n btc: {btc}\n eth: {eth}\n ltc: {ltc}\n xrp: {xrp}\n doge: {doge}\n hmstr: {hmstr}\n\n Курс меняется каждый час', reply_markup=marcet)

print('bot is start')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'sale':
        #sale(call.message)
        pass
    elif call.data == 'buy':
        #buy(call.message)
        pass
    elif call.data == 'back':
        #print(cursor.execute('SELECT admin FROM user WHERE user_id = ?', (call.message.from_user.id,)).fetchall())
        menu(call.message)

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Профиль':
        profile(message)
    elif message.text == 'Пополнить Баланс':
        pay(message)
    elif message.text == '100':
        give_balanse(user_id=message.from_user.id, balanse=100+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == '200':
        give_balanse(user_id=message.from_user.id, balanse=200+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == '300':
        give_balanse(user_id=message.from_user.id, balanse=300+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == '400':
        give_balanse(user_id=message.from_user.id, balanse=400+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == '500':
        give_balanse(user_id=message.from_user.id, balanse=500+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == 'Админ':
        if message.from_user.id == admin:
            bot.send_message(message.chat.id, text='Вы админ')
        else:
            pass
    elif message.text == 'Магазин':
        shop_1(message)
    elif message.text == 'Биржа':
        bir(message)
    elif message.text == 'Назад':
        menu(message)
    elif message.text == 'RTX 5090':
        pass
    elif message.text == 'RTX 4090':
        pass
    elif message.text == 'RTX 3090 TI':
        pass
    elif message.text == 'RTX 3090':
        pass
    elif message.text == 'RTX 3080 TI':
        pass
    elif message.text == 'RTX 3080':
        pass
    elif message.text == 'Следующая страница':
        shop_2(message)
    elif message.text == 'Ice River AEO':
        pass
    elif message.text == 'Goldshell AE BOX':
        pass
    elif message.text == 'Goldshell AE BOX PRO':
        pass
    elif message.text == 'Goldshell AE BOX II':
        pass
    elif message.text == 'Предыдущая страница':
        shop_1(message)
    else:
        bot.send_message(message.chat.id, text='Я не понимаю')

def main():
    bot.polling(non_stop=True)

if __name__ == "__main__":
    main()