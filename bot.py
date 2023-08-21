import telebot
from telebot import types

bot_token = '6696438979:AAFQ22gFgWMT-eoVda-a_EZBfE_zkOBCMB0'

access_key = 'beta'

bot = telebot.TeleBot(bot_token)

registered_users = []
user_message_counts = {}

@bot.message_handler(commands=['start'])
def start(message):
    
    if message.from_user.id in registered_users:
        bot.send_message(chat_id=message.chat.id, text="Вы зарегистрированы.")
    else:
  
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(types.KeyboardButton(text="Отправить номер телефона", request_contact=True))
        bot.send_message(chat_id=message.chat.id, text="Для регистрации, пожалуйста, поделитесь своим номером телефона.", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def register(message):
 
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    
    
    registered_users.append(user_id)
    

    markup = types.ReplyKeyboardMarkup(row_width=2)
    attack_btn = types.KeyboardButton(text="Method Attack")
    start_btn = types.KeyboardButton(text="Start Attack")
    markup.add(attack_btn, start_btn)
    
    
    bot.send_message(chat_id=message.chat.id, text=f"Регистрация завершена, {user_first_name}!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):

    sender_id = message.from_user.id
    
    
    text = message.text
    
 
    if text == access_key:
    
        bot.send_message(chat_id=sender_id, text="proxy not found error")
    elif text == "Method Attack":
    
        markup = types.ReplyKeyboardMarkup(row_width=2)
        cloudflare_btn = types.KeyboardButton(text="CloudFlare")
        ddosguard_btn = types.KeyboardButton(text="DDoS Guard")
        httpflood_btn = types.KeyboardButton(text="HTTP FLOOD")
        getflood_btn = types.KeyboardButton(text="GET REQUEST FLOOD")
        postflood_btn = types.KeyboardButton(text="POST FLOOD")
        markup.add(cloudflare_btn, ddosguard_btn, httpflood_btn, getflood_btn, postflood_btn)
        
      
        bot.send_message(chat_id=sender_id, text="Выберите метод атаки:", reply_markup=markup)
    elif text == "Start Attack":
        
        bot.send_message(chat_id=sender_id, text="URL | PORT | TIME | METHOD")
    else:
    
        if sender_id in user_message_counts:
            user_message_counts[sender_id] += 1
        else:
            user_message_counts[sender_id] = 1
        
    
        if user_message_counts[sender_id] > 500:
            
            bot.send_message(chat_id=message.chat.id, text="Вы превысили лимит сообщений. Ваш аккаунт заблокирован.")
            bot.kick_chat_member(chat_id=message.chat.id, user_id=sender_id)
        else:
            bot.send_message(chat_id=sender_id, text="Доступ запрещен.")

bot.polling()