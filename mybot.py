import telebot
from telebot import types

bot = telebot.TeleBot('6689714819:AAGQjkAkUI3OlVOC9pOyWMDRqvy-W4MEBzI')

user_choices = {}

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_buttons = ["Haven", "Ascent", "Split", "Bind", "Breeze", "Sunset", "Fracture", "Pearl", "Icebox"]
for button_label in start_buttons:
    start_keyboard.add(types.KeyboardButton(button_label))


choice_keyboard = types.ReplyKeyboardMarkup(row_width=1)
choice_buttons = ["Gekko", "Killjoy", "Sova", "Viper", "Brimstone", "Deadlock", "Cypher", "Fade", "Harbor", "Kay/0", "Yoru", "Neon"]
for button_label in choice_buttons:
    choice_keyboard.add(types.KeyboardButton(button_label))

attack_defense_keyboard = types.ReplyKeyboardMarkup(row_width=1)
attack_button = types.KeyboardButton("Attack")
defense_button = types.KeyboardButton("Defend")
attack_defense_keyboard.add(attack_button, defense_button)

point_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
point_buttons = ["А", "B", "C"]
for button_label in point_buttons:
    point_keyboard.add(types.KeyboardButton(button_label))

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Виберіть опцію:", reply_markup=start_keyboard)

@bot.message_handler(func=lambda message: message.text in start_buttons)
def handle_start_choice(message):
    user_id = message.from_user.id
    user_choices[user_id] = {"start_choice": message.text}
    bot.send_message(user_id, "Виберіть один з варіантів:", reply_markup=choice_keyboard)

@bot.message_handler(func=lambda message: message.text in choice_buttons)
def handle_choice(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_choices[user_id]["choice"] = user_choice
    bot.send_message(user_id, f"Ви обрали: {user_choice}. Виберіть атаку або оборону:", reply_markup=attack_defense_keyboard)

@bot.message_handler(func=lambda message: message.text in ["Attack", "Defend"])
def handle_attack_defense(message):
    user_id = message.from_user.id
    user_choices[user_id]["attack_defense"] = message.text
    bot.send_message(user_id, "Виберіть точку (А, B, C):", reply_markup=point_keyboard)

@bot.message_handler(func=lambda message: message.text in point_buttons)
def handle_point_choice(message):
    user_id = message.from_user.id
    user_choice = user_choices.get(user_id)
    user_choices[user_id]["point"] = message.text
    if user_choice:
        bot.send_message(user_id, f"Wait...")
        send_video_based_on_choice(user_id, user_choice)
    else:
        bot.send_message(user_id, "Спробуйте ще раз.")
    user_choices.pop(user_id, None)

def send_video_based_on_choice(user_id, user_choice):
    start_choice = user_choice["start_choice"]
    choice = user_choice["choice"]
    attack_defense = user_choice["attack_defense"]
    point = user_choice["point"]

    if start_choice == "Haven":
        if choice == "Gekko":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Sova":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Viper":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Killjoy":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Brimstone":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Deadlock":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Cypher":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Fade":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Harbor":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Kay/0":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Yoru":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                    
    if start_choice == "Haven":
        if choice == "Neon":
            if attack_defense == "Attack":
                if point == "А":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
            elif attack_defense == "Defend":
                if point == "А":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))
                elif point == "B":
                    bot.send_video(user_id, open("cs2.mp4", "rb"))
                elif point == "C":
                    bot.send_video(user_id, open("razwe.mp4", "rb"))

bot.polling()
