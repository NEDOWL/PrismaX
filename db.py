import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE crypto
               (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER NOT NULL, btc INTEGER, eth INTEGER, ltc INTEGER, xrp INTEGER, doge INTEGER, hmstr INTEGER)''')
print('Table 1 created')
cursor.execute('''CREATE TABLE user
               (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER NOT NULL, user_name TEXT NOT NULL, balanse INTEGER, admin INTEGER)''')
print('Table 2 created')
cursor.execute('''CREATE TABLE time
               (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER, times INTEGER)''')
print('Table 3 created')
cursor.execute('''CREATE TABLE crypto_price
 (id INTEGER PRIMARY KEY NOT NULL UNIQUE, btc INTEGER, eth INTEGER, ltc INTEGER, xrp INTEGER, doge INTEGER, hmstr INTEGER)''')
print('Table 4 created')
cursor.execute('INSERT INTO crypto_price (btc, eth, ltc, xrp, doge, hmstr) VALUES (?, ?, ?, ?, ?, ?)', (0, 0, 0, 0, 0, 0))
cursor.execute('''CREATE TABLE card
               (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER NOT NULL, card_number INTEGER, )''')
print('Table 5 created')
conn.commit()
conn.close()