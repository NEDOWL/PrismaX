import sqlite3
import os
if os.path.exists('db.db'):
    os.remove('db.db')
    print('db.db removed')

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE crypto
               (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER NOT NULL, btc INTEGER, eth INTEGER, ltc INTEGER, xrp INTEGER, doge INTEGER, hmstr INTEGER)''')
print('Table 1 created')
cursor.execute('''CREATE TABLE user
               (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER NOT NULL, user_name TEXT NOT NULL, balanse INTEGER, admin INTEGER, time_income INTEGER, mining STRING NOT NULL, start_pack INTEGER, ref_cod INTEGER, ref_count INTEGER)''')
print('Table 2 created')
cursor.execute('''CREATE TABLE time
               (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER, times INTEGER)''')
print('Table 3 created')
cursor.execute('''CREATE TABLE crypto_price
 (id INTEGER PRIMARY KEY NOT NULL UNIQUE, btc INTEGER, eth INTEGER, ltc INTEGER, xrp INTEGER, doge INTEGER, hmstr INTEGER)''')
print('Table 4 created')
#cursor.execute('INSERT INTO crypto_price (btc, eth, ltc, xrp, doge, hmstr) VALUES (?, ?, ?, ?, ?, ?)', (0, 0, 0, 0, 0, 0))
#cursor.execute('''CREATE TABLE card
 #              (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER NOT NULL, card_number INTEGER)''')
print('Table 5 created')
cursor.execute('''CREATE TABLE card
 (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER NOT NULL, rtx_5090 INTEGER, rtx_4090 INTEGER, rtx_3090_ti INTEGER, rtx_3090 INTEGER, rtx_3080_ti INTEGER, rtx_3080 INTEGER, ice_river_aeo INTEGER, goldshell_ae_box INTEGER, goldshell_ae_box_pro INTEGER, goldshell_ae_box_ii INTEGER, gtx_1080_ti INTEGER)''')
cursor.execute('''CREATE TABLE wallet
 (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER NOT NULL, btc INTEGER, eth INTEGER, ltc INTEGER, xrp INTEGER, doge INTEGER, hmstr INTEGER)''')
print('Table 6 created')
cursor.execute('''CREATE TABLE card_common
               (id INTEGER PRIMARY KEY NOT NULL UNIQUE, user_id INTEGER, gtx_1080_ti INTEGER, gtx_1080 INTEGER, gtx_2060 INTEGER, gtx_2070 INTEGER, gtx_2080 INTEGER, gtx_2080_ti INTEGER, rtx_3060 INTEGER, rtx_3060_ti INTEGER, rtx_3070 INTEGER, rtx_3070_ti INTEGER)''')
print('Table 7 created')
conn.commit()
conn.close()