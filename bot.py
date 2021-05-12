import telebot
import config
import api_handler
#import pb
import datetime
import pytz
import json
import traceback
import time
import urllib.request
import requests
import urllib.parse

bot = telebot.TeleBot(config.TOKEN)

def extract_unique_code(text):
    # Extracts the unique_code from the sent /start command.
    return text.split()[1] if len(text.split()) > 1 else None
def get_id(message):
    return message.chat.id
def get_name(message):
    fname=message.from_user.first_name
    lname=message.from_user.last_name
    name = str(fname) + " "+ str(lname)
    return str(name)
def get_header(message):
    headers = {
        'API-Key': config.API_Key,
        'telegram_user_id': f"{get_id(message)}",
        'Content-Type': 'application/json'
            }
    return headers

def get_header_call(call):
    headers = {
        'API-Key': config.API_Key,
        'telegram_user_id': f"{call.from_user.id}",
        'Content-Type': 'application/json'
            }
    return headers

@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = menu_buttons()
    unique_code = extract_unique_code(message.text)
    id = get_id(message)
    name = get_name(message)
    end_point = 'v1/users'
    url1 = urllib.parse.urljoin(config.URL_Server, end_point)
    payload= json.dumps({
            "name": f"{ name }",
            "referred_by": f"{ unique_code }"
            })
    header = {
        'API-Key': config.API_Key,
        'telegram_user_id': f"{id}",
        'Content-Type': 'application/json'
            }
    response = requests.request("POST", url1, headers=header, data=payload)
    resp = response.text
    var1 = (f'\033[1m CHI TRON Miner \033[0m')
    bot.send_message(
       message.chat.id,
       f'CHI TRON Miner \n Is fully automatic. Start earning TRX now for free.',reply_markup=keyboard,parse_mode='HTML'
   )

def menu_buttons():
    '<br>'
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('👤 Account', callback_data='account'),
        telebot.types.InlineKeyboardButton('👤 Referrals', callback_data='referals'),
        telebot.types.InlineKeyboardButton('✅ Check-in', callback_data='check-in')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('💲 Upgrade', callback_data='upgrade'),
        telebot.types.InlineKeyboardButton('💵 Withdraw', callback_data='withdraw')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('🏆 Ranking', callback_data='ranking'),
        telebot.types.InlineKeyboardButton('💲 Payment', callback_data='payment'),
        telebot.types.InlineKeyboardButton('📉 Stats', callback_data='stats')
    )
    return keyboard

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    keyboard = menu_buttons()
    bot.answer_callback_query(callback_query_id=call.id)
    id = call.from_user.id
    fname=call.from_user.first_name
    lname=call.from_user.last_name
    name = str(fname)+ " "+ str(lname)
    header = get_header_call(call)
    answer = ' '
    if call.data == 'account':
        answer = api_handler.handle_account_request(id,name,header)
    elif call.data == 'referals':
        answer = api_handler.handle_referals_request(id,name,header)
    elif call.data == 'upgrade':
        answer = api_handler.handle_upgrade_request(id,name,header)
    elif call.data == 'withdraw':
        answer = api_handler.handle_withdraw_request(id,name,header)
    elif call.data == 'ranking':
        answer = api_handler.handle_ranking_request(id,name,header)
    elif call.data == 'payment':
        answer = api_handler.handle_payment_request(id,name,header)
    elif call.data == 'stats':
        answer = api_handler.handle_stats_request(id,name,header)
    elif call.data == 'check-in':
        answer = api_handler.handle_checkin_request(id,name,header)
    else:
        answer = 'How can i help you! '
    bot.send_message(call.message.chat.id, answer,reply_markup=keyboard,parse_mode='HTML')

@bot.message_handler(commands=['Update_Email'])
def Update_Email(message):
    # bot.answer_callback_query(callback_query_id=message.id)
    id = get_id(message)
    name = get_name(message)
    sent = bot.send_message(message.chat.id, 'Enter Your Email_Id:'  )
    bot.register_next_step_handler(sent, email)

def email(message):
    try:
        chat_id = get_id(message)
        name = get_name(message)
        email = message.text
        end_point = 'v1/users'
        url1 = urllib.parse.urljoin(config.URL_Server, end_point)
        payload = json.dumps({
        "name": "string",
        "telegram_user_id": f"{ chat_id }",
        "email_id": f"{email}"
        })
        header = get_header(message)

        response = requests.request("PUT", url1, headers=header, data=payload)
        bot.send_message(chat_id, "Email : " + email )
        text = "User:"+name+" Update his/her email"
        URL = config.URL_For_Response+text
        url = URL.replace(" ","%20")
        urllib.request.urlopen(url)
    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(commands=['Update_Wallet'])
def Update_Wallet(message):
    id = get_id(message)
    name = get_name(message)

    answer = ' '
    sent = bot.send_message(message.chat.id, 'Enter Your Wallet:')
    bot.register_next_step_handler(sent, wallet)

def wallet(message):
    try:
        chat_id = get_id(message)
        wallet = message.text
        name = get_name(message)
        end_point = 'v1/users'
        url1 = urllib.parse.urljoin(config.URL_Server, end_point)

        payload = json.dumps({
        "name": "string",
        "telegram_user_id": f"{ chat_id }",
        "wallet": f"{ wallet }"
        })
        header = get_header(message)

        response = requests.request("PUT", url1, headers=header, data=payload)
        resp = response.text
        bot.send_message(chat_id, "Wallet : " + wallet )
        text = "User:"+name+" Update his/her Wallet "
        URL = config.URL_For_Response+text
        url = URL.replace(" ","%20")
        urllib.request.urlopen(url)
    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(commands=['Withdraw'])
def withdraw_request(message):
    # bot.answer_callback_query(callback_query_id=message.id)
    id = get_id(message)
    name = get_name(message)
    sent = bot.send_message(message.chat.id, 'Enter Amount You want to withdraw:'  )
    bot.register_next_step_handler(sent, withdraw)

def withdraw(message):
    try:
        chat_id = get_id(message)
        name = get_name(message)
        email = message.text
        print(email)
        end_point = 'v1/withdraw'
        url1 = urllib.parse.urljoin(config.URL_Server, end_point)
        #print((url1))
        payload = json.dumps({
        "withdraw_amount": int(email)
        })
        header = get_header(message)
        #print(payload)
        #print(header)

        response = requests.request("POST", url1, headers=header, data=payload)
        #print(response)
        bot.send_message(chat_id, "Request raised for payment of : " + email + " Coins")
        text = "User:"+name+" Raised a paymnet request of " + email + " Coins"
        URL = config.URL_For_Response+text
        url = URL.replace(" ","%20")
        urllib.request.urlopen(url)
    except Exception as e:
        bot.reply_to(message, e)

    
bot.polling(none_stop=True)