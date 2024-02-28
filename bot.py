import telebot
from telebot import types

from dct import csvReaderHolidays
from dct import csvReaderLessons

bot = telebot.TeleBot('6484894645:AAGSltj3P-btdHFdFuDwkYOkWDzjoGY5wKo')


# Стартовое меню
@bot.message_handler(commands=['start'])
def start(message):
    mess = (f'Здравствуйте, <b>{message.from_user.first_name}!</b>\nЭтот бот будет показывать информацию о расписании '
            f'школьных уроков, а также каникул.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    scheduleLessons_btn = types.KeyboardButton('Расписание уроков')
    schoolLink_btn = types.KeyboardButton('Сайт школы')
    scheduleHolidays_btn = types.KeyboardButton('Расписание каникул')
    markup.add(scheduleLessons_btn, schoolLink_btn, scheduleHolidays_btn)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


# Сценарий по нажатию кнопок меню из функции start
@bot.message_handler(content_types=['text'])
def firstStep(message):
    if message.text == 'Расписание уроков':  # schedule lessons
        markup = types.InlineKeyboardMarkup(row_width=1)
        scheduleLessons_btn = types.InlineKeyboardButton(csvReaderLessons())
        back_btn = types.InlineKeyboardButton(text='В меню', callback_data='back')
        markup.add(scheduleLessons_btn, back_btn)
        bot.send_message(message.chat.id, csvReaderLessons())

    if message.text == 'Сайт школы':  # school website
        markup = types.InlineKeyboardMarkup(row_width=1)
        schoolLink_btn = types.InlineKeyboardButton(text='Здесь', url='https://lyc1568.mskobr.ru')
        back_btn = types.InlineKeyboardButton(text='В меню', callback_data='back')
        markup.add(schoolLink_btn, back_btn)
        bot.send_message(message.chat.id, 'Ссылка на сайт школы',
                         parse_mode='html', reply_markup=markup)

    if message.text == 'Расписание каникул':  # schedule holidays
        markup = types.InlineKeyboardMarkup(row_width=1)
        scheduleHolidays_btn = types.InlineKeyboardButton(csvReaderHolidays())
        back_btn = types.InlineKeyboardButton(text='В меню', callback_data='back')
        markup.add(scheduleHolidays_btn, back_btn)
        bot.send_message(message.chat.id, csvReaderHolidays())


# Сценарий по нажатию inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def inlineButtonsReaction(call):
    if call.data == 'back':
        markupKeys = types.ReplyKeyboardMarkup(resize_keyboard=True) # 53-56 - initializing types of buttons
        scheduleLessons_btn = types.KeyboardButton('Расписание уроков')
        schoolLink_btn = types.KeyboardButton('Сайт школы')
        scheduleHolidays_btn = types.KeyboardButton('Расписание каникул')
        markupKeys.add(scheduleLessons_btn, schoolLink_btn, scheduleHolidays_btn)
        bot.send_message(call.message.chat.id, 'Вы вернулись в главное меню', reply_markup=markupKeys)


bot.polling(none_stop=True)
