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
# from os import environ
# from flask import Flask

# app = Flask(__name__)
# P_TIMEZONE = pytz.timezone(config.TIMEZONE)
# TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = menu_buttons()
    bot.send_message(
       message.chat.id,
       '\n\nETH Miner \n is fully automatic. Start earning ETH now for free.',reply_markup=keyboard,parse_mode='HTML'
   )

def menu_buttons():
    '<br>'
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('👤 Account', callback_data='account'),
        telebot.types.InlineKeyboardButton('👤 Referrals', callback_data='referals'),
        telebot.types.InlineKeyboardButton('👤 Check-in', callback_data='check-in')
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
    #print(call)
    fname=call.from_user.first_name
    lname=call.from_user.last_name
    name = fname + " "+ lname

    answer = ' '
    if call.data == 'account':
        answer = api_handler.handle_account_request(id,name)
    elif call.data == 'referals':
        answer = api_handler.handle_referals_request(id,name)
    elif call.data == 'upgrade':
        answer = api_handler.handle_upgrade_request(id,name)
    elif call.data == 'withdraw':
        answer = api_handler.handle_withdraw_request(id,name)
    elif call.data == 'ranking':
        answer = api_handler.handle_ranking_request(id,name)
    elif call.data == 'payment':
        answer = api_handler.handle_payment_request(id,name)
    elif call.data == 'stats':
        answer = api_handler.handle_stats_request(id,name)
    elif call.data == 'check-in':
        answer = api_handler.handle_checkin_request(id,name)
    else:
        answer = 'How can i help you! '
    bot.send_message(call.message.chat.id, answer,reply_markup=keyboard,parse_mode='HTML')
    # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

# def main():
#     return


# if __name__ == '__main__':
#     bot.py(host='0.0.0.0')
#app.run(environ.get('PORT'))
bot.polling(none_stop=True)