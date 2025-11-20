import telebot
token="8250156289:AAG4JjRS50gcucsWcLpRW-iumfVKxz4m5to"
bot=telebot.TeleBot(token)
list1=[]
Id = 0
@bot.message_handler(commands=['start','boshla'])
def send(message):
    bot.send_message(message.chat.id,"Ro'yxat kiriting.")
@bot.message_handler(commands=['info'])
def info(message):
    global list1
    for tasks in list1:
        bot.send_message(message.chat.id, f"Id: {tasks['id']}, Vazifa: {tasks['text']}, Bajarilganmi?: {"bajarilgan" if tasks["isDone"]==True else "bajarilmagan" }")
@bot.message_handler(func=lambda message: True)
def tekshir(message):
    global Id
    global list1
    tasks = {
    "id": Id, 
    "text": message.text,
    "isDone": False
    }
    Id += 1
    list1.append(tasks)
print("Dastur boshlandi")
bot.infinity_polling()












# Uyga vazifa foydalanuvchi reminder botga /bajarish comandasini yozganda.
# Foydalanuvchiga barcha vazifalarni chiqarib berish. Foydalanuvchi qaysi vazifani bajarish kerak bo'lsa o'shani id sini kiritadi.
# Kiritigan id dagi vazifani bajarilgan qilib belgilash kerak yani True.



















import telebot
from telebot import types
bot = telebot.TeleBot('8298227192:AAH0v1hhPNe5lEgyD3u12J2sD9XhUJaOl1w')

id=1
tasks={}
import random
list1=[]

@bot.message_handler(commands=['info'])
def send(message):
    bot.send_message(message.chat.id,f"Id: {tasks["id"]},vazifa: {tasks["text"]},bajarilganmi?: {"bajarilgan" if tasks["isdone"]==True else "bajarilmagan"}")
@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id,"Ro'yxat kiriting va kegin info yozing.")
@bot.message_handler(func=lambda message: True)
def tekshir(message):
    global tasks
    global id
    tasks={
        "id":id,
        "text":message.text,
        "isdone":False
    }
    id+=1
    list1.append(tasks)

@bot.message_handler(commands=['bajarildi'])
def bajarildi(message):
    global tasks
    global list1
    for task in list1:
        if task["id"] == int(message.text.split(" ")[1]):
            task["isdone"] = True
            bot.send_message(message.chat.id,"Vazifa bajarildi.")
            return
    bot.send_message(message.chat.id,"Bunday vazifa topilmadi.")

print("Bot ishga tushdi")
bot.infinity_polling()





























# import telebot

# TOKEN = "8250156289:AAG4JjRS50gcucsWcLpRW-iumfVKxz4m5to"
# bot = telebot.TeleBot(TOKEN)

# user_data = {}

# @bot.message_handler(commands=['start', 'form'])
# def start_form(message):
#     bot.send_message(message.chat.id, f"Assalomu alaykum @{message.from_user.username} Keling formani to'ldiramiz \n\nIsmingizni kiriting:")
#     bot.register_next_step_handler(message, get_name)

# def get_name(message):
#     user_id = message.from_user.id
#     user_data[user_id] = {'name': message.text}
#     bot.send_message(message.chat.id, "Familiyangizni kiriting:")
#     bot.register_next_step_handler(message, get_surname)

# def get_surname(message):
#     user_id = message.from_user.id
#     user_data[user_id]['surname'] = message.text
#     bot.send_message(message.chat.id, "Yoshingizni kiriting:")
#     bot.register_next_step_handler(message, get_age)

# def get_age(message):
#     user_id = message.from_user.id
#     if not message.text.isdigit():
#         bot.send_message(message.chat.id, "Iltimos, yoshni raqam bilan kiriting.")
#         bot.register_next_step_handler(message, get_age)
#         return

#     user_data[user_id]['age'] = int(message.text)
    
#     name = user_data[user_id]['name']
#     surname = user_data[user_id]['surname']
#     age = user_data[user_id]['age']
#     bot.send_message(message.chat.id, f"Forma to'ldirildi!\n\n Ism: {name}\n Familiya: {surname}\n Yosh: {age}")

# print("Bot ishga tushdi")
# bot.infinity_polling()




# for i in range(1,4):
#     print("*"*(2*i-1))


