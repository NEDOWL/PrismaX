from telethon import TelegramClient, events
import random
import sqlite3

# Ваши данные API
api_id = '25795692'
api_hash = 'b2c4c336ed54f9322d13cc105367d4a3'

# Создаем клиент
client = TelegramClient('event_session', api_id, api_hash)

# Подключение к базе данных
con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()

# Команда для начала события
@client.on(events.NewMessage(pattern='/start_event'))
async def start_event(event):
    await event.reply("Добро пожаловать на событие Random Dice! Напишите /menu для выбора действия.")

# Меню события
@client.on(events.NewMessage(pattern='/menu'))
async def menu_event(event):
    menu_text = (
        "Выберите действие:\n"
        "1. /profile - Профиль\n"
        "2. /rating - Рейтинг\n"
        "3. /shop - Магазин\n"
        "4. /roll_dice - Кинуть кубик\n"
    )
    await event.reply(menu_text)

# Бросок кубика
@client.on(events.NewMessage(pattern='/roll_dice'))
async def roll_dice(event):
    dice = ['1', '2', '3', '4', '5', '6']
    result = random.choice(dice)
    result_1 = random.choice(dice)

    if result == result_1:
        await event.reply(f"Вы выбросили {result} и {result_1}. Вы выиграли!")
        cur.execute("UPDATE users SET balance = balance + 100 WHERE id = ?", (event.sender_id,))
        con.commit()
    else:
        await event.reply(f"Вы выбросили {result} и {result_1}. Вы проиграли!")
        cur.execute("UPDATE users SET balance = balance - 100 WHERE id = ?", (event.sender_id,))
        con.commit()

# Профиль пользователя
@client.on(events.NewMessage(pattern='/profile'))
async def profile(event):
    cur.execute("SELECT balance FROM users WHERE id = ?", (event.sender_id,))
    balance = cur.fetchone()
    balance = balance[0] if balance else 0
    await event.reply(f"Ваш баланс: {balance}.")

# Запуск клиента
client.start()
print("Приложение запущено. Ожидание сообщений...")
client.run_until_disconnected()