import telebot
from telebot import types
import random
import time
import sqlite3
from main import bot

con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()

def event_start(message):
    bot.send_message(message.chat.id, "🛑В разработке🛑")

def event(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start = types.KeyboardButton("Начать")
    markup.add(start)
    bot.send_message(message.chat.id, "Добро пожаловать на событие Random Dice", reply_markup=markup)

def menu_event(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    profile = types.KeyboardButton("Профиль")
    rating = types.KeyboardButton("Рейтинг")
    shop = types.KeyboardButton("Магазин")
    dice = types.KeyboardButton("Кинуть кубик")
    markup.add(dice, profile, rating, shop)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)

def event_dice(message):
    dice = ['1', '2', '3', '4', '5', '6']
    result = random.choice(dice)
    result_1 = random.choice(dice)
    if result == result_1:
        bot.send_message(message.chat.id, f"Вы выбросили {result} и {result_1}. Вы выиграли!")
        cur.execute("UPDATE users SET balance = balance + 100 WHERE id = ?", (message.chat.id,))
        con.commit()
    else:
        bot.send_message(message.chat.id, f"Вы выбросили {result} и {result_1}. Вы проиграли!")
        cur.execute("UPDATE users SET balance = balance - 100 WHERE id = ?", (message.chat.id,))
        con.commit()