import telebot
from telebot import types

# Укажите токен вашего бота
bot_token = '6696438979:AAFQ22gFgWMT-eoVda-a_EZBfE_zkOBCMB0'

# Установите ключ для доступа к боту
access_key = '04116930088'

# Создание экземпляра бота
bot = telebot.TeleBot(bot_token)

registered_users = []  # Список зарегистрированных пользователей
user_message_counts = {}  # Словарь для хранения количества сообщений пользователей

@bot.message_handler(commands=['start'])
def start(message):
    # Проверка, является ли пользователь уже зарегистрированным
    if message.from_user.id in registered_users:
        bot.send_message(chat_id=message.chat.id, text="Вы уже зарегистрированы.")
    else:
        # Запрос к пользователю для регистрации по номеру
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(types.KeyboardButton(text="Отправить номер телефона", request_contact=True))
        bot.send_message(chat_id=message.chat.id, text="Для регистрации, пожалуйста, поделитесь своим номером телефона.", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def register(message):
    # Получение информации о контакте пользователя
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    
    # Регистрация пользователя по номеру телефона
    registered_users.append(user_id)
    
    # Создание кнопок
    markup = types.ReplyKeyboardMarkup(row_width=2)
    attack_btn = types.KeyboardButton(text="Method Attack")
    start_btn = types.KeyboardButton(text="Start Attack")
    markup.add(attack_btn, start_btn)
    
    # Отправка сообщения о успешной регистрации с кнопками "Method Attack" и "Start Attack"
    bot.send_message(chat_id=message.chat.id, text=f"Регистрация успешно завершена, {user_first_name}!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Получение идентификатора отправителя
    sender_id = message.from_user.id
    
    # Получение текста сообщения
    text = message.text
    
    # Проверка наличия ключа доступа
    if text == access_key:
        # Отправка обратной связи
        bot.send_message(chat_id=sender_id, text="proxy not found error")
    elif text == "Method Attack":
        # Создание кнопок для выбора метода атаки
        markup = types.ReplyKeyboardMarkup(row_width=2)
        cloudflare_btn = types.KeyboardButton(text="CloudFlare")
        ddosguard_btn = types.KeyboardButton(text="DDoS Guard")
        httpflood_btn = types.KeyboardButton(text="HTTP FLOOD")
        getflood_btn = types.KeyboardButton(text="GET REQUEST FLOOD")
        postflood_btn = types.KeyboardButton(text="POST FLOOD")
        markup.add(cloudflare_btn, ddosguard_btn, httpflood_btn, getflood_btn, postflood_btn)
        
        # Отправка сообщения с кнопками выбора метода атаки
        bot.send_message(chat_id=sender_id, text="Выберите метод атаки:", reply_markup=markup)
    elif text == "Start Attack":
        # Обработка нажатия кнопки "Start Attack"
        bot.send_message(chat_id=sender_id, text="[URL]-[PORT]-[TIME]-[METHOD]")
    else:
        # Проверка количества сообщений пользователя
        if sender_id in user_message_counts:
            user_message_counts[sender_id] += 1
        else:
            user_message_counts[sender_id] = 1
        
        # Проверка, превышает ли количество сообщений ограничение
        if user_message_counts[sender_id] > 50:
            # Блокировка пользователя и отправка уведомления
            bot.send_message(chat_id=message.chat.id, text="Вы превысили лимит сообщений. Ваш аккаунт заблокирован.")
            bot.kick_chat_member(chat_id=message.chat.id, user_id=sender_id)
        else:
            # Отправка предупреждения о неверном ключе доступа
            bot.send_message(chat_id=sender_id, text="Доступ запрещен. Неверный ключ.")
            
# Запуск прослушивания входящих сообщений
bot.polling()