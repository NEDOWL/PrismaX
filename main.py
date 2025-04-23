import telebot
from telebot import types
import sqlite3
import time
import random
import hashlib
import requests  # Для работы с API ЮMoney
import urllib.parse
import threading  # Для запуска проверки в отдельном потоке
import event

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()

tocen = ''
bot = telebot.TeleBot(token=tocen)
admin = 
###
from flask import request

@bot.message_handler(commands=['policy'])
def show_agreements_1(message):
    bot.send_message(message.chat.id, text=(
            "📜 **Пользовательское соглашение и Политика конфиденциальности**\n\n"
            "1️⃣ [Пользовательским соглашением](https://telegra.ph/POLZOVATELSKOE-SOGLASHENIE-04-17-6)\n"
            "2️⃣ [Политикой конфиденциальности](https://telegra.ph/Politika-konfidencialnosti-04-17-7)\n\n"
            
        ),
        parse_mode="Markdown"
    )


def show_agreements(message):
    markup = types.InlineKeyboardMarkup()
    agree_button = types.InlineKeyboardButton(text='✅ Согласен', callback_data='agree')
    disagree_button = types.InlineKeyboardButton(text='❌ Не согласен', callback_data='disagree')
    markup.add(agree_button, disagree_button)
    bot.send_message(
        message.chat.id,
        text=(
            "📜 **Пользовательское соглашение и Политика конфиденциальности**\n\n"
            "Перед использованием бота, пожалуйста, ознакомьтесь с:\n\n"
            "1️⃣ [Пользовательским соглашением](https://telegra.ph/POLZOVATELSKOE-SOGLASHENIE-04-17-6)\n"
            "2️⃣ [Политикой конфиденциальности](https://telegra.ph/Politika-konfidencialnosti-04-17-7)\n\n"
            "Нажимая \"Согласен\", вы подтверждаете, что ознакомились и принимаете условия."
        ),
        reply_markup=markup,
        parse_mode="Markdown"
    )
@bot.callback_query_handler(func=lambda call: call.data in ['agree', 'disagree'])
def handle_agreement(call):
    if call.data == 'agree':
        cursor.execute('INSERT OR REPLACE INTO user_agreements (user_id, agreed) VALUES (?, ?)', (call.from_user.id, 1))
        conn.commit()
        bot.send_message(call.message.chat.id, text="🎉 Спасибо за согласие! Добро пожаловать!")
        menu(call.message)  # Переход в главное меню
    elif call.data == 'disagree':
        bot.send_message(call.message.chat.id, text="❌ Вы не можете использовать бота без согласия.")

def save_user_ip(user_id):
    ip_address = request.remote_addr  # Получаем IP-адрес пользователя
    cursor.execute('UPDATE user SET ip_address = ? WHERE user_id = ?', (ip_address, user_id))
    conn.commit()

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
    # for i in ref_cods:
    #    if i == ref_cod:
    #        ref_cod = random.randint(1000000, 9999999)
    print("ref", ref_cods)
    print(message.from_user.id)
    cursor.execute('INSERT INTO card_common (user_id, gtx_1080_ti, gtx_1080, gtx_2060, gtx_2070, gtx_2080, gtx_2080_ti, rtx_3060, rtx_3060_ti, rtx_3070, rtx_3070_ti) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    cursor.execute('INSERT INTO card (user_id, rtx_5090, rtx_4090, rtx_3090_ti, rtx_3090, rtx_3080_ti, rtx_3080, ice_river_aeo, goldshell_ae_box, goldshell_ae_box_pro, goldshell_ae_box_ii, gtx_1080_ti) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    cursor.execute('INSERT INTO crypto_price (btc, eth, ltc, xrp, doge, hmstr) VALUES (?, ?, ?, ?, ?, ?)', (btc, eth, ltc, xrp, doge, hmstr))
    cursor.execute('INSERT INTO crypto (user_id, btc, eth, ltc, xrp, doge, hmstr) VALUES (?, ?, ?, ?, ?, ?, ?)', (user_id, 0, 0, 0, 0, 0, 0))
    cursor.execute('INSERT INTO user (user_id, user_name, admin, balanse, balanse_viv, time_income, mining, start_pack, ref_cod, ref_count, last_bonus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (user_id, user_name, admin, 0, 0, times, 'BTC', 0, ref_cod, 0, times - 86401))
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
    #save_user_ip(user_id)

#def check_multiaccount(user_id):
 #   ip_address = cursor.execute('SELECT ip_address FROM user WHERE user_id = ?', (user_id,)).fetchone()[0]
 #   if not ip_address:
 #       return False

    # Проверяем, есть ли другие аккаунты с таким же IP
   # accounts = cursor.execute('SELECT user_id FROM user WHERE ip_address = ? AND user_id != ?', (ip_address, user_id)).fetchall()
   # if accounts:
   #     return True  # Найдены другие аккаунты с таким же IP
   # return False

#def notify_admin_about_multiaccount(user_id):
 #   if check_multiaccount(user_id):
  #      bot.send_message(
   #         admin,
    #        text=f"⚠️ Обнаружен мультиаккаунт!\n\nПользователь ID: {user_id} использует тот же IP, что и другие аккаунты."
     #   )

def ref_new(message, ref_cod):
    user = cursor.execute('SELECT user_id FROM user WHERE ref_cod = ?', (ref_cod,)).fetchone()
    if user is None:
        pass
        #bot.send_message(message.chat.id, text='Ошибка 111: реферальная ссылка не верна\n\nОбратитесь к администратору')
    else:
        cursor.execute('SELECT ref_count FROM user WHERE user_id = ?', (user[0],))
        ref_count = cursor.fetchone()[0]
        cursor.execute('UPDATE user SET ref_count = ? WHERE user_id = ?', (ref_count + 1, user[0]))
        cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user[0],))
        balanse = cursor.fetchone()[0]
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse + 1000, user[0]))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (1000, message.from_user.id))
        conn.commit()


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    agreement = cursor.execute('SELECT agreed FROM user_agreements WHERE user_id = ?', (user_id,)).fetchone()
    if agreement is None or agreement[0] == 0:
        show_agreements(message)
    else:
        start_1(message)

def start_1(message):
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
    user_id = message.from_user.id
    #notify_admin_about_multiaccount(user_id)
    print(cursor.execute('SELECT * FROM user').fetchall())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    profile = types.KeyboardButton('👤 Профиль')
    admin = types.KeyboardButton('🔧 Админ')
    shop_common = types.KeyboardButton('🛒 Магазин')
    shop = types.KeyboardButton('💎 Премиум магазин')
    premium_button = types.KeyboardButton('💎 Купить премиум')
    bir = types.KeyboardButton('📈 Биржа')
    rating = types.KeyboardButton('Рейтинг')
    '''casino = types.KeyboardButton('🎰 Казино')'''
    event = types.KeyboardButton('🎲 События')
    admins = cursor.execute('SELECT admin FROM user WHERE user_id = ?', (int(message.from_user.id),)).fetchall()
    print(admins)
    print(cursor.execute('SELECT * FROM user').fetchall())
    if admins == [(1,)]:
        markup.add(profile, shop_common, shop, premium_button, bir, rating, event, admin)
    else:
        markup.add(profile, shop_common, shop, premium_button, bir, rating, event)
    bot.send_message(
    message.chat.id,
    text=(
        "🏠 **Добро пожаловать в главное меню!**\n\n"
        "🔹 Здесь вы можете:\n"
        "1️⃣ **👤 Профиль** — посмотреть информацию о вашем аккаунте.\n"
        "2️⃣ **💎 Премиум магазин** — приобрести эксклюзивные товары.\n"
        "3️⃣ **🛒 Магазин** — купить стандартные товары.\n"
        "4️⃣ **📈 Биржа** — торговать криптовалютой.\n"
        "Выберите действие, нажав на соответствующую кнопку ниже. 👇"
    ),
    reply_markup=markup,
    parse_mode="Markdown")


def profile(message):
    user_id = message.from_user.id
    is_premium = check_premium_status(user_id)
    premium_status = "Активен" if is_premium else "Не активен"

    update_card_income(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    change_mine_crime = types.KeyboardButton(text='⛏️ Выбор криптовалюты')
    start_pack = types.KeyboardButton(text='🎁 Забрать стартовый пакет')
    yoomoney = types.KeyboardButton('💳 Пополнить Баланс')
    yoomoney_2 = types.KeyboardButton('💳 Вывести Баланс')
    history_button = types.KeyboardButton('📜 История операций')
    ref = types.KeyboardButton(text='🤝 Рефер. прог.')
    conversion = types.KeyboardButton('Конвертация валют')
    daily_bonus = types.KeyboardButton('🎁 Ежедневный бонус')
    back = types.KeyboardButton(text='🔙 Назад')
    if cursor.execute('SELECT start_pack FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] == 0:
        markup.add(change_mine_crime, yoomoney, yoomoney_2, history_button, start_pack, ref, conversion, daily_bonus, back)
    else:
        markup.add(change_mine_crime, yoomoney, yoomoney_2, history_button, ref, conversion, daily_bonus, back)
    ming = cursor.execute('SELECT mining FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    global bal
    
    bal = 0
    income = 0
    cursor.execute('SELECT rtx_5090, rtx_4090, rtx_3090_ti, rtx_3090, rtx_3080_ti, rtx_3080, ice_river_aeo, goldshell_ae_box, goldshell_ae_box_pro, goldshell_ae_box_ii, gtx_1080_ti FROM card WHERE user_id = ?', (message.from_user.id,))
    for i in cursor.fetchall():
        for j in i:
            income += j
        print(income)
    cursor.execute('SELECT gtx_1080_ti, gtx_1080, gtx_2060, gtx_2070, gtx_2080, gtx_2080_ti, rtx_3060, rtx_3060_ti, rtx_3070, rtx_3070_ti FROM card_common WHERE user_id = ?', (message.from_user.id,))
    for i in cursor.fetchall():
        for j in i:
            income += j
    times = cursor.execute('SELECT time_income FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    times = time.time()-times
    print(round(times, 0))
    if premium_status == 'Активен':
        income = income * 1.2
        print('income', income)
    else:
        income = income
        
    if times >= 1:
        bal = round(income * (times/3600/24/30), 3)
        print('bal=',bal)
    wallets(message)
    cursor.execute('UPDATE user SET time_income = ? WHERE user_id = ?', (time.time(), message.from_user.id))
    cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,))
    balanse = round(cursor.fetchone()[0], 3)
    print(balanse)
    cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse, message.from_user.id))
    conn.commit()
    balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]

    btc = round(float(f"{cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}"), 8)
    print(f'{btc:.10f}')
    eth = float(f"{cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}")
    ltc = float(f"{cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}")
    xrp = float(f"{cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}")
    doge = float(f"{cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}")
    hmstr = float(f"{cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:.10f}")
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
    balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    bot.send_message(message.chat.id, text=f'''👤 Ваш профиль:
💎 Премиум-аккаунт: {premium_status}
⏳ Действует до: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cursor.execute('SELECT premium_until FROM user WHERE user_id = ?', (user_id,)).fetchone()[0])) if is_premium else '—'}

👤 Имя пользователя: {message.from_user.username}
🆔 ID: {message.from_user.id}
💰 Баланс: {balanse} руб.
💰 Баланс вив: {balanse_viv:.3f} вив

💎 Криптовалюты:
BTC: {btc:.8f}
ETH: {eth:.8f}
LTC: {ltc:.8f}
XRP: {xrp:.8f}
DOGE: {doge:.8f}
HMSTR: {hmstr:.8f}

⛏️ Криптовалюта для майнинга: {ming}

📈 Общий доход:
{(income/30/24):.3f} вив/час''', reply_markup=markup)
    print(cursor.execute('SELECT * FROM card').fetchall())

def premium_menu(message):
    markup = types.InlineKeyboardMarkup()
    buy_premium_button = types.InlineKeyboardButton(text='💎 Купить премиум (249 руб.)', callback_data='buy_premium')
    back_button = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back')
    markup.add(buy_premium_button, back_button)

    bot.send_message(
        message.chat.id,
        text=(
            "💎 **Премиум-аккаунт**\n\n"
            "🔹 **Что дает премиум?**\n"
            "1️⃣ Увеличенный доход от видеокарт (+20%).\n"
            "2️⃣ Снижение комиссии на вывод средств (с 5% до 2%).\n"
            "3️⃣ Увеличенные ежедневные бонусы (+50%).\n"
            "4️⃣ Приоритетная поддержка.\n\n"
            "💰 **Стоимость:** 249 руб. (действует 30 дней).\n\n"
            "Нажмите \"Купить премиум\", чтобы активировать премиум-аккаунт."
        ),
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == 'buy_premium')
def handle_buy_premium(call):
    user_ids = call.from_user.id
    buy_premium(call.message, user_ids)

def buy_premium(message, user_ids):
    user_id = user_ids
    premium_price = 249  # Стоимость премиум-аккаунта в рублях
    balanse_rub = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_id,)).fetchone()[0]

    if balanse_rub >= premium_price:
        # Списываем деньги
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse_rub - premium_price, user_id))

        # Устанавливаем премиум-статус и дату окончания
        current_time = time.time()
        premium_until = current_time + 30 * 24 * 3600  # Добавляем 30 дней
        cursor.execute('UPDATE user SET premium = 1, premium_until = ? WHERE user_id = ?', (premium_until, user_id))
        conn.commit()

        bot.send_message(
            message.chat.id,
            text=(
                "🎉 **Поздравляем!**\n\n"
                "Вы успешно приобрели премиум-аккаунт!\n\n"
                "💎 Теперь вы получаете:\n"
                "🔹 Увеличенный доход от видеокарт.\n"
                "🔹 Сниженную комиссию на вывод средств.\n"
                "🔹 Увеличенные ежедневные бонусы.\n\n"
                f"⏳ Премиум-аккаунт активен до: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(premium_until))}."
            ),
            parse_mode="Markdown"
        )
        log_transaction(user_id, "Покупка", -premium_price, "Покупка премиум-аккаунта")
    else:
        bot.send_message(
            message.chat.id,
            text=(
                "❌ **Недостаточно средств!**\n\n"
                "Стоимость премиум-аккаунта: 249 руб.\n"
                "Пополните баланс, чтобы приобрести премиум-аккаунт."
            )
        )

def check_premium_status(user_id):
    # Получаем статус премиума и дату окончания
    premium, premium_until = cursor.execute(
        'SELECT premium, premium_until FROM user WHERE user_id = ?', (user_id,)
    ).fetchone()

    current_time = time.time()

    # Проверяем, активен ли премиум
    if premium == 1 and premium_until > current_time:
        return True

    # Если срок истёк, сбрасываем премиум-статус
    if premium_until <= current_time:
        cursor.execute('UPDATE user SET premium = 0, premium_until = 0 WHERE user_id = ?', (user_id,))
        conn.commit()

    return False

def daily_bonus(message):
    user_id = message.from_user.id
    last_bonus_time = cursor.execute('SELECT last_bonus FROM user WHERE user_id = ?', (user_id,)).fetchone()[0]
    current_time = time.time()

    # Проверяем, прошли ли 24 часа с последнего бонуса
    if current_time - last_bonus_time >= 86400:  # 86400 секунд = 24 часа
        bonus_amount = 50  # Фиксированный бонус
        premium = cursor.execute('SELECT premium FROM user WHERE user_id = ?', (user_id,)).fetchone()[0]
        if premium == 1:
            bonus_amount += 25
        cursor.execute('UPDATE user SET balanse_viv = balanse_viv + ?, last_bonus = ? WHERE user_id = ?', (bonus_amount, current_time, user_id))
        conn.commit()
        bot.send_message(
            message.chat.id,
            text=f"🎉 **Ежедневный бонус!**\n\nВы получили {bonus_amount} вив за вход сегодня. Заходите каждый день, чтобы получать бонусы!"
        )
    else:
        remaining_time = 86400 - (current_time - last_bonus_time)
        hours = int(remaining_time // 3600)
        minutes = int((remaining_time % 3600) // 60)
        bot.send_message(
            message.chat.id,
            text=f"⏳ Вы уже получили бонус сегодня. Следующий бонус будет доступен через {hours} часов и {minutes} минут."
        )

def update_card_income(message):
    # Получаем текущий доход и время последнего обновления
    user_id = message.from_user.id
    last_update = cursor.execute('SELECT time_income FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    current_time = time.time()
    elapsed_days = (current_time - last_update) / (3600 * 24)  # Переводим время в дни

    if elapsed_days >= 30:  # Проверяем, прошло ли 30 дней
        # Уменьшаем доход всех карт на 5%
        cursor.execute('''
            UPDATE card_common
            SET gtx_1080_ti = gtx_1080_ti * 0.95,
                gtx_1080 = gtx_1080 * 0.95,
                gtx_2060 = gtx_2060 * 0.95,
                gtx_2070 = gtx_2070 * 0.95,
                gtx_2080 = gtx_2080 * 0.95,
                gtx_2080_ti = gtx_2080_ti * 0.95,
                rtx_3060 = rtx_3060 * 0.95,
                rtx_3060_ti = rtx_3060_ti * 0.95,
                rtx_3070 = rtx_3070 * 0.95,
                rtx_3070_ti = rtx_3070_ti * 0.95
            WHERE user_id = ?
        ''', (user_id,))
        # Обновляем время последнего обновления
        cursor.execute('UPDATE user SET time_income = ? WHERE user_id = ?', (current_time, user_id))
        conn.commit()

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


# def wallet(message):
#   wallets(message)
#  cursor.execute('SELECT btc, eth, ltc, xrp, doge, hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,))
# wallet = cursor.fetchone()
# print(wallet)
# bot.send_message(message.chat.id, text=f'Кошелек\nbtc: {wallet[0]}\neth: {wallet[1]}\nltc: {wallet[2]}\nxrp: {wallet[3]}\ndoge: {wallet[4]}\nhmstr: {wallet[5]}')

# Конвертация рублей в вив
def rub_to_viv(rub):
    return rub * 100


# Конвертация вив в рубли
def viv_to_rub(viv):
    return viv / 100


# Обновление функции give_balanse для работы с вив
def give_balanse(user_id: int, balanse_viv: int):
    cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse_viv, user_id))
    conn.commit()


def give_balanse_rub(user_id: int, balanse: int):
    cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse, user_id))
    conn.commit()


def pay(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sto = types.KeyboardButton('💵 100')
    dves = types.KeyboardButton('💵 200')
    tris = types.KeyboardButton('💵 300')
    chet = types.KeyboardButton('💵 400')
    five = types.KeyboardButton('💵 500')
    beck = types.KeyboardButton('🔙 Назад')
    markup.add(sto, dves, tris, chet, five, beck)
    bot.send_message(message.chat.id, text='💳 Выберите сумму пополнения:', reply_markup=markup)


def shop_common(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    gtx_1080_ti = types.KeyboardButton('🖥️ GTX 1080 TI')
    gtx_1080 = types.KeyboardButton('🖥️ GTX 1080')
    gtx_2060 = types.KeyboardButton('🖥️ GTX 2060')
    gtx_2070 = types.KeyboardButton('🖥️ GTX 2070')
    gtx_2080 = types.KeyboardButton('🖥️ GTX 2080')
    gtx_2080_ti = types.KeyboardButton('🖥️ GTX 2080 TI')
    rtx_3060 = types.KeyboardButton('🖥️ RTX 3060')
    rtx_3060_ti = types.KeyboardButton('🖥️ RTX 3060 TI')
    rtx_3070 = types.KeyboardButton('🖥️ RTX 3070')
    rtx_3070_ti = types.KeyboardButton('🖥️ RTX 3070 TI')
    # next = types.KeyboardButton('Следующая страница')
    beck = types.KeyboardButton('🔙 Назад')
    markup.add(gtx_1080_ti, gtx_1080, gtx_2060, gtx_2070, gtx_2080, gtx_2080_ti, rtx_3060, rtx_3060_ti, rtx_3070, rtx_3070_ti, beck)
    balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    bot.send_message(
    message.chat.id,
    text=(
        "🛒 **Добро пожаловать в магазин видеокарт!**\n\n"
        "🔹 Здесь вы можете приобрести видеокарты для майнинга криптовалют.\n"
        "Каждая карта имеет свои характеристики и доходность.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Выберите видеокарту из списка ниже.\n"
        "2️⃣ Ознакомьтесь с её характеристиками и стоимостью.\n"
        "3️⃣ Нажмите кнопку \"Купить\", чтобы приобрести карту.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f} вив.\n\n"
        "Выберите видеокарту из списка ниже. 👇"
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)


def gtx_1080_ti(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_1080_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    current_count = cursor.execute('SELECT gtx_1080_ti FROM card_common WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 150  # Базовая стоимость
    price = base_price * (1.1 ** (current_count / 50))  # Увеличение на 10% за каждую карту
    lic = round(price / 50, 2)  # Увеличен срок окупаемости
    bot.send_message(
        message.chat.id,
        text=(
            "Вы выбрали карту **GTX 1080 TI**\n\n"
            "🔹 **Характеристики и стоимость:**\n"
            "💰 Доход: 50 вив/мес\n"  # Уменьшено для увеличения срока окупаемости
            f"💵 Стоимость: {price:.2f} вив\n"  # Увеличена стоимость
            f"⏳ Окупаемость: {lic} месяцев\n\n"  # Увеличен срок окупаемости
            "💡 **Как это работает?**\n"
            "1️⃣ Вы покупаете карту.\n"
            "2️⃣ Карта начинает приносить доход.\n"
            f"3️⃣ Окупаемость наступает через {lic} месяцев.\n\n"
            "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
        ),
        reply_markup=markup,
        parse_mode="Markdown"
    )

    

def buy_1080_ti(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return

    balanses = result[0]
    # Получаем текущее количество карт GTX 1080 TI у пользователя
    current_count = cursor.execute('SELECT gtx_1080_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 150  # Базовая стоимость
    price = base_price * (1.1 ** (current_count / 50))  # Увеличение на 10% за каждую карту

    if balanses >= price:
        cursor.execute('UPDATE card_common SET gtx_1080_ti = ? WHERE user_id = ?', (current_count + 50, user_ids))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
            call.chat.id,
            text=(
                f"🎉 **Поздравляем!**\n\n"
                f"Вы успешно приобрели **GTX 1080 TI** за {price:.2f} вив.\n\n"
                f"💰 **Ваш текущий баланс:** {balanse_viv:.3f} вив.\n\n"
                "Продолжайте покупки или вернитесь в главное меню. 👇"
            ),
            parse_mode="Markdown"
        )
        log_transaction(user_ids, "Покупка", price, f"Покупка карты GTX 1080 TI")
    else:
        bot.send_message(
            call.chat.id,
            text=(
                "❌ **Недостаточно средств!**\n\n"
                "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
                "💡 **Что можно сделать?**\n"
                "1️⃣ Пополните баланс через меню пополнения.\n"
                "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
                "Если у вас возникли вопросы, обратитесь в поддержку."
            ),
            parse_mode="Markdown"
        )

def gtx_1080(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_1080')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)

    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_1080 FROM card_common WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 80  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 250  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 80, 2)  # Увеличен срок окупаемости
    bot.send_message(
        message.chat.id,
        text=(
            "Вы выбрали карту **GTX 1080**\n\n"
            "🔹 **Характеристики и стоимость:**\n"
            "💰 Доход: 80 вив/мес\n"
            f"💵 Стоимость: {price:.2f} вив\n"
            f"⏳ Окупаемость: {lic} месяца\n\n"
            "💡 **Как это работает?**\n"
            "1️⃣ Вы покупаете карту.\n"
            "2️⃣ Карта начинает приносить доход.\n"
            f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
            "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
        ),
        reply_markup=markup,
        parse_mode="Markdown"
    )

def buy_1080(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return

    balanses = result[0]
    income = cursor.execute('SELECT gtx_1080 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_1080 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 80  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 250  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    if balanses >= price:
        cursor.execute('UPDATE card_common SET gtx_1080 = ? WHERE user_id = ?', (income + 80, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **GTX 1080** за {price:.2f} вив.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты GTX 1080")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def gtx_2060(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_2060')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
     # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_2060 FROM card_common WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 100  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 350  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 100, 2)  # Увеличен срок окупаемости

    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **GTX 2060**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 100 вив/мес\n"
        f"💵 Стоимость: {price:.3f} вив\n"
        f"⏳ Окупаемость: {lic} месяца\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_2060(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return

    balanses = result[0]
    income = cursor.execute('SELECT gtx_2060 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
     # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_2060 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 100  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 350  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 100, 2)  # Увеличен срок окупаемости
    
    if balanses >= price:
        cursor.execute('UPDATE card_common SET gtx_2060 = ? WHERE user_id = ?', (income + 100, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **GTX 2060** за {price:.2f} вив.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты GTX 2060")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def gtx_2070(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_2070')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    user_ids = message.from_user.id
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_2070 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 200  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 500  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 200, 2)  # Увеличен срок окупаемости
    
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **GTX 2070**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 200 вив/мес\n"
        f"💵 Стоимость: {price:.2f} вив\n"
        f"⏳ Окупаемость: {lic} месяца\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_2070(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return
   # user_ids = message.from_user.id
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_2070 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 200  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 500  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 200, 2)  # Увеличен срок окупаемости
    
    balanses = result[0]
    income = cursor.execute('SELECT gtx_2070 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= price:
        cursor.execute('UPDATE card_common SET gtx_2070 = ? WHERE user_id = ?', (income + 200, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **GTX 2070** за {price:.2f} вив.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты GTX 2070")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def gtx_2080(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_2080')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    user_ids = message.from_user.id
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_2080 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 250  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 700  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 250, 2)  # Увеличен срок окупаемости
    
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **GTX 2080**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 250 вив/мес\n"
        f"💵 Стоимость: {price:.3f} вив\n"
        f"⏳ Окупаемость: {lic} месяца\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_2080(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_2080 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 250  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 700  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 250, 2)  # Увеличен срок окупаемости
    
    balanses = result[0]
    income = cursor.execute('SELECT gtx_2080 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= price:
        cursor.execute('UPDATE card_common SET gtx_2080 = ? WHERE user_id = ?', (income + 250, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **GTX 2080** за {price:.3f} вив.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты GTX 2080")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def gtx_2080_ti(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_2080_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    user_ids = message.from_user.id
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_2080_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 300  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 1000  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 300, 2)  # Увеличен срок окупаемости
    user_ids = message.from_user.id
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **GTX 2080 TI**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 300 вив/мес\n"
        f"💵 Стоимость: {price:.3f} вив\n"
        f"⏳ Окупаемость: {lic} месяца\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_2080_ti(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT gtx_2080_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 300  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 1000  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 300, 2)  # Увеличен срок окупаемости
    
    balanses = result[0]
    income = cursor.execute('SELECT gtx_2080_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= price:
        cursor.execute('UPDATE card_common SET gtx_2080_ti = ? WHERE user_id = ?', (income + 300, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **GTX 2080 TI** за {price:.3f} вив.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты GTX 2080 TI")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_3060(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3060')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    user_ids = message.from_user.id
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT rtx_3060 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 350  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 1200  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 350, 2)  # Увеличен срок окупаемости
    user_ids = message.from_user.id
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 3060**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 350 вив/мес\n"
        f"💵 Стоимость: {price:.3f} вив\n"
        f"⏳ Окупаемость: {lic} месяца\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_3060(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT rtx_3600 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 350  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 1200  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 350, 2)  # Увеличен срок окупаемости
    
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3060 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= price:
        cursor.execute('UPDATE card_common SET rtx_3060 = ? WHERE user_id = ?', (income + 350, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **RTX 3060** за {price:.3f}.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты RTX 3060")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_3060_ti(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3060_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    user_ids = message.from_user.id
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT rtx_3060_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 400  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 1500  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 400, 2)  # Увеличен срок окупаемости
    
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 3060 TI**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 400 вив/мес\n"
        f"💵 Стоимость: {price:.3f} вив\n"
        f"⏳ Окупаемость: {lic}  месяца\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_3060_ti(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT rtx_3060_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 400  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 1500  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 400, 2)  # Увеличен срок окупаемости
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3060_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= price:
        cursor.execute('UPDATE card_common SET rtx_3060_ti = ? WHERE user_id = ?', (income + 400, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **RTX 3060 TI** за {price:.3f} вив.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты RTX 3060 TI")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_3070(message):
    user_ids = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3070')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT rtx_3070 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 500  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 2000  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 500, 2)  # Увеличен срок окупаемости
    user_ids = message.from_user.id
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 3070**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 500 вив/мес\n"
        f"💵 Стоимость: {price:.3f} вив\n"
        f"⏳ Окупаемость: {lic} месяца\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_3070(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return
        # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT rtx_3070 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 500  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 2000  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 500, 2)  # Увеличен срок окупаемости
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3070 FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= price:
        cursor.execute('UPDATE card_common SET rtx_3070 = ? WHERE user_id = ?', (income + 500, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **RTX 3070** за {price:.3f} вив.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты RTX 3070")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_3070_ti(message):
    user_ids = message.from_user.id
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3070_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT rtx_3070_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 600  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 2500  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 600, 2)  # Увеличен срок окупаемости
    user_ids = message.from_user.id
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 3070 TI**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 600 вив/мес\n"
        f"💵 Стоимость: {price:.3f} вив\n"
        f"⏳ Окупаемость: {lic} месяца\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        f"3️⃣ Окупаемость наступает через {lic} месяца.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_3070_ti(call, user_ids):
    result = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        bot.send_message(call.chat.id, text='Ошибка 123: пользователь не найден в базе данных.\n\nОбратитесь к администратору')
        return
    # Получаем текущий доход от GTX 1080
    current_income = cursor.execute('SELECT rtx_3070_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    # Вычисляем количество карт
    card_count = current_income // 600  # Доход одной карты — 120 вив/мес
    # Рассчитываем стоимость с учетом прогрессивного увеличения
    base_price = 2500  # Базовая стоимость
    price = base_price * (1.1 ** card_count)  # Увеличение на 10% за каждую карту
    lic = round(price / 600, 2)  # Увеличен срок окупаемости
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3070_ti FROM card_common WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= price:
        cursor.execute('UPDATE card_common SET rtx_3070_ti = ? WHERE user_id = ?', (income + 600, user_ids,))
        conn.commit()
        give_balanse(user_id=user_ids, balanse_viv=balanses - price)
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
        call.chat.id,
        text=(
        "🎉 **Поздравляем!**\n\n"
        f"Вы успешно приобрели **RTX 3070 TI** за {price:.3f} вив.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv}.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", price, f"Покупка карты RTX 3070 TI")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


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
    bot.send_message(
    message.chat.id,
    text=(
        "🛒 **Добро пожаловать в премиум-магазин!**\n\n"
        "🔹 Здесь вы можете приобрести эксклюзивные видеокарты с высокой доходностью.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Выберите видеокарту из списка ниже.\n"
        "2️⃣ Ознакомьтесь с её характеристиками и стоимостью.\n"
        "3️⃣ Нажмите кнопку \"Купить\", чтобы приобрести карту.\n\n"
        "Выберите видеокарту из списка ниже. 👇"
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def shop_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ice_river = types.KeyboardButton('Ice River AEO')
    gl_shell = types.KeyboardButton('Goldshell AE BOX')
    gl_shell_pro = types.KeyboardButton('Goldshell AE BOX PRO')
    gl_shell_ii = types.KeyboardButton('Goldshell AE BOX II')
    back_1 = types.KeyboardButton('Предыдущая страница')
    beck = types.KeyboardButton('Назад')
    markup.add(ice_river, gl_shell, gl_shell_pro, gl_shell_ii, beck, back_1)
    bot.send_message(
    message.chat.id,
    text=(
        "🛒 **Добро пожаловать в премиум-магазин (страница 2)!**\n\n"
        "🔹 Здесь вы можете приобрести эксклюзивные видеокарты с высокой доходностью.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Выберите видеокарту из списка ниже.\n"
        "2️⃣ Ознакомьтесь с её характеристиками и стоимостью.\n"
        "3️⃣ Нажмите кнопку \"Купить\", чтобы приобрести карту.\n\n"
        "Выберите видеокарту из списка ниже. 👇"
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def rtx_5090(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_5090')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 5090**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 78800 вив/мес\n"
        "💵 Стоимость: 10,000 руб\n"
        "⏳ Окупаемость: 12 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        "3️⃣ Окупаемость наступает через 12 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_5090(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return

    balanses = result[0]
    income = cursor.execute('SELECT rtx_5090 FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 10000:
        cursor.execute('UPDATE card SET rtx_5090 = ? WHERE user_id = ?', (income + 78800, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 10000)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно приобрели **RTX 5090**.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ), parse_mode="Markdown")
        log_transaction(user_ids, "Покупка", 10000, f"Покупка карты RTX 5090")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_4090(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_4090')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 4090**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 48300 вив/мес\n"
        "💵 Стоимость: 8000 руб\n"
        "⏳ Окупаемость: 15 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        "3️⃣ Окупаемость наступает через 15 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_4090(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_4090 FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 8000:
        cursor.execute('UPDATE card SET rtx_4090 = ? WHERE user_id = ?', (income + 48300, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 8000)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно приобрели **RTX 4090**.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", 8000, f"Покупка карты RTX 4090")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_3090_ti(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3090_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 3090 TI**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 33000 вив/мес\n"
        "💵 Стоимость: 6000 руб\n"
        "⏳ Окупаемость: 18 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        "3️⃣ Окупаемость наступает через 18 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_3090_ti(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3090_ti FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 6000:
        cursor.execute('UPDATE card SET rtx_3090_ti = ? WHERE user_id = ?', (income + 33000, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 6000)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно приобрели **RTX 3090 TI**.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)    
        log_transaction(user_ids, "Покупка", 6000, f"Покупка карты RTX 3090 TI")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_3090(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3090')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 3090**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 30000 вив/мес\n"
        "💵 Стоимость: 5500 руб\n"
        "⏳ Окупаемость: 15 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        "3️⃣ Окупаемость наступает через 15 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_3090(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3090 FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 5500:
        cursor.execute('UPDATE card SET rtx_3090 = ? WHERE user_id = ?', (income + 30000, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 5500)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно купили **RTX 3090**.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)    
        log_transaction(user_ids, "Покупка", 5500, f"Покупка карты RTX 3090")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_3080_ti(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3080_ti')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 3080 TI**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 25000 вив/мес\n"
        "💵 Стоимость: 3000 руб\n"
        "⏳ Окупаемость: 12 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        "3️⃣ Окупаемость наступает через 12 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_3080_ti(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3080_ti FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 3000:
        cursor.execute('UPDATE card SET rtx_3080_ti = ? WHERE user_id = ?', (income + 25000, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 3000)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно купили **RTX 3080 TI**.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", 3000, f"Покупка карты RTX 3080 TI")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def rtx_3080(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_3080')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали карту **RTX 3080**\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 22000 вив/мес\n"
        "💵 Стоимость: 2500 руб\n"
        "⏳ Окупаемость: 10 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход каждый месяц.\n"
        "3️⃣ Окупаемость наступает через 10 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_3080(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT rtx_3080 FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 2500:
        cursor.execute('UPDATE card SET rtx_3080 = ? WHERE user_id = ?', (income + 22000, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 2500)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно купили **RTX 3080**.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", 2500, f"Покупка карты RTX 3080")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def iraeo(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_iraeo')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали Ice River AEO\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 500000 вив/мес\n"
        "💵 Стоимость: 50000 руб\n"
        "⏳ Окупаемость: 10 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        "3️⃣ Окупаемость наступает через 10 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_iraeo(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT ice_river_aeo FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 50000:
        cursor.execute('UPDATE card SET ice_river_aeo = ? WHERE user_id = ?', (income + 500000, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 50000)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно купили Ice River AEO.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)    
        log_transaction(user_ids, "Покупка", 50000, f"Покупка карты Ice River AEO")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def goldshell_ae_box(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_goldshell_ae_box')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали Goldshell AE BOX\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 300000 вив/мес\n"
        "💵 Стоимость: 35000 руб\n"
        "⏳ Окупаемость: 11 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход каждый.\n"
        "3️⃣ Окупаемость наступает через 11 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_goldshell_ae_box(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT goldshell_ae_box FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 35000:
        cursor.execute('UPDATE card SET goldshell_ae_box = ? WHERE user_id = ?', (income + 300000, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 35000)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно купили Goldshell AE BOX.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)   
        log_transaction(user_ids, "Покупка", 35000, f"Покупка карты Goldshell AE BOX")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def goldshell_ae_box_pro(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_goldshell_ae_box_pro')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали Goldshell AE BOX PRO\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 200000 вив/мес\n"
        "💵 Стоимость: 15000 руб\n"
        "⏳ Окупаемость: 11 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        "3️⃣ Окупаемость наступает через 11 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_goldshell_ae_box_pro(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT goldshell_ae_box_pro FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 15000:
        cursor.execute('UPDATE card SET goldshell_ae_box_pro = ? WHERE user_id = ?', (income + 200000, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 15000)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно купили Goldshell AE BOX PRO.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", 15000, f"Покупка карты Goldshell AE BOX PRO")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


def goldshell_ae_box_ii(message):
    markup = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton(text='Купить', callback_data='buy_goldshell_ae_box_ii')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(buy, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Вы выбрали Goldshell AE BOX II\n\n"
        "🔹 **Характеристики и стоимость:**\n"
        "💰 Доход: 150000 вив/мес\n"
        "💵 Стоимость: 10000 руб\n"
        "⏳ Окупаемость: 11 месяцев\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Вы покупаете карту.\n"
        "2️⃣ Карта начинает приносить доход.\n"
        "3️⃣ Окупаемость наступает через 11 месяцев.\n\n"
        "Нажмите \"Купить\", чтобы приобрести карту, или \"Назад\", чтобы вернуться."
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def buy_goldshell_ae_box_ii(call, user_ids):
    result = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()
    if result is None:
        print(user_ids)
        bot.send_message(call.chat.id, text='Ошибка: пользователь не найден в базе данных.')
        return
    balanses = result[0]
    income = cursor.execute('SELECT goldshell_ae_box_ii FROM card WHERE user_id = ?', (user_ids,)).fetchone()[0]
    if balanses >= 10000:
        cursor.execute('UPDATE card SET goldshell_ae_box_ii = ? WHERE user_id = ?', (income + 150000, user_ids,))
        conn.commit()
        give_balanse_rub(user_id=user_ids, balanse=balanses - 10000)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (user_ids,)).fetchone()[0]
        bot.send_message(
    call.chat.id,
    text=(
        "🎉 **Поздравляем!**\n\n"
        "Вы успешно купили Goldshell AE BOX II.\n\n"
        f"💰 **Ваш текущий баланс обновлен {balanse}.**\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(user_ids, "Покупка", 10000, f"Покупка карты Goldshell AE BOX II")
    else:
        bot.send_message(
    call.chat.id,
    text=(
        "❌ **Недостаточно средств!**\n\n"
        "🔹 Убедитесь, что у вас достаточно средств для выполнения этой операции.\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Пополните баланс через меню пополнения.\n"
        "2️⃣ Проверьте текущий баланс в разделе \"👤 Профиль\".\n\n"
        "Если у вас возникли вопросы, обратитесь в поддержку."
    ),
    parse_mode="Markdown"
)


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
        timet = time.time()
        cursor.execute('UPDATE time SET times = ? WHERE user_id = ?', (timet, message.from_user.id))
        cursor.execute('UPDATE crypto_price SET btc = ?, eth = ?, ltc = ?, xrp = ?, doge = ?, hmstr = ?', (btc, eth, ltc, xrp, doge, hmstr))
        conn.commit()
        print(times)
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
    #buy = types.InlineKeyboardButton(text='Купить монеты', callback_data='buy')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    inbvest = types.InlineKeyboardButton(text='Инвестировать', callback_data='invest')
    marcet.add(sale,inbvest, back)
    cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,))
    balanse_viv = cursor.fetchone()[0]
    bot.send_message(
    message.chat.id,
    text=(
        "📈 **Добро пожаловать на биржу криптовалют!**\n\n"
        "🔹 Здесь вы можете покупать криптовалюту по текущему курсу.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Ознакомьтесь с текущими курсами криптовалют.\n"
        "2️⃣ Укажите количество и подтвердите сделку.\n\n"
        "🔄 **Курс обновляется каждый час.**\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f} вив.\n\n"
        "Текущие курсы:\n"
        f"₿ BTC: {btc} вив/ед\n"
        f"Ξ ETH: {eth} вив/ед\n"
        f"Ł LTC: {ltc} вив/ед\n"
        f"✕ XRP: {xrp} вив/ед\n"
        f"Ð DOGE: {doge} вив/ед\n"
        f"🐹 HMSTR: {hmstr} вив/ед\n\n"
        "Выберите действие ниже. 👇"
    ),
    reply_markup=marcet,
    parse_mode="Markdown"
)

def invest(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    low_risk = types.KeyboardButton('📉 Низкий риск (5% прибыли)')
    medium_risk = types.KeyboardButton('📈 Средний риск (20% прибыли)')
    high_risk = types.KeyboardButton('🔥 Высокий риск (до 50% прибыли)')
    back = types.KeyboardButton('🔙 Назад')
    markup.add(low_risk, medium_risk, high_risk, back)
    bot.send_message(
        message.chat.id,
        text=(
            "💼 **Инвестиции**\n\n"
            "🔹 Выберите уровень риска для вашей инвестиции:\n"
            "1️⃣ **Низкий риск** — 5% прибыли, без риска потери.\n"
            "2️⃣ **Средний риск** — 20% прибыли, шанс потери 10%.\n"
            "3️⃣ **Высокий риск** — до 50% прибыли, шанс потери 50%.\n\n"
            "Выберите вариант ниже. 👇"
        ),
        reply_markup=markup
    )
    bot.register_next_step_handler(message, process_investment_choice)

def process_investment_choice(message):
    if message.text == '📉 Низкий риск (5% прибыли)':
        bot.send_message(message.chat.id, text='Введите сумму для инвестирования:')
        bot.register_next_step_handler(message, lambda msg: process_investment(msg, 'low'))
    elif message.text == '📈 Средний риск (20% прибыли)':
        bot.send_message(message.chat.id, text='Введите сумму для инвестирования:')
        bot.register_next_step_handler(message, lambda msg: process_investment(msg, 'medium'))
    elif message.text == '🔥 Высокий риск (до 50% прибыли)':
        bot.send_message(message.chat.id, text='Введите сумму для инвестирования:')
        bot.register_next_step_handler(message, lambda msg: process_investment(msg, 'high'))
    elif message.text == '🔙 Назад':
        # Здесь можно добавить логику возврата в главное меню или другое действие
        pass
    else:
        bot.send_message(message.chat.id, text='Пожалуйста, выберите один из предложенных вариантов.')

def process_investment(message, risk_level):
    try:
        amount = int(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if amount > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств для инвестиций.')
            return
        if amount <= 0:
            bot.send_message(message.chat.id, text='Сумма должна быть больше 0.')
            return

        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - amount, message.from_user.id))
        conn.commit()

        if risk_level == 'low':

            profit = amount * 0.05
            bot.send_message(message.chat.id, text=f'Вы получили прибыль: {profit:.2f} вив.')
            cursor.execute('UPDATE user SET balanse_viv = balanse_viv + ? WHERE user_id = ?', (profit + amount, message.from_user.id))

        elif risk_level == 'medium':
            if random.random() > 0.1:  # 90% шанс успеха
                profit = amount * 0.2
                bot.send_message(message.chat.id, text=f'Вы получили прибыль: {profit:.2f} вив.')
                cursor.execute('UPDATE user SET balanse_viv = balanse_viv + ? WHERE user_id = ?', (profit + amount, message.from_user.id))
            else:
                bot.send_message(message.chat.id, text='Вы потеряли свои инвестиции.')
        elif risk_level == 'high':
            if random.random() > 0.5:  # 50% шанс успеха
                profit = amount * 0.5
                bot.send_message(message.chat.id, text=f'Вы получили прибыль: {profit:.2f} вив.')
                cursor.execute('UPDATE user SET balanse_viv = balanse_viv + ? WHERE user_id = ?', (profit + amount, message.from_user.id))
            else:
                bot.send_message(message.chat.id, text='Вы потеряли свои инвестиции.')
        conn.commit()
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')

def buy(message):
    markup = types.InlineKeyboardMarkup()
    btc = types.InlineKeyboardButton(text='BTC', callback_data='btc_buy')
    eth = types.InlineKeyboardButton(text='ETH', callback_data='eth_buy')
    ltc = types.InlineKeyboardButton(text='LTC', callback_data='ltc_buy')
    xrp = types.InlineKeyboardButton(text='XRP', callback_data='xrp_buy')
    doge = types.InlineKeyboardButton(text='DOGE', callback_data='doge_buy')
    hmstr = types.InlineKeyboardButton(text='HMSTR', callback_data='hmstr_buy')
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    markup.add(btc, eth, ltc, xrp, doge, hmstr, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Выберите криптовалюту для покупки:\n\n"
        "🔹 **BTC**\n"
        "🔹 **ETH**\n"
        "🔹 **LTC**\n"
        "🔹 **XRP**\n"
        "🔹 **DOGE**\n"
        "🔹 **HMSTR**\n\n"
        "Нажмите на нужную криптовалюту, чтобы продолжить. 👇"
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)
def buy_btc(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,))
    btc = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество BTC для покупки\nВаш баланс: {btc:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, buy_btc_1)
def buy_btc_1(message):
    try:
        btc = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        btc_price = cursor.execute('SELECT btc FROM crypto_price').fetchone()[0]
        if btc <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if btc * btc_price > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств')
            return
        cursor.execute('UPDATE crypto SET btc = ? WHERE user_id = ?', (cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] + btc, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - btc * btc_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно купили {btc:.8f} BTC\n"
        f"💰 Ваш баланс: {round(new_balanse, 3)} вив.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)        
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')
def buy_eth(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,))
    eth = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество ETH для покупки\nВаш баланс: {eth:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, buy_eth_1)
def buy_eth_1(message):
    try:
        eth = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        eth_price = cursor.execute('SELECT eth FROM crypto_price').fetchone()[0]
        if eth <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if eth * eth_price > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств')
            return
        cursor.execute('UPDATE crypto SET eth = ? WHERE user_id = ?', (cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] + eth, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - eth * eth_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно купили {eth:.8f} ETH\n"
        f"💰 Ваш баланс: {round(new_balanse, 3)} вив.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')
def buy_ltc(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,))
    ltc = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество LTC для покупки\nВаш баланс: {ltc:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, buy_ltc_1)
def buy_ltc_1(message):
    try:
        ltc = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        ltc_price = cursor.execute('SELECT ltc FROM crypto_price').fetchone()[0]
        if ltc <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if ltc * ltc_price > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств')
            return
        cursor.execute('UPDATE crypto SET ltc = ? WHERE user_id = ?', (cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] + ltc, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - ltc * ltc_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно купили {ltc:.8f} LTC\n"
        f"💰 Ваш баланс: {round(new_balanse, 3)} вив.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)        
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')
def buy_xrp(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,))
    xrp = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество XRP для покупки\nВаш баланс: {xrp:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, buy_xrp_1)
def buy_xrp_1(message):
    try:
        xrp = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        xrp_price = cursor.execute('SELECT xrp FROM crypto_price').fetchone()[0]
        if xrp <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if xrp * xrp_price > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств')
            return
        cursor.execute('UPDATE crypto SET xrp = ? WHERE user_id = ?', (cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] + xrp, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - xrp * xrp_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно купили {xrp:.8f} XRP\n"
        f"💰 Ваш баланс: {round(new_balanse, 3)} вив.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)        
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')
def buy_doge(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,))
    doge = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество DOGE для покупки\nВаш баланс: {doge:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, buy_doge_1)
def buy_doge_1(message):
    try:
        doge = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        doge_price = cursor.execute('SELECT doge FROM crypto_price').fetchone()[0]
        if doge <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if doge * doge_price > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств')
            return
        cursor.execute('UPDATE crypto SET doge = ? WHERE user_id = ?', (cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] + doge, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - doge * doge_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно купили {doge:.8f} DOGE\n"
        f"💰 Ваш баланс: {round(new_balanse, 3)} вив.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)        
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')
def buy_hmstr(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (user_ids,))
    hmstr = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество HMSTR для покупки\nВаш баланс: {hmstr:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, buy_hmstr_1)
def buy_hmstr_1(message):
    try:
        hmstr = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        hmstr_price = cursor.execute('SELECT hmstr FROM crypto_price').fetchone()[0]
        if hmstr <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if hmstr * hmstr_price > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств')
            return
        cursor.execute('UPDATE crypto SET hmstr = ? WHERE user_id = ?', (cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] + hmstr, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - hmstr * hmstr_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно купили {hmstr:.8f} HMSTR\n"
        f"💰 Ваш баланс: {round(new_balanse, 3)} вив.\n\n"
        "Продолжайте покупки или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)        
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')

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
    bot.send_message(
    message.chat.id,
    text=(
        "Выберите криптовалюту для продажи:\n\n"
        "🔹 **BTC**\n"
        "🔹 **ETH**\n"
        "🔹 **LTC**\n"
        "🔹 **XRP**\n"
        "🔹 **DOGE**\n"
        "🔹 **HMSTR**\n\n"
        "Нажмите на нужную криптовалюту, чтобы продолжить. 👇"
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)

def sale_btc(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (user_ids,))
    btc = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество BTC для продажи\nВаш баланс BTC: {btc:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_btc_1)


def sale_btc_1(message):
    try:
        btc = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        btc_price = cursor.execute('SELECT btc FROM crypto_price').fetchone()[0]
        if btc <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if btc > cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно BTC')
            return
        cursor.execute('UPDATE crypto SET btc = ? WHERE user_id = ?', (cursor.execute('SELECT btc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - btc, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse + btc * btc_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно продали {btc:.8f} BTC\n"
        f"На ваш баланс зачислено {round(btc * btc_price, 3)} вив\n"
        f"Ваш баланс: {round(new_balanse, 3)} вив\n\n"
        "Продолжайте торговать или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(message.from_user.id, "Продажа", round(btc * btc_price, 3), f"Продажа BTC {btc:.8f}")        
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')


def sale_eth(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (user_ids,))
    eth = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество ETH для продажи\nВаш баланс ETH: {eth:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_eth_1)


def sale_eth_1(message):
    try:
        eth = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        eth_price = cursor.execute('SELECT eth FROM crypto_price').fetchone()[0]
        if eth <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if eth > cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно ETH')
            return
        cursor.execute('UPDATE crypto SET eth = ? WHERE user_id = ?', (cursor.execute('SELECT eth FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - eth, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse + eth * eth_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно продали {eth:.8f} ETH\n"
        f"На ваш баланс зачислено {round(eth * eth_price, 3)} вив\n"
        f"Ваш баланс: {round(new_balanse, 3)} вив\n\n"
        "Продолжайте торговать или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(message.from_user.id, "Продажа", round(eth * eth_price, 3), f"Продажа ETH {eth:.8f}")
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')


def sale_ltc(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (user_ids,))
    ltc = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество LTC для продажи\nВаш баланс LTC: {ltc:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_ltc_1)


def sale_ltc_1(message):
    try:
        ltc = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        ltc_price = cursor.execute('SELECT ltc FROM crypto_price').fetchone()[0]
        if ltc <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if ltc > cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно LTC')
            return
        cursor.execute('UPDATE crypto SET ltc = ? WHERE user_id = ?', (cursor.execute('SELECT ltc FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - ltc, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse + ltc * ltc_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно продали {ltc:.8f} LTC\n"
        f"На ваш баланс зачислено {round(ltc * ltc_price, 3)} вив\n"
        f"Ваш баланс: {round(new_balanse, 3)} вив\n\n"
        "Продолжайте торговать или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(message.from_user.id, "Продажа", round(ltc * ltc_price, 3), f"Продажа LTC {ltc:.8f}")
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')


def sale_xrp(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (user_ids,))
    xrp = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество XRP для продажи\nВаш баланс XRP: {xrp:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_xrp_1)


def sale_xrp_1(message):
    try:
        xrp = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        xrp_price = cursor.execute('SELECT xrp FROM crypto_price').fetchone()[0]
        if xrp <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if xrp > cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно XRP')
            return
        cursor.execute('UPDATE crypto SET xrp = ? WHERE user_id = ?', (cursor.execute('SELECT xrp FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - xrp, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse + xrp * xrp_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно продали {xrp:.8f} XRP\n"
        f"На ваш баланс зачислено {round(xrp * xrp_price, 3)} вив\n"
        f"Ваш баланс: {round(new_balanse, 3)} вив\n\n"
        "Продолжайте торговать или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(message.from_user.id, "Продажа", round(xrp * xrp_price, 3), f"Продажа XRP {xrp:.8f}")
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')


def sale_doge(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (user_ids,))
    doge = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество DOGE для продажи\nВаш баланс DOGE: {doge:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_doge_1)


def sale_doge_1(message):
    try:
        doge = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        doge_price = cursor.execute('SELECT doge FROM crypto_price').fetchone()[0]
        if doge <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if doge > cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно DOGE')
            return
        cursor.execute('UPDATE crypto SET doge = ? WHERE user_id = ?', (cursor.execute('SELECT doge FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - doge, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse + doge * doge_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно продали {doge:.8f} DOGE\n"
        f"На ваш баланс зачислено {round(doge * doge_price, 3)} вив\n"
        f"Ваш баланс: {round(new_balanse, 3)} вив\n\n"
        "Продолжайте торговать или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(message.from_user.id, "Продажа", round(doge * doge_price, 3), f"Продажа DOGE {doge:.8f}")
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')


def sale_hmstr(call, user_ids):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    markup.add(back)
    cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (user_ids,))
    hmstr = cursor.fetchone()[0]
    bot.send_message(call.chat.id, text=f'Введите количество HMSTR для продажи\nВаш баланс HMSTR: {hmstr:.8f} ', reply_markup=markup)
    bot.register_next_step_handler(call, sale_hmstr_1)


def sale_hmstr_1(message):
    try:
        hmstr = float(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        hmstr_price = cursor.execute('SELECT hmstr FROM crypto_price').fetchone()[0]
        if hmstr <= 0:
            bot.send_message(message.chat.id, text='Некорректное значение')
            return
        if hmstr > cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]:
            bot.send_message(message.chat.id, text='У вас недостаточно HMSTR')
            return
        cursor.execute('UPDATE crypto SET hmstr = ? WHERE user_id = ?', (cursor.execute('SELECT hmstr FROM crypto WHERE user_id = ?', (message.from_user.id,)).fetchone()[0] - hmstr, message.from_user.id))
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse + hmstr * hmstr_price, message.from_user.id))
        new_balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        conn.commit()
        bot.send_message(
    message.chat.id,
    text=(
        f"Вы успешно продали {hmstr:.8f} HMSTR\n"
        f"На ваш баланс зачислено {round(hmstr * hmstr_price, 3)} вив\n"
        f"Ваш баланс: {round(new_balanse, 3)} вив\n\n"
        "Продолжайте торговать или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
        log_transaction(message.from_user.id, "Продажа", round(hmstr * hmstr_price, 3), f"Продажа HMSTR {hmstr:.8f}")
        bir(message)
    except:
        bot.send_message(message.chat.id, text='Некорректное значение')


def change_mine_crime(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btc = types.KeyboardButton('₿ BTC')
    eth = types.KeyboardButton('Ξ ETH')
    ltc = types.KeyboardButton('Ł LTC')
    xrp = types.KeyboardButton('✕ XRP')
    doge = types.KeyboardButton('Ð DOGE')
    hmstr = types.KeyboardButton('🐹 HMSTR')
    back = types.KeyboardButton('🔙 Назад')
    markup.add(btc, eth, ltc, xrp, doge, hmstr, back)
    bot.send_message(message.chat.id, text='⛏️ Выберите криптовалюту для майнинга (по умолчанию BTC):', reply_markup=markup)


def admin(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    search_user = types.KeyboardButton('Поиск пользователя')
    bid = types.KeyboardButton('Заявки на вывод')
    logs_button = types.KeyboardButton('📜 Логи операций')
    markup.add(search_user, bid, logs_button, back)
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
        log_transaction(user_id, "Пополнение", balanse, f"Пополнение баланса администратором на {balanse} вив")


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
    #bot.send_message(message.chat.id, text='Вы успешно начали игру')
    profile(message)
print('bot is start')


def referal(message):
    ref_cod = cursor.execute('SELECT ref_cod FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    bot.send_message(
    message.chat.id,
    text=(
        "🤝 **Реферальная программа**\n\n"
        "🔹 Приглашайте друзей и получайте бонусы на свой баланс!\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Отправьте свою реферальную ссылку друзьям.\n"
        "2️⃣ Когда друг зарегистрируется, вы получите бонус 1000 вив.\n\n"
        f"🔗 **Ваша реферальная ссылка:**\n"
        f"[https://t.me/PrismaX_official_bot?start={ref_cod}](https://t.me/PrismaX_official_bot?start={ref_cod})\n\n"
        "Поделитесь ссылкой и начните зарабатывать прямо сейчас!"
    ),
    parse_mode="Markdown"
)

# вывод средств на карту
def consolusion(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    card = types.KeyboardButton('На карту')
    markup.add(card, back)
    bot.send_message(
    message.chat.id,
    text=(
        "💳 **Выберите способ вывода средств**\n\n"
        "🔹 **На карту** — вывод средств на банковскую карту.\n\n"
        "Нажмите на нужный способ, чтобы продолжить. 👇"
    ),
    reply_markup=markup
)
def cards(message):
    bot.send_message(message.chat.id, text='Введите номер карты')
    bot.register_next_step_handler(message, card_1)
def card_1(message):
    global num
    num = random.randint(100000, 999999)
    card = message.text
    cursor.execute('INSERT INTO user_data (num, user_id, num_card) VALUES (?, ?, ?)', (num, message.from_user.id, card))
    conn.commit()
    bot.send_message(message.chat.id, text='Введите сумму вывода')
    bot.register_next_step_handler(message, card_2)
def card_2(message):
    global num
    summa = message.text
    cursor.execute('UPDATE user_data SET sum = ? WHERE num = ?', (summa, num))
    conn.commit()
    bot.send_message(message.chat.id, text='Введите название банка')
    bot.register_next_step_handler(message, card_3)

def card_3(message):
    global num
    bank = message.text
    cursor.execute('UPDATE user_data SET bank_card = ? WHERE num = ?', (bank, num))
    conn.commit()
    cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,))
    balanse = cursor.fetchone()[0]
    summa = cursor.execute('SELECT sum FROM user_data WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    if balanse >= int(summa):
        if int(summa) >= 300:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
            markup_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back_admin = types.KeyboardButton('Назад')
            info = types.KeyboardButton('Информация')
            markup_admin.add(info, back_admin)
            cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse - int(summa), message.from_user.id))
            conn.commit()
            bot.send_message(
    message.chat.id,
    text=(
        f"🎉 **Заявка №{num} на вывод средств успешно отправлена!**\n\n"
        "💡 **Что дальше?**\n"
        "1️⃣ Ожидайте обработки заявки администратором.\n"
        "2️⃣ Вы получите уведомление, как только средства будут переведены.\n\n"
    ),
    reply_markup=markup
)            
            log_transaction(message.from_user.id, "Вывод", -int(summa), f"Вывод средств на карту {bank} {summa} вив")
            bot.send_message(2146048678, text=f'Заявка №{num} на вывод для пользователя {message.from_user.id}', reply_markup=markup_admin)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('Назад')
            markup.add(back)
            bot.send_message(
    message.chat.id,
    text=(
        "❌ **Минимальная сумма вывода — 300 руб.**\n\n"
        "💡 **Что можно сделать?**\n"
        "1️⃣ Укажите сумму больше или равную 300 руб.\n"
        "2️⃣ Если у вас возникли вопросы, обратитесь в поддержку.\n\n"
        "Попробуйте снова. 👇"
    ),
    reply_markup=markup
)    
    else:
        bot.send_message(message.chat.id, text='У вас недостаточно средств')
            
def admin_consolusion(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Назад')
    user_id = types.KeyboardButton('Удалить заявку')
    markup.add(user_id, back)
    bid = cursor.execute('SELECT * FROM user_data').fetchall()
    for i in bid:
        bot.send_message(message.chat.id, text=f'ID: {i[0]}\n№ {i[1]}\nПользователь: {i[2]}\nКарта: {i[3]}\nСумма: {i[5]}\nБанк: {i[4]}')
    bot.send_message(message.chat.id, text='Заявки на вывод средств', reply_markup=markup)
def delete_bid(message):
    bot.send_message(message.chat.id, text='Введите ID заявки')
    bot.register_next_step_handler(message, delete_bid_1)
def delete_bid_1(message):
    bid_id = message.text
    cursor.execute('DELETE FROM user_data WHERE id = ?', (bid_id,))
    conn.commit()
    bot.send_message(message.chat.id, text='Заявка успешно удалена')

def admin_logs(message):

    logs = cursor.execute(
        'SELECT user_id, type, amount, timestamp, details FROM transactions ORDER BY timestamp DESC LIMIT 20'
    ).fetchall()

    if not logs:
        bot.send_message(message.chat.id, text="Логи пусты.")
        return

    log_text = "📜 **Логи операций:**\n\n"
    for log in logs:
        user_id, operation_type, amount, timestamp, details = log
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        log_text += f"🔹 Пользователь: {user_id}\n"
        log_text += f"   Тип: {operation_type}\n"
        log_text += f"   Сумма: {amount:.2f}\n"
        log_text += f"   Дата: {date}\n"
        if details:
            log_text += f"   Детали: {details}\n"
        log_text += "\n"

    bot.send_message(message.chat.id, text=log_text, parse_mode="Markdown")


###casino_game###

'''
def casino_game_menu(message):
    markup = types.InlineKeyboardMarkup()
    roulette = types.InlineKeyboardButton(text='🎡 Рулетка', callback_data='roulette')
    mines = types.InlineKeyboardButton(text='💣 Мины', callback_data='mines')
    slots = types.InlineKeyboardButton(text='🎰 Слоты', callback_data='slots')
    back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='back')
    markup.add(roulette, mines, slots, back)
    balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    bot.send_message(
    message.chat.id,
    text=(
        "🎰 **Добро пожаловать в казино!**\n\n"
        "🔹 Здесь вы можете испытать удачу в различных играх.\n\n"
        "💡 **Доступные игры:**\n"
        "🎡 **Рулетка** — угадайте цвет или номер и получите выигрыш.\n"
        "💣 **Мины** — откройте ячейки, избегая мин, чтобы увеличить выигрыш.\n"
        "🎰 **Слоты** — крутите барабаны и выигрывайте призы.\n\n"
        f"💰 **Ваш текущий баланс:** {balanse_viv:.3f} вив.\n\n"
        "Выберите игру ниже и начните играть. Удачи! 🍀"
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)


def roulette(message):
    markup = types.InlineKeyboardMarkup()
    red = types.InlineKeyboardButton(text='Красный (x2)', callback_data='red')
    black = types.InlineKeyboardButton(text='Чёрный (x2)', callback_data='black')
    green = types.InlineKeyboardButton(text='Зелёный (x36)', callback_data='green')
    number = types.InlineKeyboardButton(text='Ставка на номер (x36)', callback_data='number')
    back = types.InlineKeyboardButton(text='Назад', callback_data='casino_game_menu')
    markup.add(red, black, green, number, back)
    bot.send_message(message.chat.id, text='Выберите тип ставки:', reply_markup=markup)


def roulette_result(message, bet_type, bet_amount, bet_number=None):
    # Генерация серверного сида и хэша
    server_seed, server_hash = generate_server_seed()
    client_seed = str(message.from_user.id)  # Используем ID пользователя как клиентский сид
    nonce = random.randint(1, 1000000)  # Уникальный идентификатор игры

    # Генерация результата
    result_number = generate_game_result(server_seed, client_seed, nonce)
    result_color = 'green' if result_number == 0 else ('red' if result_number % 2 == 0 else 'black')

    # Отправляем хэш серверного сида игроку
    # bot.send_message(message.chat.id, text=f"Хэш серверного сида: {server_hash}")

    # Проверка результата
    if bet_type == 'color':
        if bet_number == result_color:
            winnings = rub_to_viv(bet_amount * 2)
            bot.send_message(
    message.chat.id,
    text=(
        f"🎉 **Поздравляем!**\n\n"
        f"Вы выиграли! Выпало {result_color} {result_number}.\n"
        f"Ваш выигрыш: {viv_to_rub(winnings)} вив.\n\n"
        "Продолжайте играть или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)           
            bal = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (bal + winnings, message.from_user.id))
            conn.commit()
        else:
            bot.send_message(
    message.chat.id,
    text=(
        f"❌ **Вы проиграли.**\n\n"
        f"Выпало: {result_color} {result_number}.\n\n"
        "Попробуйте снова или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)    
    elif bet_type == 'number':
        if bet_number == result_number:
            winnings = rub_to_viv(bet_amount * 36)
            bot.send_message(
    message.chat.id,
    text=(
        f"🎉 **Поздравляем!**\n\n"
        f"Вы выиграли! Выпало число {result_number}.\n"
        f"Ваш выигрыш: {viv_to_rub(winnings)} вив.\n\n"
        "Продолжайте играть или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)            
            bal = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (bal + winnings, message.from_user.id))
            conn.commit()
        else:
            bot.send_message(
    message.chat.id,
    text=(
        f"❌ **Вы проиграли.**\n\n"
        f"Выпало число {result_number}.\n\n"
        "Попробуйте снова или вернитесь в главное меню. 👇"
    ),
    parse_mode="Markdown"
)
    # Отправляем игроку серверный сид для проверки
    #bot.send_message(message.chat.id, text=f"Серверный сид (для проверки): {server_seed}")


def generate_server_seed():
    # Генерация случайного серверного сида и его хэша
    server_seed = str(random.getrandbits(256))
    server_hash = hashlib.sha256(server_seed.encode()).hexdigest()
    return server_seed, server_hash


def generate_game_result(server_seed, client_seed, nonce):
    # Генерация результата игры на основе серверного и клиентского сидов
    seed = server_seed + client_seed + str(nonce)
    random.seed(seed)
    result = random.randint(0, 36)  # Результат от 0 до 36
    return result


def roulette_bet_color(call, color):
    # Запрос ставки
    msg = bot.send_message(call.message.chat.id, text=f'Введите сумму ставки на {color}:')
    bot.register_next_step_handler(msg, process_bet_color, color)


def process_bet_color(message, color):
    try:
        bet_amount = int(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if bet_amount > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств для ставки.')
            return
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - bet_amount, message.from_user.id))
        conn.commit()
        roulette_result(message, 'color', bet_amount, color)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


def roulette_bet_number(call):
    # Запрос ставки на номер
    msg = bot.send_message(
    call.message.chat.id,
    text=(
        "Введите номер (0-36), на который хотите поставить:\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Укажите номер от 0 до 36.\n"
        "2️⃣ Подтвердите ставку и ожидайте результата.\n\n"
        "Удачи! 🍀"
    )
)    
    bot.register_next_step_handler(msg, process_bet_number)


def process_bet_number(message):
    try:
        bet_number = int(message.text)
        if bet_number < 0 or bet_number > 36:
            bot.send_message(message.chat.id, text='Введите номер от 0 до 36.')
            return
        msg = bot.send_message(message.chat.id, text=f'Введите сумму ставки на номер {bet_number}:')
        bot.register_next_step_handler(msg, process_bet_number_amount, bet_number)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


def process_bet_number_amount(message, bet_number):
    try:
        bet_amount = int(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if bet_amount > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств для ставки.')
            return
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - bet_amount, message.from_user.id))
        conn.commit()
        roulette_result(message, 'number', bet_amount, bet_number)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


def mines_game_menu(message):
    markup = types.InlineKeyboardMarkup()
    start_game = types.InlineKeyboardButton(text='Начать игру', callback_data='start_mines_game')
    back = types.InlineKeyboardButton(text='Назад', callback_data='casino_game_menu')
    markup.add(start_game, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Добро пожаловать в игру \"Мины\".\n\n"
        "Нажмите \"Начать игру\", чтобы начать.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Укажите сумму ставки.\n"
        "2️⃣ Выберите количество мин.\n"
        "3️⃣ Открывайте ячейки, избегая мин, чтобы увеличить выигрыш.\n\n"
        "Удачи! 🍀"
    ),
    reply_markup=markup
)

def start_mines_game(message):
    msg = bot.send_message(message.chat.id, text='Введите сумму ставки:')
    bot.register_next_step_handler(msg, process_mines_bet)


def process_mines_bet(message):
    try:
        bet_amount = int(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if bet_amount > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств для ставки.')
            return
        if bet_amount <= 0:
            bot.send_message(message.chat.id, text='Ставка должна быть больше 0.')
            return

        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - bet_amount, message.from_user.id))
        conn.commit()
        msg = bot.send_message(message.chat.id, text='Введите количество бомб (1-24):')
        bot.register_next_step_handler(msg, process_bomb_count, bet_amount)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


def process_bomb_count(message, bet_amount):
    try:
        bomb_count = int(message.text)
        if bomb_count < 1 or bomb_count > 24:
            bot.send_message(message.chat.id, text='Количество бомб должно быть от 1 до 24.')
            return
        bot.send_message(message.chat.id, text=f'Игра началась! Ваша ставка: {bet_amount} руб.\nВыберите ячейку (1-25):')
        start_mines_round(message, bet_amount, [], bomb_count)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


def start_mines_round(message, bet_amount, opened_cells, bomb_count):
    total_cells = 25
    bombs = random.sample(range(1, total_cells + 1), bomb_count)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    buttons = []
    for i in range(1, total_cells + 1):
        if i in opened_cells:
            buttons.append(types.KeyboardButton(f' '))
        else:
            buttons.append(types.KeyboardButton(str(i)))
        if len(buttons) == 5:  # Добавляем строку из 5 кнопок
            markup.add(*buttons)
            buttons = []
    if buttons:  # Добавляем оставшиеся кнопки, если они есть
        markup.add(*buttons)
    back = types.KeyboardButton('Забрать выигрыш')
    markup.add(back)

    bot.send_message(message.chat.id, text='Выберите ячейку:', reply_markup=markup)
    bot.register_next_step_handler(message, process_mines_choice, bet_amount, bombs, opened_cells, bomb_count)


def process_mines_choice(message, bet_amount, bombs, opened_cells, bomb_count):
    try:
        if message.text == 'Забрать выигрыш':
            multiplier = 1 + len(opened_cells) * (len(bombs) / 25)  # Реалистичный рост множителя
            winnings = round(bet_amount * multiplier, 2)
            balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
            cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse + winnings, message.from_user.id))
            conn.commit()
            bot.send_message(message.chat.id, text=f'Вы забрали выигрыш: {winnings} руб.')
            casino_game_menu(message)
            return

        choice = int(message.text)
        if choice < 1 or choice > 25 or choice in opened_cells:
            bot.send_message(message.chat.id, text='Некорректный выбор. Попробуйте снова.')
            start_mines_round(message, bet_amount, opened_cells, bomb_count)
            return

        if choice in bombs:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
            buttons = []
            for i in range(1, 26):
                if i in bombs:
                    buttons.append(types.KeyboardButton('💣'))  # Отображение мины
                elif i in opened_cells:
                    buttons.append(types.KeyboardButton(f' '))
                else:
                    buttons.append(types.KeyboardButton(str(i)))
                if len(buttons) == 5:  # Добавляем строку из 5 кнопок
                    markup.add(*buttons)
                    buttons = []
            if buttons:  # Добавляем оставшиеся кнопки, если они есть
                markup.add(*buttons)
            bot.send_message(
    message.chat.id,
    text=(
        f"💣 **Вы попали на мину!**\n\n"
        f"Вы проиграли свою ставку: {bet_amount} руб.\n\n"
        "Попробуйте снова или вернитесь в главное меню. 👇"
    ),
    reply_markup=markup
)            
            casino_game_menu(message)
        else:
            opened_cells.append(choice)
            multiplier = 1 + len(opened_cells) * (len(bombs) / 25)  ## Реалистичный рост множителя
            potential_winnings = round(bet_amount * multiplier, 2)
            bot.send_message(
                message.chat.id,
                text=f'Вы открыли ячейку {choice}. Продолжайте!\n\nТекущий множитель: x{multiplier:.2f}\nСумма, которую вы можете забрать: {potential_winnings} руб.'
            )
            start_mines_round(message, bet_amount, opened_cells, bomb_count)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


def slots_game_menu(message):
    markup = types.InlineKeyboardMarkup()
    start_game = types.InlineKeyboardButton(text='🎰 Играть в слоты', callback_data='start_slots_game')
    back = types.InlineKeyboardButton(text='🔙 Назад', callback_data='casino_game_menu')
    markup.add(start_game, back)
    bot.send_message(
    message.chat.id,
    text=(
        "Добро пожаловать в игру \"Слоты\".\n\n"
        "Нажмите \"Играть в слоты\", чтобы начать.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Укажите сумму ставки.\n"
        "2️⃣ Крутите барабаны и ждите результата.\n"
        "3️⃣ Заберите свой выигрыш или попробуйте снова.\n\n"
        "Удачи! 🍀"
    ),
    reply_markup=markup
)

def start_slots_game(message):
    msg = bot.send_message(message.chat.id, text='Введите сумму ставки:')
    bot.register_next_step_handler(msg, process_slots_bet)


def process_slots_bet(message):
    try:
        bet_amount = int(message.text)
        balanse = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if bet_amount > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств для ставки.')
            return
        if bet_amount <= 0:
            bot.send_message(message.chat.id, text='Ставка должна быть больше 0.')
            return

        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse - bet_amount, message.from_user.id))
        conn.commit()
        play_slots(message, bet_amount)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


def play_slots(message, bet_amount):
    symbols = ['🍒', '🍋', '🍉', '⭐', '🔔', '7️⃣', '🍇', '🍓', '🍍', '💎', '💰']
    result = [random.choice(symbols) for _ in range(6)]
    bot.send_message(message.chat.id, text=f'🎰 Результат: {" | ".join(result)}')

    if len(set(result)) == 1:  # Все шесть символов совпадают
        multiplier = 10
        winnings = rub_to_viv(bet_amount * multiplier)
        bot.send_message(message.chat.id, text=f'🎉 Джекпот! Все символы совпали! Вы выиграли {viv_to_rub(winnings)} вив.')
    elif len(set(result)) <= 3:  # Три или меньше уникальных символов
        multiplier = 5
        winnings = rub_to_viv(bet_amount * multiplier)
        bot.send_message(message.chat.id, text=f'✨ Отличный результат! Вы выиграли {viv_to_rub(winnings)} вив.')
    elif len(set(result)) <= 4:  # Четыре уникальных символа
        multiplier = 2
        winnings = rub_to_viv(bet_amount * multiplier)
        bot.send_message(message.chat.id, text=f'😊 Хороший результат! Вы выиграли {viv_to_rub(winnings)} вив.')
    else:  # Пять или шесть уникальных символов
        winnings = 0
        bot.send_message(message.chat.id, text='😢 Вы проиграли.')

    if winnings > 0:
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        cursor.execute('UPDATE user SET balanse_viv = ? WHERE user_id = ?', (balanse_viv + winnings, message.from_user.id))
        conn.commit()

    slots_game_menu(message)
'''

def conversion_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    to_viv = types.KeyboardButton('рубли в вив')
    to_rub = types.KeyboardButton('вив в рубли')
    back = types.KeyboardButton('🔙 Назад')
    markup.add(to_viv, to_rub, back)
    balanse_rub = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
    bot.send_message(
    message.chat.id,
    text=(
        "💱 **Конвертация валют**\n\n"
        "🔹 Здесь вы можете конвертировать рубли в вив и наоборот.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Выберите направление конвертации.\n"
        "2️⃣ Укажите сумму для конвертации.\n"
        "3️⃣ Подтвердите действие.\n\n"
        "4️⃣ Комиссия: 5% от суммы.\n\n"
        "💡 **Курс конвертации:**\n"
        "1 рубль = 100 вив\n"
        f"💰 **Ваш текущий баланс:**\n"
        f"Рубли: {balanse_rub:.3f} руб.\n"
        f"Вив: {balanse_viv:.3f} вив.\n\n"
        "Выберите действие ниже. 👇"
    ),
    reply_markup=markup,
    parse_mode="Markdown"
)


def convert_rub_to_viv(message):
    msg = bot.send_message(message.chat.id, text='Введите количество рублей для конвертации в вив:')
    bot.register_next_step_handler(msg, process_rub_to_viv)


def process_rub_to_viv(message):
    try:
        rub = int(message.text)
        if rub <= 0:
            bot.send_message(message.chat.id, text='Введите положительное число.')
            return
        balanse_rub = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if rub > balanse_rub:
            bot.send_message(message.chat.id, text='У вас недостаточно рублей для конвертации.')
            return
        viv = rub_to_viv(rub * 0.95)  # Учитываем комиссию 5%
        cursor.execute('UPDATE user SET balanse = ?, balanse_viv = balanse_viv + ? WHERE user_id = ?', (balanse_rub - rub, viv, message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text=f'Вы успешно конвертировали {rub} рублей в {viv} вив.')
        conversion_menu(message)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


def convert_viv_to_rub(message):
    msg = bot.send_message(message.chat.id, text='Введите количество вив для конвертации в рубли:')
    bot.register_next_step_handler(msg, process_viv_to_rub)


def process_viv_to_rub(message):
    try:
        viv = int(message.text)
        if viv <= 0:
            bot.send_message(message.chat.id, text='Введите положительное число.')
            return
        balanse_viv = cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if viv > balanse_viv:
            bot.send_message(message.chat.id, text='У вас недостаточно вив для конвертации.')
            return
        rub = viv_to_rub(viv * 0.95)  # Учитываем комиссию 5%
        cursor.execute('UPDATE user SET balanse_viv = ?, balanse = balanse + ? WHERE user_id = ?', (balanse_viv - viv, rub, message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text=f'Вы успешно конвертировали {viv} вив в {rub} рублей.')
        conversion_menu(message)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')


# Функция для генерации ссылки на оплату через ЮMoney
def generate_yoomoney_payment_link(amount, label):
    base_url = "https://yoomoney.ru/quickpay/confirm.xml"
    params = {
        "receiver": "4100118995621972",  # Замените на ваш номер кошелька ЮMoney
        "quickpay-form": "shop",
        "targets": f"Пополнение баланса",
        "paymentType": "AC",  # Банковская карта
        "sum": amount,
        "label": label
    }
    query_string = urllib.parse.urlencode(params)
    return f"{base_url}?{query_string}"

def yoomoney_payment(message):
    try:
        msg = bot.send_message(
    message.chat.id,
    text=(
        "💳 **Пополнение баланса**\n\n"
        "🔹 Укажите сумму, на которую вы хотите пополнить баланс.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Введите сумму пополнения.\n"
        "2️⃣ Перейдите по сгенерированной ссылке для оплаты.\n"
        "3️⃣ После оплаты баланс будет автоматически пополнен.\n\n"
        "Введите сумму ниже. 👇"
    )
)
        bot.register_next_step_handler(msg, process_yoomoney_payment)
    except Exception as e:
        bot.send_message(message.chat.id, text="Произошла ошибка. Попробуйте снова.")

# Функция для обработки платежа через ЮMoney
def process_yoomoney_payment(message):
    try:
        amount = int(message.text)
        if amount <= 0:
            bot.send_message(message.chat.id, text="Введите положительное число.")
            return

        # Генерация уникального идентификатора платежа
        payment_label = f"{message.from_user.id}_{int(time.time())}"

        # Генерация ссылки на оплату
        payment_link = generate_yoomoney_payment_link(amount, payment_label)
        bot.send_message(message.chat.id,text=(
        "💳 **Пополнение баланса**\n\n"
        "🔹 Для пополнения баланса перейдите по ссылке ниже и выполните оплату.\n\n"
        "💡 **Как это работает?**\n"
        "1️⃣ Перейдите по ссылке для оплаты.\n"
        "2️⃣ После успешной оплаты баланс будет автоматически пополнен.\n\n"
        f"🔗 **Ссылка для пополнения:** [Перейти к оплате]({payment_link})\n\n"
        "После оплаты, баланс будет автоматически пополнен. Если возникли проблемы, обратитесь в поддержку."
        ), parse_mode="Markdown")

        # Сохраняем информацию о платеже в базу данных
        cursor.execute(
            'INSERT INTO pending_payments (user_id, label, amount) VALUES (?, ?, ?)',
            (message.from_user.id, payment_label, amount)
        )
        conn.commit()
        print(f"Сохраняем платеж: user_id={message.from_user.id}, label={payment_label}, amount={amount}")
    except ValueError:
        bot.send_message(message.chat.id, text="Введите корректное число.")


def get_yoomoney_token(client_id, redirect_uri, scope):
    """
    Функция для получения токена ЮMoney через OAuth2.
    """
    auth_url = f"https://yoomoney.ru/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}"
    print(f"Перейдите по следующей ссылке для авторизации: {auth_url}")
    auth_code = input("Введите код авторизации: ")

    token_url = "https://yoomoney.ru/oauth/token"
    data = {
        "code": auth_code,
        "client_id": client_id,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token = response.json().get("access_token")
        print(f"Токен успешно получен: {token}")
        return token
    else:
        print(f"Ошибка получения токена: {response.status_code}, {response.text}")
        return None

# Пример использования функции get_yoomoney_token
client_id = "5834FAC7D6FB0A2CC219FDE0B20250EC691A2BC438F14699A88023253F095AB9"  # Замените на ваш client_id
redirect_uri = "http://194.87.95.213:8000/callback"  # Укажите ваш redirect_uri
scope = "account-info operation-history"  # Укажите необходимые права
token = get_yoomoney_token(client_id, redirect_uri, scope)

# Функция для проверки платежей через API ЮMoney
def check_yoomoney_payments():
    while True:
        try:
            if not token:
                print("Ошибка: Токен ЮMoney не задан.")
                time.sleep(60)
                continue

            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get("https://yoomoney.ru/api/operation-history", headers=headers)

            if response.status_code == 200:
                operations = response.json().get("operations", [])
                print(f"Получено операций: {len(operations)}")  # Логируем количество операций
                for operation in operations:
                    print(f"Обработка операции: {operation}")  # Логируем данные операции
                    if operation.get("status") == "success" and "label" in operation:
                        label = operation["label"]
                        amount = float(operation["amount"])

                        # Проверяем, есть ли такой платеж в ожидающих
                        pending_payment = cursor.execute(
                            'SELECT user_id, amount FROM pending_payments WHERE label = ?',
                            (label,)
                        ).fetchone()
                        print(f"Проверяем платеж с меткой {label}: {pending_payment}")  # Логируем проверку платежа
                        # Если платеж найден, проверяем сумму

                        if pending_payment:
                            user_id, expected_amount = pending_payment

                            # Проверяем, совпадает ли сумма
                            if abs((expected_amount - expected_amount * 0.03) - amount) < 0.01:  # Допустимая погрешность 3%
                                # Пополняем баланс пользователя
                                balanse = cursor.execute(
                                    'SELECT balanse FROM user WHERE user_id = ?',
                                    (user_id,)
                                ).fetchone()[0]
                                cursor.execute(
                                    'UPDATE user SET balanse = ? WHERE user_id = ?',
                                    (balanse + amount, user_id)
                                )

                                # Удаляем запись из ожидающих платежей
                                cursor.execute(
                                    'DELETE FROM pending_payments WHERE label = ?',
                                    (label,)
                                )
                                conn.commit()

                                # Уведомляем пользователя
                                bot.send_message(user_id, text=f"Ваш баланс успешно пополнен на {amount} руб.")
                                bot.send_message(2146048678, text=f"Баланс пользователя {user_id} пополнен на {amount} руб.")
                                print(f"Баланс пользователя {user_id} пополнен на {amount} руб.")
                                log_transaction(user_id, "Пополнение", amount, "Пополнение через ЮMoney")
                            else:
                                print(f"Сумма платежа {amount} не совпадает с ожидаемой {expected_amount}.")
                        else:
                            print(f"Платеж с меткой {label} не найден в ожидающих.")
                            print(cursor.execute('SELECT * FROM pending_payments').fetchall())
            elif response.status_code == 401:
                print("Ошибка API ЮMoney: Неверный токен авторизации. Проверьте токен.")
            else:
                print(f"Ошибка API ЮMoney: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Ошибка при проверке платежей: {e}")
        time.sleep(60)  # Проверяем каждые 60 секунд


# Создаем таблицу для хранения ожидающих платежей
cursor.execute('''
CREATE TABLE IF NOT EXISTS pending_payments (
    user_id INTEGER,
    label TEXT PRIMARY KEY,
    amount REAL
)
''')
conn.commit()

# Запускаем проверку платежей в отдельном потоке
threading.Thread(target=check_yoomoney_payments, daemon=True).start()

def log_transaction(user_id, operation_type, amount, details=""):
    timestamp = time.time()
    cursor.execute(
        'INSERT INTO transactions (user_id, type, amount, timestamp, details) VALUES (?, ?, ?, ?, ?)',
        (user_id, operation_type, amount, timestamp, details)
    )
    conn.commit()

def transaction_history(message):
    user_id = message.from_user.id
    transactions = cursor.execute(
        'SELECT type, amount, timestamp, details FROM transactions WHERE user_id = ? ORDER BY timestamp DESC LIMIT 10',
        (user_id,)
    ).fetchall()

    if not transactions:
        bot.send_message(message.chat.id, text="У вас пока нет операций.")
        return

    history = "📜 **История операций:**\n\n"
    for t in transactions:
        operation_type, amount, timestamp, details = t
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        history += f"🔹 {operation_type}\n"
        history += f"   Сумма: {amount:.3f}\n"
        history += f"   Дата: {date}\n"
        if details:
            history += f"   Детали: {details}\n"
        history += "\n"

    bot.send_message(message.chat.id, text=history, parse_mode="Markdown")

def rating(message):
    # Получаем топ-100 пользователей, отсортированных по балансу вив
    top_users = cursor.execute(
        'SELECT user_id, user_name, balanse_viv FROM user ORDER BY balanse_viv DESC LIMIT 100'
    ).fetchall()

    # Формируем текст для отображения рейтинга
    rating_text = "🏆 **Топ-100 пользователей:**\n\n"
    for idx, user in enumerate(top_users, start=1):
        user_id, user_name, balanse_viv = user

        # Суммируем доходы из таблицы card_common (обычные карты)
        common_income = cursor.execute(
            'SELECT SUM(gtx_1080_ti + gtx_1080 + gtx_2060 + gtx_2070 + gtx_2080 + gtx_2080_ti + rtx_3060 + rtx_3060_ti + rtx_3070 + rtx_3070_ti) FROM card_common WHERE user_id = ?',
            (user_id,)
        ).fetchone()[0] or 0

        # Суммируем доходы из таблицы card (премиум карты)
        premium_income = cursor.execute(
            'SELECT SUM(rtx_5090 + rtx_4090 + rtx_3090_ti + rtx_3090 + rtx_3080_ti + rtx_3080 + ice_river_aeo + goldshell_ae_box + goldshell_ae_box_pro + goldshell_ae_box_ii) FROM card WHERE user_id = ?',
            (user_id,)
        ).fetchone()[0] or 0

        # Общий доход
        total_income = common_income + premium_income

        rating_text += f"{idx}. {user_name or 'Без имени'} (ID: {user_id})\n"
        rating_text += f"   💰 Баланс: {balanse_viv:.3f} вив\n"
        rating_text += f"   📈 Общий доход: {total_income:.3f} вив/мес\n\n"

    # Определяем место текущего пользователя
    user_id = message.from_user.id
    user_rank = cursor.execute(
        'SELECT COUNT(*) + 1 FROM user WHERE balanse_viv > (SELECT balanse_viv FROM user WHERE user_id = ?)',
        (user_id,)
    ).fetchone()[0]

    user_balanse_viv = cursor.execute(
        'SELECT balanse_viv FROM user WHERE user_id = ?',
        (user_id,)
    ).fetchone()[0] or 0

    # Считаем общий доход текущего пользователя
    user_common_income = cursor.execute(
        'SELECT SUM(gtx_1080_ti + gtx_1080 + gtx_2060 + gtx_2070 + gtx_2080 + gtx_2080_ti + rtx_3060 + rtx_3060_ti + rtx_3070 + rtx_3070_ti) FROM card_common WHERE user_id = ?',
        (user_id,)
    ).fetchone()[0] or 0

    user_premium_income = cursor.execute(
        'SELECT SUM(rtx_5090 + rtx_4090 + rtx_3090_ti + rtx_3090 + rtx_3080_ti + rtx_3080 + ice_river_aeo + goldshell_ae_box + goldshell_ae_box_pro + goldshell_ae_box_ii) FROM card WHERE user_id = ?',
        (user_id,)
    ).fetchone()[0] or 0

    user_total_income = user_common_income + user_premium_income

    rating_text += f"📊 **Ваше место в рейтинге:** {user_rank}\n"
    rating_text += f"   💰 Ваш баланс: {user_balanse_viv:.3f} вив\n"
    rating_text += f"   📈 Ваш общий доход: {user_total_income:.3f} вив/мес\n"

    # Отправляем сообщение пользователю
    bot.send_message(message.chat.id, text=rating_text, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    user_ids = call.from_user.id  # Используем call.from_user.id для получения ID пользователя
    print(f"Callback from user ID: {user_ids}")
    if call.data == 'sale':
        sale(call.message)
    elif call.data == 'buy':
        buy(call.message)
    elif call.data == 'back':
        # print(cursor.execute('SELECT admin FROM user WHERE user_id = ?', (call.message.from_user.id,)).fetchall())
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
    elif call.data == 'buy_1080_ti':
        buy_1080_ti(call.message, user_ids)
    elif call.data == 'buy_1080':
        buy_1080(call.message, user_ids)
    elif call.data == 'buy_2060':
        buy_2060(call.message, user_ids)
    elif call.data == 'buy_2070':
        buy_2070(call.message, user_ids)
    elif call.data == 'buy_2080':
        buy_2080(call.message, user_ids)
    elif call.data == 'buy_2080_ti':
        buy_2080_ti(call.message, user_ids)
    elif call.data == 'buy_3060':
        buy_3060(call.message, user_ids)
    elif call.data == 'buy_3060_ti':
        buy_3060_ti(call.message, user_ids)
    elif call.data == 'buy_3070':
        buy_3070(call.message, user_ids)
    elif call.data == 'buy_3070_ti':
        buy_3070_ti(call.message, user_ids)
    elif call.data == 'btc_buy':
        buy_btc(call.message, user_ids)
    elif call.data == 'eth_buy':
        buy_eth(call.message, user_ids)
    elif call.data == 'ltc_buy':
        buy_ltc(call.message, user_ids)
    elif call.data == 'xrp_buy':
        buy_xrp(call.message, user_ids)
    elif call.data == 'doge_buy':
        buy_doge(call.message, user_ids)
    elif call.data == 'hmstr_buy':
        buy_hmstr(call.message, user_ids)
    elif call.data == 'invest':
        invest(call.message)
    else:
        print(f"Unknown callback data: {call.data}")
        pass


# Пример изменения текста в функции text
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == '👤 Профиль':
        profile(message)
    elif message.text == '💳 Пополнить Баланс':
        yoomoney_payment(message)
    #elif message.text == '💵 100':
    #    bot.send_message(message.chat.id, text='Вы пополнили баланс на 100 вив')
    #    give_balanse(user_id=message.from_user.id, balanse_viv=rub_to_viv(100) + cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
    #    menu(message)
    #elif message.text == '💵 200':
    #    bot.send_message(message.chat.id, text='Вы пополнили баланс на 200 вив')
    #    give_balanse(user_id=message.from_user.id, balanse_viv=rub_to_viv(200) + cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
    #    menu(message)
    #elif message.text == '💵 300':
    #    bot.send_message(message.chat.id, text='Вы пополнили баланс на 300')
    #    give_balanse(user_id=message.from_user.id, balanse_viv=rub_to_viv(300) + cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
    #    menu(message)
    #elif message.text == '💵 400':
    #    bot.send_message(message.chat.id, text='Вы пополнили баланс на 400')
    #    give_balanse(user_id=message.from_user.id, balanse_viv=rub_to_viv(400) + cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
    #    menu(message)
    #elif message.text == '💵 500':
    #    bot.send_message(message.chat.id, text='Вы пополнили баланс на 500')
    #    give_balanse(user_id=message.from_user.id, balanse_viv=rub_to_viv(500) + cursor.execute('SELECT balanse_viv FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0])
    #    menu(message)
    elif message.text == '🔧 Админ':
        if message.from_user.id == 2146048678:
            admin(message)
    elif message.text == '💎 Премиум магазин':
        shop_1(message)
    elif message.text == '📈 Биржа':
        bir(message)
    elif message.text == '🔙 Назад' or message.text == 'Назад':
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
        if message.from_user.id == 2146048678:
            search_users(message)
    elif message.text == 'Добавить баланс':
        if message.from_user.id == 2146048678:
            add_balanse(message)
    elif message.text == 'Убрать баланс':
        #remove_balanse(message)
        pass
    elif message.text == '₿ BTC':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('BTC', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг BTC')
        profile(message)
    elif message.text == 'Ξ ETH':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('ETH', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг ETH')
        profile(message)
    elif message.text == 'Ł LTC':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('LTC', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг LTC')
        profile(message)
    elif message.text == '✕ XRP':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('XRP', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг XRP')
        profile(message)
    elif message.text == 'Ð DOGE':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('DOGE', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг DOGE')
        profile(message)
    elif message.text == '🐹 HMSTR':
        cursor.execute('UPDATE user SET mining = ? WHERE user_id = ?', ('HMSTR', message.from_user.id))
        conn.commit()
        bot.send_message(message.chat.id, text='Вы выбрали майнинг HMSTR')
        profile(message)
    elif message.text == '⛏️ Выбор криптовалюты':
        change_mine_crime(message)
    elif message.text == '🎁 Забрать стартовый пакет':
        start_pack(message)
    elif message.text == 'Начать':
        start_pack_1(message)
    elif message.text == '🛒 Магазин':
        shop_common(message)
    elif message.text == '🤝 Рефер. прог.':
        referal(message)
    elif message.text == '🖥️ GTX 1080 TI':
        gtx_1080_ti(message)
    elif message.text == '🖥️ GTX 1080':
        gtx_1080(message)
    elif message.text == '🖥️ GTX 2060':
        gtx_2060(message)
    elif message.text == '🖥️ GTX 2070':
        gtx_2070(message)
    elif message.text == '🖥️ GTX 2080':
        gtx_2080(message)
    elif message.text == '🖥️ GTX 2080 TI':
        gtx_2080_ti(message)
    elif message.text == '🖥️ RTX 3060':
        rtx_3060(message)
    elif message.text == '🖥️ RTX 3060 TI':
        rtx_3060_ti(message)
    elif message.text == '🖥️ RTX 3070':
        rtx_3070(message)
    elif message.text == '🖥️ RTX 3070 TI':
        rtx_3070_ti(message)
    elif message.text == 'рубли в вив':
        convert_rub_to_viv(message)
    elif message.text == 'вив в рубли':
        convert_viv_to_rub(message)
    elif message.text == 'Конвертация валют':
        conversion_menu(message)
    elif message.text == '💳 Вывести Баланс':
        consolusion(message)
    elif message.text == 'Заявки на вывод' or message.text == 'Информация':
        if message.from_user.id == 2146048678:
            admin_consolusion(message)
    elif message.text == 'На карту':
        cards(message)
    elif message.text == 'Удалить заявку':
        if message.from_user.id == 2146048678:
            delete_bid(message)
    elif message.text == '🎲 События':
        event.event_start(message)
    elif message.text == '🎁 Ежедневный бонус':
        daily_bonus(message)
        profile(message)
    elif message.text == '📜 История операций':
        transaction_history(message)
    elif message.text == '📜 Логи операций':
        admin_logs(message)
    elif message.text == '💎 Купить премиум':
        premium_menu(message)
    elif message.text == 'Рейтинг':
        rating(message)
    else:
        bot.send_message(message.chat.id, text='Я не понимаю')


def main():
    bot.polling(non_stop=True)


if __name__ == '__main__':
    main()