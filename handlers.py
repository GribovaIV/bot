from telegram import ReplyKeyboardMarkup, InputMediaPhoto, ReplyKeyboardRemove
from utilites import *
from glob import glob
from texts import *
from selenium import webdriver

# открывает браузер в режиме тест ПО

driver = webdriver.Chrome()

# функция помощи 1

def help_1(bot,update):	
	
	bot.message.reply_text(	
		text=help_11,
		)

# функция помощи 2

def help_2(bot,update):
	
	update.bot.send_message(
		chat_id='@MoscowITproject',
		text = channel_1
		)

# функция для команды 1

def one(bot,update):
	
    driver.get('https://www.youtube.com/channel/UCZUw_DqGER3mWhArink_0ug' + "/videos")
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
    	url = videos[i].get_attribute('href')
    	tmp = str(url)
    	update.bot.send_message(
    		chat_id='@MoscowITproject',
    		text = tmp,
    		disable_web_page_preview = False
    		)
    	if i == 2:
    		break

# функция для команды 2

def two(bot,update):
	
    driver.get('https://www.youtube.com/channel/UCdzKIxIaDm84e0bWooUf7cw' + "/videos")
    videos = driver.find_elements_by_id("video-title")
    for i in range(len(videos)):
    	url = videos[i].get_attribute('href')
    	tmp = str(url)
    	update.bot.send_message(
    		chat_id='@MoscowITproject',
    		text = tmp, disable_web_page_preview = False
    		)
    	if i == 2:
    		break

# функция start отвечает пользователю на стандартную команду /start при первом запуске бота

def start(bot, update):
	update.bot.send_photo(
		caption = menu_text,
		chat_id=bot.message.chat_id,
		photo=open('images/фон.jpg','rb'),
		reply_markup = key()
		)

# функция work отвечает пользователю на запрос при ручном вводе или нажатию на кнопку

def work(bot,update):
	bot.message.reply_text(	
		begin,
		reply_markup = inl(),
		)

def black_work(bot,update):(
	bot.message.reply_text(
		black_begin,
		reply_markup = black_inl()
		)
	)

# функция inl_but анализирует, какая из Inline кнопок была отправлена на сервер, и отправляет пользователю ответ

def inl_but(bot,update):

# практика	
	# задания
	if bot.callback_query.data == 'A':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/1.png','rb'),
			reply_markup = answer_A()	
			)
	if bot.callback_query.data == 'B':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/2_1.png','rb'),
			reply_markup = answer_B()	
			)
	if bot.callback_query.data == 'C':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/3_1.png','rb'),
			reply_markup = answer_С()	
			)
	if bot.callback_query.data == 'D':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/4_1.png','rb'),
			reply_markup = answer_D()	
			)
	if bot.callback_query.data == 'E':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/5_1.png','rb'),
			reply_markup = answer_E()	
			)
	# ответы
	# алгебра логики
	if bot.callback_query.data == 'A_1':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/1_2.png','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'A_2':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'A_3':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'A_4':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)

	# python

	if bot.callback_query.data == 'B_1':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'B_2':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'B_3':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/2_2.png','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'B_4':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)

	# системы счисления

	if bot.callback_query.data == 'С_1':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'С_2':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/3_2.png','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'С_3':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'С_4':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)

	# графы

	if bot.callback_query.data == 'D_1':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'D_2':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'D_3':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/4_2.png','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'D_4':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	# комбинаторика
	if bot.callback_query.data == 'E_1':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'E_2':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'E_3':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/ошибка.jpg','rb'),
			reply_markup = black_back()	
			)
	if bot.callback_query.data == 'E_4':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/5_2.png','rb'),
			reply_markup = black_back()	
			)
# -----------------------------------------------------------
	# условие для алгебры логики

	if bot.callback_query.data == '1':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			)

		update.bot.send_photo(
			chat_id=query.message.chat.id,
			photo=open('images/A_2.png','rb'),
			
			
			)
		update.bot.send_photo(
			chat_id=query.message.chat.id,
			caption=alg_log,
			photo=open('images/A_1.png','rb'),
			
			reply_markup = back()
			)

    # условие для Python	
		
	if bot.callback_query.data == '2':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id
			)
		update.bot.send_photo(
			caption=py,
			chat_id=query.message.chat.id,
			photo=open('images/B_1.png','rb'),
			reply_markup = back()
			)

	# условие для систем счисления

	if bot.callback_query.data == '3':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id
			)
		update.bot.send_photo(
			
			chat_id=query.message.chat.id,
			photo=open('images/C_1.png','rb'),
			
			)
		update.bot.send_photo(
			caption=ss,
			chat_id=query.message.chat.id,
			photo=open('images/C_2.png','rb'),
			reply_markup = back()
			)

	# условие для графов

	if bot.callback_query.data == '4':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id
			)
		update.bot.send_photo(
			caption=gr,
			chat_id=query.message.chat.id,
			photo=open('images/D_1.png','rb'),
			reply_markup = back()
			)

	# условие для комбинаторики

	if bot.callback_query.data == '5':
		query = bot.callback_query

		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id
			)
		update.bot.send_photo(
			caption=cb,
			chat_id=query.message.chat.id,
			photo=open('images/E_1.png','rb'),
			reply_markup = back()
			)

	# условие для возврата
	
	if bot.callback_query.data == '9':
		query = bot.callback_query


		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			
			reply_markup = inl()
			)
	if bot.callback_query.data == '9_1':
		query = bot.callback_query


		update.bot.editMessageReplyMarkup(
			
			chat_id=query.message.chat_id,
			message_id=query.message.message_id,
			
			reply_markup = black_inl()
			)


