import re
import requests
import config
import json
import webbrowser
import urllib.request
import requests
import urllib.parse


def handle_account_request(id,name,header):
  u_name = name
  end_point = 'v1/users'
  url1 = urllib.parse.urljoin(config.URL_Server, end_point)
  response = requests.request("GET", url1, headers=header)
  resp = response.text
  resp_dict = json.loads(resp)
  account = resp_dict["user"]
  plan = resp_dict["user"]["subscribed_plans"]
  result1 = f"GENERAL INFORMATION \n\
    \n\
    User:  { u_name }\n \
    Balance: {account['total_balance']} TRX  \n \
                    "
  for i in plan: 
    result = f" \n\
      Plan: {i['plan_name']} \n \
    ⚡️ Speed: {i['speed']} \n \
             {i['max_coin_per_day']} TRX/day \n \
             {i['max_coin_per_month']} TRX/month \n \
      "
    result1 = result1 + result
  result2 = result1 + f"  \n\
    TRX wallet:    {account['wallet']}\n \
    /Update_Wallet\n \
                    \n \
    Email:    {account['email_id']} \n \
    /Update_Email  \n\
    "
  text = 'User:'+u_name+' views his/her account details' 
  #URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  URL = config.URL_For_Response+text
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result2

def handle_referals_request(id,name,header):
  u_name = name
  referal_code =id
  end_point = 'v1/referrals'
  url1 = urllib.parse.urljoin(config.URL_Server, end_point)

  response = requests.request("GET", url1, headers=header)
  resp = response.text
  resp_dict = json.loads(resp)

  refer = resp_dict["result"]
  #result = '<b>' + 'Referrals code' + ' -> ' + referal_code + ':</b>\n\n'
  results = f"👥 REFERRAL SYSTEM \n \
    ▫️ Earnings: { refer['earnings' ]} TRX\n \
    ▫️ Referrals: { refer['no_of_referrals']} \n \
    ▫️ Active Referrals: { refer['no_of_active_referrals'] } \n \
    ▫️ Bonus: 3 TRX Coin for every referrals. \n \
    ▫️ Link: https://t.me/alam12bot?start="+str(referal_code)+"\n "
  text = 'User:'+u_name+' with referal code:'+str(referal_code)+' views his/her referal statement' 
  #URL = 'https://api.telegram.org/bot'+(config.TOKEN)+'/sendMessage?chat_id='+(config.CHAT)+'&text='+text+''
  URL = config.URL_For_Response+text
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return results

def handle_withdraw_request(id,name,header):
  u_name = name
  end_point = 'v1/withdraw/checklist'
  url1 = urllib.parse.urljoin(config.URL_Server, end_point)
  response = requests.request("GET", url1, headers=header)
  resp = response.text
  resp_dict = json.loads(resp)

  refer = resp_dict["withdraw_check_list"]
  min_bal = refer["is_eligible_for_min_withdraw"]
  value = [refer["is_eligible_for_min_withdraw"],refer["is_wallet_updated"],refer["is_email_updated"],refer["total_number_of_refer"]]
  value1 = ['✔️' if i==True else '✖️' if i==False else i for i in value]
  # print(value1)
  # for val in value:
  #   if val is True:
  #     val = "✔️"
  #     tick.append(val)
  #     #print(val)
  #   else:
  #     val = "✖️"
  #     tick.append(val)
      #print(val)
    #print(val)
  #print(tick)
  # if min_bal is True:
  #   min_bal = "✔️"
  #   print("Minimum Balance", min_bal)
  # else:
  #   print("else executed")
  result = f"💵 WITHDRAW \n \
                     \n \
    {value1[0]} Minimum withdrawal: 100 TRX \n \
    {value1[1]} Update wallet for your account.\n \
    {value1[2]} Update email for your account.\n \
    {value1[3]} Refer 10 friends. \n \
      \n\
      "
  if value[0] is True and value[1] is True and value[2] is True and value[3] is True:
    result1 = result+f"\n \
    all checklist completed!\n \
    /Withdraw\n \
    For any Queries visit : {config.LINK_FOR_QUERIES}  \n\ "
  else:
    result1 = result+"\n \
    ⚠️ You must have all checklist completed!"
  text = 'User:'+u_name+' views his/her withdraw criteria' 
  URL = config.URL_For_Response+text
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result1
  
def handle_upgrade_request(id,name,header):
  u_name = name
  end_point = 'v1/plans'
  url1 = urllib.parse.urljoin(config.URL_Server, end_point)
  response = requests.request("GET", url1, headers=header)
  resp = response.text
  resp_dict = json.loads(resp)
  result1 = f"UPGRADE ACCOUNT \n \
                      "
  plan_list = resp_dict["plan_list"]
  for i in plan_list: 
    result = f" \n\
          🔹 Plan:{i['plan_name']} \n \
          💲 Price:{ i['price'] } TRX \n \
          ⚡️ Speed: 1500 MH/s \n \
                  { i['max_coin_per_day'] } TRX/day \n \
                  { i['max_coin_per_month'] } TRX/month \n \
          💵 Withdrawal: { i['withdrawal'] }  \n \
          ⌚️ Contract length: { i['contract_length'] }  \n \
                        "
    result1 = result1 + result
  result2 = result1 +f"\n\
  ◽️ Please send Tron to the address bellow to Upgrade your account:\n \
    \n /TFkMc9zFoQZVQuJB7YdbeTCoFm2FMC4rDW \n \
  ⚠️ Only send Tron (TRX) to this address! \n \
    Send your Screenshot of payment here : {config.LINK_FOR_QUERIES}  \n \
    "
  text = 'User:'+u_name+' views Upgrade Plans' 
  URL = config.URL_For_Response+text
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result2

def handle_ranking_request(id, name,header):
  u_name = name
  end_point = 'v1/ranking'
  url1 = urllib.parse.urljoin(config.URL_Server, end_point)
  response = requests.request("GET", url1, headers=header)
  resp = response.text
  resp_dict = json.loads(resp)
  result1 = f"🏆 RANKING\n \
    "
  plan_list = resp_dict["ranking"]
  for i in plan_list: 
    #if int(i['id']) < 6:
      result = f" \n\
        {i['id']}  {i['name']}  {i['coin']} \n \
        "
      result1 = result1 + result
    #else:
  # result = f"🏆 RANKING\n \
  #   \n \
  #   \n \
  # 🥇 Ibrahima PAFADNAM +746 \n \
  # 🥈 Junior Nghonyama +633 \n \
  # 🥉 Charles +618 \n \
  # ▫️ Jah +586 \n \
  # ▫️ Njagi Susan +556 \n \
  # 🔹 Son Tran +465 \n \
  # ▫️ Yeong Teong Ngo +455 \n \
  # 🔹 SBW +440 \n \
  # ▫️ GURAM KHUTASHVI +413 \n \
  # 🔹 Vania Silva +412  \n \
  #   "
  #result = '<b>' + 'Ranking' + ' -> '  ':</b>\n\n'
  text = 'User:'+u_name+' views overall Top 10 Ranking' 
  URL = config.URL_For_Response+text
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result1

def handle_payment_request(id, name,header):
  u_name = name
  end_point = 'v1/payment'
  url1 = urllib.parse.urljoin(config.URL_Server, end_point)
 
  response = requests.request("GET", url1, headers=header)
  resp = response.text
  resp_dict = json.loads(resp)
  result1 = f"💲 PAYMENT HISTORY\n \
    "
  plan_list = resp_dict["payment"]
  for i in plan_list: 
    result = f" \n\
      ✅  {i['coin']},  {i['time']} \n \
     🔹   {i['name']}   \n \
      "
    result1 = result1 + result
  result2 = result1 +"\n\
  ▫️ Only 10 latest payments are displayed!"
#   result = f"💲 PAYMENT HISTORY\n \
#     \n \
# ✅ 0.32150000 ETH, 04-14 09:27 \n \
# 🔹 Shu Gy \n \
#   \n \
# ✅ 0.74375800 ETH, 04-14 09:24 \n \
# 🔹 Elsa \n \
#   \n \
# ✅ 0.33351000 ETH, 04-14 09:24 \n \
# 🔹 ᎠᎬᏡᎢᎬᏒᏫᏌᏚ \n \
#   \n \
# ✅ 0.35530200 ETH, 04-14 09:22 \n \
# 🔹 Kaptchouang Sandra \n \
#   \n \
# ✅ 0.26291000 ETH, 04-14 09:19 \n \
# 🔹 Ezrah Ngetich \n \
#   \n \
# ✅ 0.26540600 ETH, 04-14 09:19 \n \
# 🔹 SlimKing \n \
#   \n \
# ✅ 0.25552200 ETH, 04-14 09:19 \n \
# 🔹 T·D \n \
#   \n \
# ✅ 0.38535300 ETH, 04-14 09:17 \n \
# 🔹 Roger G \n \
#   \n \
# ✅ 0.26401900 ETH, 04-14 09:17 \n \
# 🔹 *·* \n \
#   \n \
# ✅ 0.25257600 ETH, 04-14 09:16 \n \
# 🔹 Patrylo Patrylo \n \
#   \n \
# ▫️ Only 10 latest payments are displayed! \n \
#   "
  #result = '<b>' + 'Payment' + ' -> ' +  ':</b>\n\n'
  text = 'User:'+u_name+' views Payment requests' 
  URL = config.URL_For_Response+text
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result2

def handle_stats_request(id,name,header):
  u_name = name
  end_point = 'v1/stats'
  url1 = urllib.parse.urljoin(config.URL_Server, end_point)

  response = requests.request("GET", url1, headers=header)
  resp = response.text
  resp_dict = json.loads(resp)
  stats = resp_dict["stats"]
  result = f"\n\
            📈 BOT STATS \n \
        ◽️ Monthly withdraw:{stats['monthly_withdraw']} \n \
        ◽️ Monthly members:{stats ['monthly_members'] } \n \
        ◽️ Active members:{stats ['active_members'] } \n \
        ◽️ Referer:{stats['referer']} \n \
        ◽️ Online:{stats['online'] } \n \
            \n \
                        "

  text = "User:"+u_name+" views Company's stats"
  URL = config.URL_For_Response+text
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result

def handle_checkin_request(id,name,header):
  u_name = name
  end_point = 'v1/check-in'
  url1 = urllib.parse.urljoin(config.URL_Server, end_point)
  
  response = requests.request("GET", url1, headers=header)

  result = f"📈 Daily Check-in \n \
    "
  text = "User:"+u_name+" just checked-in"
  URL = config.URL_For_Response+text
  url = URL.replace(" ","%20")
  urllib.request.urlopen(url)
  return result






