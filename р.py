import random

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
    # Генерация случайного результата рулетки
    result_number = random.randint(0, 36)
    result_color = 'green' if result_number == 0 else ('red' if result_number % 2 == 0 else 'black')

    # Проверка результата
    if bet_type == 'color':
        if bet_number == result_color:
            winnings = bet_amount * 2
            bot.send_message(message.chat.id, text=f'Вы выиграли! Выпало {result_color} {result_number}. Ваш выигрыш: {winnings} руб.')
            give_balanse(user_id=message.from_user.id, balanse=winnings)
        else:
            bot.send_message(message.chat.id, text=f'Вы проиграли. Выпало {result_color} {result_number}.')
    elif bet_type == 'number':
        if bet_number == result_number:
            winnings = bet_amount * 36
            bot.send_message(message.chat.id, text=f'Вы выиграли! Выпало число {result_number}. Ваш выигрыш: {winnings} руб.')
            give_balanse(user_id=message.from_user.id, balanse=winnings)
        else:
            bot.send_message(message.chat.id, text=f'Вы проиграли. Выпало число {result_number}.')

def roulette_bet_color(call, color):
    # Запрос ставки
    msg = bot.send_message(call.message.chat.id, text=f'Введите сумму ставки на {color}:')
    bot.register_next_step_handler(msg, process_bet_color, color)

def process_bet_color(message, color):
    try:
        bet_amount = int(message.text)
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if bet_amount > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств для ставки.')
            return
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse - bet_amount, message.from_user.id))
        conn.commit()
        roulette_result(message, 'color', bet_amount, color)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')

def roulette_bet_number(call):
    # Запрос ставки на номер
    msg = bot.send_message(call.message.chat.id, text='Введите номер (0-36), на который хотите поставить:')
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
        balanse = cursor.execute('SELECT balanse FROM user WHERE user_id = ?', (message.from_user.id,)).fetchone()[0]
        if bet_amount > balanse:
            bot.send_message(message.chat.id, text='У вас недостаточно средств для ставки.')
            return
        cursor.execute('UPDATE user SET balanse = ? WHERE user_id = ?', (balanse - bet_amount, message.from_user.id))
        conn.commit()
        roulette_result(message, 'number', bet_amount, bet_number)
    except ValueError:
        bot.send_message(message.chat.id, text='Введите корректное число.')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'red':
        roulette_bet_color(call, 'red')
    elif call.data == 'black':
        roulette_bet_color(call, 'black')
    elif call.data == 'green':
        roulette_bet_color(call, 'green')
    elif call.data == 'number':
        roulette_bet_number(call)
    elif call.data == 'casino_game_menu':
        casino_game_menu(call.message)