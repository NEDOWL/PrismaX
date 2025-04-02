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



def db(user_id: int, user_name: str, message):
    btc = random.randint(10000, 20000)
    eth = random.randint(100, 1000)
    ltc = random.randint(10, 1000)
    xrp = random.randint(200, 20000)
    doge = random.randint(1, 100)
    hmstr = random.randint(1, 10)
    times = time.time()
    admin = 0
    ref_cod = random.randint(100000, 999999)
    ref_cods = cursor.execute('SELECT ref_cod FROM user').fetchone()
    #for i in ref_cods:
    #    if i == ref_cod:
    #        ref_cod = random.randint(1000000, 9999999)
    print("ref", ref_cods)
    print(message.from_user.id)
    cursor.execute('INSERT INTO card (user_id, rtx_5090, rtx_4090, rtx_3090_ti, rtx_3090, rtx_3080_ti, rtx_3080, ice_river_aeo, goldshell_ae_box, goldshell_ae_box_pro, goldshell_ae_box_ii, gtx_1080_ti) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    cursor.execute('INSERT INTO crypto_price (btc, eth, ltc, xrp, doge, hmstr) VALUES (?, ?, ?, ?, ?, ?)', (btc, eth, ltc, xrp, doge, hmstr))
    cursor.execute('INSERT INTO crypto (user_id, btc, eth, ltc, xrp, doge, hmstr) VALUES (?, ?, ?, ?, ?, ?, ?)', (user_id, 0, 0, 0, 0, 0, 0))
    cursor.execute('INSERT INTO user (user_id, user_name, admin, balanse, time_income, mining, start_pack, ref_cod, ref_count) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, user_name, admin, 0, times, 'BTC', 0, ref_cod, 0))
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
    
def ref_new(message, ref_cod):
    ref_cods = cursor.execute('SELECT ref_cod FROM user')


@bot.message_handler(commands=['start'])
def start(message):
    id = cursor.execute('SELECT user_id FROM user').fetchall()
    id = [i[0] for i in id]
    print(id)
    if message.from_user.id in id:
        menu(message)
    else:
        us_id = message.from_user.id
        us_name = message.from_user.username
        print(us_id, us_name) 
        db(user_id=us_id, user_name=us_name, message=message)
        menu(message)
        ref_cod = message.text[7:]
        ref_new(message, ref_cod)

@bot.message_handler(commands=['menu'])
def menu(message):
    print(cursor.execute('SELECT * FROM user').fetchall())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    profile = types.KeyboardButton('Профиль')
    balance = types.KeyboardButton('Пополнить Баланс')
    admin = types.KeyboardButton('Админ')
    shop_common = types.KeyboardButton('Магазин')
    shop = types.KeyboardButton('Премиум магазин')
    bir = types.KeyboardButton('Биржа')
    admins = cursor.execute('SELECT admin FROM user WHERE user_id = ?', (int(message.from_user.id),)).fetchall()
    print(admins)
    print(cursor.execute('SELECT * FROM user').fetchall())
    if admins == [(1,)]:
        markup.add(profile, balance, shop_common, shop, bir, admin)
    else:
        markup.add(profile, balance, shop_common, shop, bir)
    bot.send_message(message.chat.id, text='Меню\n\n version:beta 0.4.3', reply_markup=markup)

def profile(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    change_mine_crime = types.KeyboardButton(text='Выбор криптовалюты')
    start_pack = types.KeyboardButton(text='Забрать стартовый пакет')
    ref = types.KeyboardButton(text= 'Рефер. прог.')
    back = types.KeyboardButton(text='Назад')
    if cursor.execute('SELECT start_pack FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] == 0:
        markup.add(change_mine_crime, start_pack, ref, back)
    else:
        markup.add(change_mine_crime, ref, back)
    ming = cursor.execute('SELECT mining FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    global bal
    bal = 0
    income = 0
    cursor.execute('SELECT rtx_5090, rtx_4090, rtx_3090_ti, rtx_3090, rtx_3080_ti, rtx_3080, ice_river_aeo, goldshell_ae_box, goldshell_ae_box_pro, goldshell_ae_box_ii, gtx_1080_ti FROM card')
    for i in cursor.fetchall():
        for j in i:
            income += j
        print(income)
    times = cursor.execute('SELECT time_income FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    times = time.time()-times
    print(round(times, 0))
    if times >= 1:
        bal = round(income * (times/3600/24/30), 3)
        print(bal)
    cursor.execute('UPDATE user SET time_income = ? WHERE user_id = ?', (time.time(), message.from_user.id))
    cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,))
    balanse = round(cursor.fetchone()[0], 3)
    print(balanse)
    cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse, message.from_user.id))
    conn.commit()
    balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    
    btc = round(float(f'{cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}'), 8)
    print(f'{btc:.10f}')
    eth = float(f'{cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}')
    ltc = float(f'{cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}')
    xrp = float(f'{cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}')
    doge = float(f'{cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}')
    hmstr = float(f'{cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}')
    if btc < 0.00000001:
        btc = 0
    if eth < 0.00000001:
        eth = 0
    if ltc < 0.00000001:
        ltc = 0
    if xrp < 0.00000001:
        xrp = 0
    if doge < 0.00000001:
        doge = 0
    if hmstr < 0.00000001:
        hmstr = 0
    bot.send_message(message.chat.id, text=f'Профиль\nusername: {message.from_user.username}\nid: {message.from_user.id}\nбаланс: {balanse}\n\nКриптовалюты:\nbtc: {btc:.8f}\neth: {eth:.8f}\nltc: {ltc:.8f}\nxrp: {xrp:.8f}\ndoge: {doge:.8f}\nhmstr: {hmstr:.8f}\n\n Крипта которую вы майните: {ming}\n\nОбщий доход:\n{income} руб/мес\n{(income/30):.3f} руб/день\n{(income/30/24):.3f} руб/час', reply_markup=markup)
    #bot.send_message(message.chat.id, text=f'Профиль\nusername: {message.from_user.username}\nid: {message.from_user.id}\nбаланс: {balanse}')
    wallets(message)
    print(cursor.execute('SELECT * FROM card').fetchall())

def wallets(message):
    print(cursor.execute('SELECT * FROM crypto_price').fetchall())
    global bal
    mine = cursor.execute('SELECT mining FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    if mine == 'BTC':
        if (cursor.execute('SELECT btc FROM crypto_price').fetchone()[0]) == 0:
            btcs = 0
        else:
            btcs = round(bal / (cursor.execute('SELECT btc FROM crypto_price').fetchone()[0]), 8)
            btcs = round(float(f'{btcs:.10f}'), 8)
            btcs_old = cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE crypto SET btc = ? WHERE user_id = ?', (btcs + btcs_old, message.from_user.id))
            conn.commit()
            print(btcs)
    elif mine == 'ETH':
        if (cursor.execute('SELECT eth FROM crypto_price').fetchone()[0]) == 0:
            eths = 0
        else:
            eths = round(bal / (cursor.execute('SELECT eth FROM crypto_price').fetchone()[0]), 8)
            eths = round(float(f'{eths:.10f}'), 8)
            eths_old = cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE crypto SET eth = ? WHERE user_id = ?', (eths + eths_old, message.from_user.id))
            conn.commit()
    elif mine == 'LTC':
        if (cursor.execute('SELECT ltc FROM crypto_price').fetchone()[0]) == 0:
            ltcs = 0
        else:
            ltcs = round(bal / (cursor.execute('SELECT ltc FROM crypto_price').fetchone()[0]), 8)
            ltcs = round(float(f'{ltcs:.10f}'), 8)
            ltcs_old = cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE crypto SET ltc = ? WHERE user_id = ?', (ltcs + ltcs_old, message.from_user.id))
            conn.commit()
    elif mine == 'XRP':
        if (cursor.execute('SELECT xrp FROM crypto_price').fetchone()[0]) == 0:
            xrps = 0
        else:
            xrps = round(bal / (cursor.execute('SELECT xrp FROM crypto_price').fetchone()[0]), 8)
            xrps = round(float(f'{xrps:.10f}'), 8)
            xrps_old = cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE crypto SET xrp = ? WHERE user_id = ?', (xrps + xrps_old, message.from_user.id))
            conn.commit()
    elif mine == 'DOGE':
        if (cursor.execute('SELECT doge FROM crypto_price').fetchone()[0]) == 0:
            doges = 0
        else:
            doges = round(bal / (cursor.execute('SELECT doge FROM crypto_price').fetchone()[0]), 8)
            doges = round(float(f'{doges:.10f}'), 8)
            doges_old = cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE crypto SET doge = ? WHERE user_id = ?', (doges + doges_old, message.from_user.id))
            conn.commit()
    elif mine == 'HMSTR':
        if (cursor.execute('SELECT hmstr FROM crypto_price').fetchone()[0]) == 0:
            hmstrs = 0
        else:
            hmstrs = round(bal / (cursor.execute('SELECT hmstr FROM crypto_price').fetchone()[0]), 8)
            hmstrs = round(float(f'{hmstrs:.10f}'), 8)
            hmstrs_old = cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE crypto SET hmstr = ? WHERE user_id = ?', (hmstrs + hmstrs_old, message.from_user.id))
            conn.commit()

#def wallet(message):
 #   wallets(message)
  #  cursor.execute('SELECT btc, eth, ltc, xrp, doge, hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,))
   # wallet = cursor.fetchone()
    #print(wallet)
    #bot.send_message(message.chat.id, text=f'Кошелек\nbtc: {wallet[0]}\neth: {wallet[1]}\nltc: {wallet[2]}\nxrp: {wallet[3]}\ndoge: {wallet[4]}\nhmstr: {wallet[5]}')
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

def shop_common(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    gtx_1080_ti = types.KeyboardButton('GTX 1080 TI')
    gtx_1080 = types.KeyboardButton('GTX 1080')
    gtx_2060 = types.KeyboardButton('GTX 2060')
    gtx_2070 = types.KeyboardButton('GTX 2070')
    gtx_2080 = types.KeyboardButton('GTX 2080')
    gtx_2080_ti = types.KeyboardButton('GTX 2080 TI')
    rtx_3060 = types.KeyboardButton('RTX 3060')
    rtx_3060_ti = types.KeyboardButton('RTX 3060 TI')
    rtx_3070 = types.KeyboardButton('RTX 3070')
    rtx_3070_ti = types.KeyboardButton('RTX 3070 TI')
    next = types.KeyboardButton('Следующая страница')
    beck = types.KeyboardButton('Назад')
    markup.add(gtx_1080_ti, gtx_1080, gtx_2060, gtx_2070, gtx_2080, gtx_2080_ti, rtx_3060, rtx_3060_ti, rtx_3070, rtx_3070_ti, beck, next)
    bot.send_message(message.chat.id, text='Магазин', reply_markup=markup)

def gtx_1080_ti(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_1080_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали карту GTX 1080 TI\n\nХарактеристики и ее стоимость:\n доход: 100 руб/мес\n стоимость: 200руб\n\nОкупаемость: 2 месяцев', reply_markup=markup)

def buy_1080_ti(call, user_ids):
    result = cursor.execute('SELECT balance FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    
    balanses = result[0]
    income = cursor.execute('SELECT gtx_1080_ti FROM card_common WHERE user_id = ?', (user_ids)).fetchone()[0]
    if balanses >= 200:
        cursor.execute('UPDATE card_common SET gtx_1080_ti = ? WHERE user_id = ?', (income + 100, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 200)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили GTX 1080TI')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')



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
    markup.add(rtx_5090, rtx_4090, rtx_3090_ti, rtx_3090, rtx_3080_ti, rtx_3080, beck, next)
    bot.send_message(message.chat.id, text='Магазин', reply_markup=markup)

def shop_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ice_river = types.KeyboardButton('Ice River AEO')
    gl_shell = types.KeyboardButton('Goldshell AE BOX')
    gl_shell_pro = types.KeyboardButton('Goldshell AE BOX PRO')
    gl_shell_ii = types.KeyboardButton('Goldshell AE BOX II')
    back_1 = types.KeyboardButton('Предыдущая страница')
    beck = types.KeyboardButton('Назад')
    markup.add(ice_river, gl_shell, gl_shell_pro, gl_shell_ii, beck, back_1)
    bot.send_message(message.chat.id, text='Магазин', reply_markup=markup) 

def rtx_5090(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_5090')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали карту RTX 5090\n\nХарактеристики и ее стоимость:\n доход: 788 руб/мес\n стоимость: 10000руб\n\nОкупаемость: 12 месяцев', reply_markup=markup)

def buy_5090(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return

    balanses = result[0]
    income = cursor.execute('SELECT rtx_5090 FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 10000:
        cursor.execute('UPDATE card SET rtx_5090 = ? WHERE user_id = ?', (income + 788, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 10000)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили RTX 5090')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def rtx_4090(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_4090')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали карту RTX 4090\n\nХарактеристики и ее стоимость:\n доход: 483 руб/мес\n стоимость: 8000руб\n\nОкупаемость: 15 месяцев', reply_markup=markup)

def buy_4090(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_4090 FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 8000:
        cursor.execute('UPDATE card SET rtx_4090 = ? WHERE user_id = ?', (income + 788, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 8000)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили RTX 4090')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def rtx_3090_ti(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3090_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали карту RTX 3090 TI\n\nХарактеристики и ее стоимость:\n доход: 330 руб/мес\n стоимость: 6000руб\n\nОкупаемость: 18 месяцев', reply_markup=markup)

def buy_3090_ti(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3090_ti FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 6000:
        cursor.execute('UPDATE card SET rtx_3090_ti = ? WHERE user_id = ?', (income + 330, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 6000)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили RTX 3090 TI')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def rtx_3090(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3090')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали карту RTX 3090\n\nХарактеристики и ее стоимость:\n доход: 300 руб/мес\n стоимость: 5500руб\n\nОкупаемость: 15 месяцев', reply_markup=markup)

def buy_3090(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3090 FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 5500:
        cursor.execute('UPDATE card SET rtx_3090 = ? WHERE user_id = ?', (income + 300, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 5500)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили RTX 3090')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def rtx_3080_ti(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3080_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали карту RTX 3080 TI\n\nХарактеристики и ее стоимость:\n доход: 250 руб/мес\n стоимость: 3000руб\n\nОкупаемость: 12 месяцев', reply_markup=markup)

def buy_3080_ti(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3080_ti FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 3000:
        cursor.execute('UPDATE card SET rtx_3080_ti = ? WHERE user_id = ?', (income + 250, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 3000)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили RTX 3080 TI')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def rtx_3080(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3080')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали карту RTX 3080\n\nХарактеристики и ее стоимость:\n доход: 220 руб/мес\n стоимость: 2500руб\n\nОкупаемость: 10 месяцев', reply_markup=markup)

def buy_3080(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3080 FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 2500:
        cursor.execute('UPDATE card SET rtx_3080 = ? WHERE user_id = ?', (income + 220, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 2500)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили RTX 3080')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def iraeo(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_iraeo')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали Ice River AEO\n\nХарактеристики и ее стоимость:\n доход: 5000 руб/мес\n стоимость: 50000руб\n\nОкупаемость: 10 месяцев', reply_markup=markup)

def buy_iraeo(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT ice_river_aeo FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 50000:
        cursor.execute('UPDATE card SET ice_river_aeo = ? WHERE user_id = ?', (income + 5000, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 50000)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили Ice River AEO')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def goldshell_ae_box(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_goldshell_ae_box')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали Goldshell AE BOX\n\nХарактеристики и ее стоимость:\n доход: 3000 руб/мес\n стоимость: 35000руб\n\nОкупаемость: 11 месяцев', reply_markup=markup)

def buy_goldshell_ae_box(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT goldshell_ae_box FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 35000:
        cursor.execute('UPDATE card SET goldshell_ae_box = ? WHERE user_id = ?', (income + 3000, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 35000)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили Goldshell AE BOX')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def goldshell_ae_box_pro(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_goldshell_ae_box_pro')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали Goldshell AE BOX PRO\n\nХарактеристики и ее стоимость:\n доход: 2000 руб/мес\n стоимость: 15000руб\n\nОкупаемость: 11 месяцев', reply_markup=markup)

def buy_goldshell_ae_box_pro(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT goldshell_ae_box_pro FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 15000:
        cursor.execute('UPDATE card SET goldshell_ae_box_pro = ? WHERE user_id = ?', (income + 2000, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 15000)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили Goldshell AE BOX PRO')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

def goldshell_ae_box_ii(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_goldshell_ae_box_ii')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(message.chat.id, text='Вы выбрали Goldshell AE BOX II\n\nХарактеристики и ее стоимость:\n доход: 1500 руб/мес\n стоимость: 10000руб\n\nОкупаемость: 11 месяцев', reply_markup=markup)

def buy_goldshell_ae_box_ii(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT goldshell_ae_box_ii FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 10000:
        cursor.execute('UPDATE card SET goldshell_ae_box_ii = ? WHERE user_id = ?', (income + 1500, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse=balanses - 10000)
        bot.send_message(call.chat.id, text='Поздравляю, вы купили Goldshell AE BOX II')
    else:
        bot.send_message(call.chat.id, text='У вас недостаточно средств')

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
        cursor.execute('UPDATE time SET times = ? WHERE user_id = ?', (times, message.from_user.id))
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
    bot.send_message(message.chat.id, text=f'Добро пожаловать на биржу!\n\nКурс криптовалют:\n btc: {btc} руб/ед\n eth: {eth} руб/ед\n ltc: {ltc} руб/ед\n xrp: {xrp} руб/ед\n doge: {doge} руб/ед\n hmstr: {hmstr} руб/ед\n\n Курс меняется каждый час', reply_markup=marcet)

def sale(message):
    markup = types.InlineKeyboardMarkup()
    btc = types.InlineKeyboardButton(text='BTC', callback_data='btc')
    eth = types.InlineKeyboardButton(text='ETH', callback_data='eth')
    ltc = types.InlineKeyboardButton(text='LTC', callback_data='ltc')
    xrp = types.InlineKeyboardButton(text='XRP', callback_data='xrp')
    doge = types.InlineKeyboardButton(text='DOGE', callback_data='doge')
    hmstr = types.InlineKeyboardButton(text='HMSTR', callback_data='hmstr')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(btc, eth, ltc, xrp, doge, hmstr, back)
    bot.send_message(message.chat.id, text='Выберите криптовалюту для продажи', reply_markup=markup)

def sale_btc(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sell = types.KeyboardButton('Продать')
    back = types.KeyboardButton('Назад')
    markup.add(sell, back)
    cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (user_ids,))
    btc = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество BTC для продажи\nВаш баланс BTC: {btc:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_btc_1)

def sale_btc_1(message):
    try:
        btc = float(message.text)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        btc_price = cursor.execute('SELECT btc FROM crypto_price').fetchone()[0]
        if btc <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if btc > cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно BTC')
            return
        cursor.execute('UPDATE crypto SET btc = ? WHERE user_id = ?', (cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - btc, message.from_user.id))
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse + btc * btc_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(message.chat.id, text=f'Вы успешно продали {btc} BTC\nНа ваш баланс зачислено {round(btc * btc_price, 3)} руб\nВаш баланс: {round(new_balanse, 3)} руб')
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')

def sale_eth(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sell = types.KeyboardButton('Продать')
    back = types.KeyboardButton('Назад')
    markup.add(sell, back)
    cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (user_ids,))
    eth = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество ETH для продажи\nВаш баланс ETH: {eth:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_eth_1)

def sale_eth_1(message):
    try:
        eth = float(message.text)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        eth_price = cursor.execute('SELECT eth FROM crypto_price').fetchone()[0]
        if eth <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if eth > cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно ETH')
            return
        cursor.execute('UPDATE crypto SET eth = ? WHERE user_id = ?', (cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - eth, message.from_user.id))
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse + eth * eth_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(message.chat.id, text=f'Вы успешно продали {eth} ETH\nНа ваш баланс зачислено {round(eth * eth_price, 3)} руб\nВаш баланс: {round(new_balanse, 3)} руб')
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')

def sale_ltc(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sell = types.KeyboardButton('Продать')
    back = types.KeyboardButton('Назад')
    markup.add(sell, back)
    cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (user_ids,))
    ltc = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество LTC для продажи\nВаш баланс LTC: {ltc:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_ltc_1)

def sale_ltc_1(message):
    try:
        ltc = float(message.text)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        ltc_price = cursor.execute('SELECT ltc FROM crypto_price').fetchone()[0]
        if ltc <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if ltc > cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно LTC')
            return
        cursor.execute('UPDATE crypto SET ltc = ? WHERE user_id = ?', (cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - ltc, message.from_user.id))
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse + ltc * ltc_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(message.chat.id, text=f'Вы успешно продали {ltc} LTC\nНа ваш баланс зачислено {round(ltc * ltc_price, 3)} руб\nВаш баланс: {round(new_balanse, 3)} руб')
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')

def sale_xrp(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sell = types.KeyboardButton('Продать')
    back = types.KeyboardButton('Назад')
    markup.add(sell, back)
    cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (user_ids,))
    xrp = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество XRP для продажи\nВаш баланс XRP: {xrp:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_xrp_1)

def sale_xrp_1(message):
    try:
        xrp = float(message.text)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        xrp_price = cursor.execute('SELECT xrp FROM crypto_price').fetchone()[0]
        if xrp <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if xrp > cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно XRP')
            return
        cursor.execute('UPDATE crypto SET xrp = ? WHERE user_id = ?', (cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - xrp, message.from_user.id))
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse + xrp * xrp_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(message.chat.id, text=f'Вы успешно продали {xrp} XRP\nНа ваш баланс зачислено {round(xrp * xrp_price, 3)} руб\nВаш баланс: {round(new_balanse, 3)} руб')
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')

def sale_doge(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sell = types.KeyboardButton('Продать')
    back = types.KeyboardButton('Назад')
    markup.add(sell, back)
    cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (user_ids,))
    doge = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество DOGE для продажи\nВаш баланс DOGE: {doge:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_doge_1)

def sale_doge_1(message):
    try:
        doge = float(message.text)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        doge_price = cursor.execute('SELECT doge FROM crypto_price').fetchone()[0]
        if doge <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if doge > cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно DOGE')
            return
        cursor.execute('UPDATE crypto SET doge = ? WHERE user_id = ?', (cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - doge, message.from_user.id))
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse + doge * doge_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(message.chat.id, text=f'Вы успешно продали {doge} DOGE\nНа ваш баланс зачислено {round(doge * doge_price, 3)} руб\nВаш баланс: {round(new_balanse, 3)} руб')
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')

def sale_hmstr(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sell = types.KeyboardButton('Продать')
    back = types.KeyboardButton('Назад')
    markup.add(sell, back)
    cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (user_ids,))
    hmstr = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество HMSTR для продажи\nВаш баланс HMSTR: {hmstr:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_hmstr_1)

def sale_hmstr_1(message):
    try:
        hmstr = float(message.text)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        hmstr_price = cursor.execute('SELECT hmstr FROM crypto_price').fetchone()[0]
        if hmstr <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if hmstr > cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно HMSTR')
            return
        cursor.execute('UPDATE crypto SET hmstr = ? WHERE user_id = ?', (cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - hmstr, message.from_user.id))
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse + hmstr * hmstr_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(message.chat.id, text=f'Вы успешно продали {hmstr} HMSTR\nНа ваш баланс зачислено {round(hmstr * hmstr_price, 3)} руб\nВаш баланс: {round(new_balanse, 3)} руб')
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')

def change_mine_crime(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btc = types.KeyboardButton('BTC')
    eth = types.KeyboardButton('ETH')
    ltc = types.KeyboardButton('LTC')
    xrp = types.KeyboardButton('XRP')
    doge = types.KeyboardButton('DOGE')
    hmstr = types.KeyboardButton('HMSTR')
    back = types.KeyboardButton('Назад')
    markup.add(btc, eth, ltc, xrp, doge, hmstr, back)
    bot.send_message(message.chat.id, text='Выберите криптовалюту для майнинга(по умолчанию BTC)', reply_markup=markup)
    
def admin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    search_user = types.KeyboardButton('Поиск пользователя')
    markup.add(search_user, back)
    bot.send_message(message.chat.id, text='Админ панель', reply_markup=markup)

def search_users(message):
    id = bot.send_message(message.chat.id, text='Введите ID пользователя')
    bot.register_next_step_handler(id, search_user)

def search_user(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    add_balanse = types.KeyboardButton('Добавить баланс')
    remove_balanse = types.KeyboardButton('Убрать баланс')
    back = types.KeyboardButton('Назад')
    markup.add(add_balanse, remove_balanse, back)
    user_id = message.text
    cursor.execute('SELECT * FROM user WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    if user is None:
        bot.send_message(message.chat.id, text='Пользователь не найден')
    else:
        bot.send_message(message.chat.id, text=f'ID: {user[0]}\nusername: {user[1]}\nadmin: {user[2]}\nbalanse: {user[3]}\ntime_income: {user[4]}', reply_markup=markup)

def add_balanse(message):
    id = bot.send_message(message.chat.id, text='Введите ID пользователя')
    bot.register_next_step_handler(id, add_balanse_1)

def add_balanse_1(message):
    global user_id
    user_id = message.text
    balanse = bot.send_message(message.chat.id, text='Введите сумму')
    bot.register_next_step_handler(balanse, add_balanse_2)

def add_balanse_2(message):
    global user_id
    user_ids = user_id
    balanse = int(message.text)
    cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,))
    balanse_1 = cursor.fetchone()
    if balanse_1 is None:
        bot.send_message(message.chat.id, text='Пользователь не найден')
    else:
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse_1[0] + balanse, user_id))
        conn.commit()
        bot.send_message(message.chat.id, text='Баланс успешно добавлен')

def start_pack(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton('Начать')
    markup.add(start)
    bot.send_message(message.chat.id, text='Добро пожаловать в игру\n\n Нажмите "Начать" чтобы начать зарабатывать реальные деньги)', reply_markup=markup)

def start_pack_1(message):
    cursor.execute('UPDATE user SET start_pack = ? WHERE user_id = ?', (1, message.from_user.id))
    conn.commit()
    cursor.execute('UPDATE card SET gtx_1080_ti = ? WHERE user_id = ?', (100, message.from_user.id))
    conn.commit()
    bot.send_message(message.chat.id, text='Вы успешно начали игру')
    profile(message)
print('bot is start')

def referal(message):
    ref_cod = cursor.execute('SELECT ref_cod FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    bot.send_message(message.chat.id, text=f'Ваша реферальная ссылка https://t.me/Ai_asistent_my_bot?start={ref_cod}')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_ids = call.from_user.id  # Используем call.from_user.id для получения ID пользователя
    print(f"Callback from user ID: {user_ids}")
    if call.data == 'sale':
        sale(call.message)
    elif call.data == 'buy':
        #buy(call.message)
        pass
    elif call.data == 'back':
        #print(cursor.execute('SELECT admin FROM user WHERE user_id = ?', (call.message.from_user.id,)).fetchall())
        menu(call.message)
    elif call.data == 'buy_5090':
        buy_5090(call.message, user_ids)
    elif call.data == 'buy_4090':
        buy_4090(call.message, user_ids)
    elif call.data == 'buy_3090_ti':
        buy_3090_ti(call.message, user_ids)
    elif call.data == 'buy_3090':
        buy_3090(call.message, user_ids)
    elif call.data == 'buy_3080_ti':
        buy_3080_ti(call.message, user_ids)
    elif call.data == 'buy_3080':
        buy_3080(call.message, user_ids)
    elif call.data == 'buy_iraeo':
        buy_iraeo(call.message, user_ids)
    elif call.data == 'buy_goldshell_ae_box':
        buy_goldshell_ae_box(call.message, user_ids)
    elif call.data == 'buy_goldshell_ae_box_pro':
        buy_goldshell_ae_box_pro(call.message, user_ids)
    elif call.data == 'buy_goldshell_ae_box_ii':
        buy_goldshell_ae_box_ii(call.message, user_ids)
    elif call.data == 'btc':
        sale_btc(call.message, user_ids)
    elif call.data == 'eth':
        sale_eth(call.message, user_ids)
    elif call.data == 'ltc':
        sale_ltc(call.message, user_ids)
    elif call.data == 'xrp':
        sale_xrp(call.message, user_ids)
    elif call.data == 'doge':
        sale_doge(call.message, user_ids)
    elif call.data == 'hmstr':
        sale_hmstr(call.message, user_ids)
    else:
        pass

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Профиль':
        profile(message)
    elif message.text == 'Пополнить Баланс':
        pay(message)
    elif message.text == '100':
        bot.send_message(message.chat.id, text='Вы пополнили баланс на 100')
        give_balanse(user_id=message.from_user.id, balanse=100+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == '200':
        bot.send_message(message.chat.id, text='Вы пополнили баланс на 200')
        give_balanse(user_id=message.from_user.id, balanse=200+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == '300':
        bot.send_message(message.chat.id, text='Вы пополнили баланс на 300')
        give_balanse(user_id=message.from_user.id, balanse=300+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == '400':
        bot.send_message(message.chat.id, text='Вы пополнили баланс на 400')
        give_balanse(user_id=message.from_user.id, balanse=400+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == '500':
        bot.send_message(message.chat.id, text='Вы пополнили баланс на 500')
        give_balanse(user_id=message.from_user.id, balanse=500+cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
        menu(message)
    elif message.text == 'Админ':
        admin(message)
    elif message.text == 'Премиум магазин':
        shop_1(message)
    elif message.text == 'Биржа':
        bir(message)
    elif message.text == 'Назад':
        menu(message)
    elif message.text == 'RTX 5090':
        rtx_5090(message)
    elif message.text == 'RTX 4090':
        rtx_4090(message)
    elif message.text == 'RTX 3090 TI':
        rtx_3090_ti(message)
    elif message.text == 'RTX 3090':
        rtx_3090(message)
    elif message.text == 'RTX 3080 TI':
        rtx_3080_ti(message)
    elif message.text == 'RTX 3080':
        rtx_3080(message)
    elif message.text == 'Следующая страница':
        shop_2(message)
    elif message.text == 'Ice River AEO':
        iraeo(message)
    elif message.text == 'Goldshell AE BOX':
        goldshell_ae_box(message)
    elif message.text == 'Goldshell AE BOX PRO':
        goldshell_ae_box_pro(message)
    elif message.text == 'Goldshell AE BOX II':
        goldshell_ae_box_ii(message)
    elif message.text == 'Предыдущая страница':
        shop_1(message)
    elif message.text == 'Поиск пользователя':
        search_users(message)
    elif message.text == 'Добавить баланс':
        add_balanse(message)
    elif message.text == 'Убрать баланс':
        remove_balanse(message)
    elif message.text == 'BTC':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('BTC', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг BTC')
        profile(message)
    elif message.text == 'ETH':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('ETH', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг ETH')
        profile(message)
    elif message.text == 'LTC':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('LTC', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг LTC')
        profile(message)
    elif message.text == 'XRP':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('XRP', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг XRP')
        profile(message)
    elif message.text == 'DOGE':    
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('DOGE', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг DOGE')
        profile(message)
    elif message.text == 'HMSTR':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('HMSTR', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг HMSTR')
        profile(message)
    elif message.text == 'Выбор криптовалюты':
        change_mine_crime(message)
    elif message.text == 'Забрать стартовый пакет':
        start_pack(message)
    elif message.text == 'Начать':
        start_pack_1(message)
    elif message.text == 'Магазин':
        shop_common(message)
    elif message.text == 'Рефер. прог.':
        referal(message)
    else:
        bot.send_message(message.chat.id, text='Я не понимаю')

def main():
    bot.polling(non_stop=True)

if __name__ == "__main__":
    main()