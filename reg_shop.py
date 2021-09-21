import telebot
from  telebot import types
import random
from random import randint


# 2031496237:AAH42VfO3NagBjO1V7TPEBjWeujhxTF0k9A

bot = telebot.TeleBot("2031496237:AAH42VfO3NagBjO1V7TPEBjWeujhxTF0k9A", parse_mode=None)



name = ''
surname = ''
number = 0
goods = ''
volume = 0
answer = ''
delivery = ''
discount = ''
bot_num = randint(1,10)



@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы заказать нашу продукцию, ответь на пару вопросов. ')
    bot.send_message(message.chat.id, 'Как вас зовут ? ')
    bot.register_next_step_handler(message, reg_name)




def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у вас фамилия?")
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Ваш номер телефона?\nУкажите в формате '+71111111111'")
    bot.register_next_step_handler(message, reg_number)

def reg_number(message):
    global number
    number = message.text
    if len(number) >= 12:
        bot.send_message(message.from_user.id, "Выберите пункт продукта, который хотите заказать: ")
        bot.send_message(message.from_user.id, "1: ")
        img = open('1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.from_user.id, "2: ")
        img = open('2.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.from_user.id, "3: ")
        img = open('3.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.register_next_step_handler(message, reg_goods)
    else:
        bot.send_message(message.from_user.id, "Укажите в формате '+71234567890")
        bot.register_next_step_handler(message, reg_number)




def reg_goods(message):
    global goods
    if int(message.text) == 1:
        goods = 'Яблоки классические'
    if int(message.text) == 2:
        goods = 'Яблоки с корицей'
    if int(message.text) == 3:
        goods = 'Яблоки с корицей и лимоном'

    bot.send_message(message.from_user.id, "Сколько упаковок вы хотите заказать? ")
    bot.register_next_step_handler(message, reg_volume)





def reg_volume(message):
    global volume
    volume = message.text
    bot.send_message(message.from_user.id, "Самовывоз или Доставка ? ")
    bot.register_next_step_handler(message, reg_delivery)

def reg_delivery(message):
    global delivery
    delivery = message.text
    bot.send_message(message.from_user.id, "Испытайте удачу и выйграйте скидку 30%")
    bot.send_message(message.from_user.id, "Введите число от 1 до 10: ")
    bot.register_next_step_handler(message, reg_discount)

def reg_discount(message):
    global discount
    if int(message.text) > 10 or int(message.text) < 0:
        bot.send_message(message.from_user.id, "Введите число от 1 до 10\nЕсли ваше число будет равно числу бота\nВы выйграйте скидку 30%")
    else:
        if int(message.text) == bot_num:
            bot.send_message(message.from_user.id, "Вы выйграли!")
            discount = '✅'
        else:
            bot.send_message(message.from_user.id, "В этот раз не повезло. На следующий заказ от нас скидка 10%")
            bot.send_message(message.from_user.id, "Ваше число: " + str(message.text))
            bot.send_message(message.from_user.id, "Число бота: " + str(bot_num))
            discount = '❎'







    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)

    question = 'Ваше имя: ' + name + '\nВаша фамилия: ' + surname + '\nВаш телефон: ' + str(number) + '\nВаш заказ: ' + str(goods) + '\nКоличество: ' +str(volume) + '\nТип: ' + str(delivery) + '\nСкидка: '+ discount + ''
    bot.send_message('731425265', question)
    bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Отлично, ожидайте подтверждение!")

        bot.send_message(call.message.chat.id, "Если захотите заказать что-то еще:\nВоспользуйтесь /start")


    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Попробуем еще раз!")
        bot.send_message(call.message.chat.id, "Как вас зовут ?")
        bot.register_next_step_handler(call.message, reg_name)


@bot.message_handler(content_types=["text"])
def some_funtion(message):
    bot.send_message('731425265', question)




bot.polling()

