# -*- coding: utf-8 -*-
import re
import requests
#from prompt_toolkit import HTML
import json
# URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

def handle_account_request(id,name):
  u_name = name
  # u_name1 = ("\033[1m" +{name}+ "\033[0m")
  # print(u_name1)
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
  return account_detail

def handle_referals_request(id):
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
  return result

def handle_withdraw_request(id):
  """💵 WITHDRAW

✖️ Minimum withdrawal: 0.25000000 ETH
✖️ Update wallet for your account.
✖️ Update email for your account.
✖️ Refer 10 friends.

⚠️ You must have all checklist completed! """
  #result = '<b>' + 'Withdraw' + ' -> '  ':</b>\n\n'
  result = f"💵 WITHDRAW \n \
                     \n \
    ✖️ Minimum withdrawal: 0.25000000 ETH \n \
    ✖️ Update wallet for your account.\n \
    ✖️ Update email for your account.\n \
    ✖️ Refer 10 friends. "
  return result

def handle_upgrade_request(id):
  #result = '<b>' + 'Upgrade' + ' -> ' ':</b>\n\n'
  result = f"UPGRADE ACCOUNT \n \
                     \n \
        🔹 Plan: CRAB\n \
        💲 Price: 0.125 ETH \n \
        ⚡️ Speed: 1500 MH/s \n \
                0.36000000 ETH/day \n \
                10.80000000 ETH/month \n \
        💵 Withdrawal: 6 hours \n \
        ⌚️ Contract length: 1 year \n \
                      \n \
                      \n \
        🔹 Plan: SHARK \n \
        💲 Price: 1.25 ETH \n \
        ⚡️ Speed: 15 GH/s \n \
                0.72000000 ETH/day\n \
                21.60000000 ETH/month\n \
        💵 Withdrawal: instant \n \
        ⌚️ Contract length: 1 year \n \
                      \n \
                      \n \
  ◽️ Please send Ethereum to the address bellow to Upgrade your account:\n \
    \n \
  0x719071dAF5dAEDAF69C849c141880********* \n \
      \n \
  https://etherscan.io/address/0x719071dAF5dAEDAF69C849c141880Dbc64A439b3\n \
      \n \
  ⚠️ Only send Ethereum (ETH) to this address! \n \
                       "
  return result

def handle_ranking_request(id):
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
  return result

def handle_payment_request(id):
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
  return result

def handle_stats_request(id):
  result = f"📈 BOT STATS \n \
    \n \
◽️ Monthly withdraw: 11647.3522 ETH \n \
◽️ Monthly members: 274,104 \n \
◽️ Active members: 136,417 \n \
◽️ Referer: 91,740 \n \
◽️ Online: 2,833 \n \
  "
  #result = '<b>' + 'Stats' + ' -> ' +  ':</b>\n\n'
  return result





