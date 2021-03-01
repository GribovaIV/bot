from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

# функция key служит для создания кнопок

def key():
	MyKeyboard = ReplyKeyboardMarkup(
		[['Теория 📖'],['Практика ✏️'],['В главное меню 🚪']],
		resize_keyboard = True)
	return MyKeyboard

# фунция inl служит для создания Inline кнопок

def inl():
	inline = InlineKeyboardMarkup([
			[InlineKeyboardButton('Алгебра логики 📚', callback_data='1')],
			[InlineKeyboardButton('Основа Python 🐍', callback_data='2')],
			[InlineKeyboardButton('Системы счисления 📐', callback_data='3')],
			[InlineKeyboardButton('Графы 🌌', callback_data='4')],
			[InlineKeyboardButton('Комбинаторика 🧩', callback_data='5')],

		])

	return inline

# функция практики

def black_inl():
	black_inline = InlineKeyboardMarkup([
			[InlineKeyboardButton('Алгебра логики 📚', callback_data='A')],
			[InlineKeyboardButton('Python 🐍', callback_data='B')],
			[InlineKeyboardButton('Системы счисления 📐', callback_data='C')],
			[InlineKeyboardButton('Графы 🌌', callback_data='D')],
			[InlineKeyboardButton('Комбинаторика 🧩', callback_data='E')],
			])
	return black_inline


# функция back служит для процесса возврата в меню

def back():
	inline_back = InlineKeyboardMarkup([[
			InlineKeyboardButton('Назад', callback_data='9'),
		]])
	return inline_back

def black_back():
	inline_back = InlineKeyboardMarkup([[
			InlineKeyboardButton('Назад', callback_data='9_1'),
		]])
	return inline_back

# Inline-клавиатура для ответов

def answer_A():
	inline_answer_A = InlineKeyboardMarkup([
				[InlineKeyboardButton('Ответ 32', callback_data='A_1')],
				[InlineKeyboardButton('Ответ 16', callback_data='A_2')],
				[InlineKeyboardButton('Ответ 15', callback_data='A_3')],
				[InlineKeyboardButton('Ответ 34', callback_data='A_4')],
			])
	return inline_answer_A

def answer_B():
	inline_answer_B = InlineKeyboardMarkup([
				[InlineKeyboardButton('Ответ 106 48438', callback_data='B_1')],
				[InlineKeyboardButton('Ответ 140 8613', callback_data='B_2')],
				[InlineKeyboardButton('Ответ 8815 9225', callback_data='B_3')],
				[InlineKeyboardButton('Ответ 2013 99958', callback_data='B_4')],
			])
	return inline_answer_B

def answer_С():
	inline_answer_С = InlineKeyboardMarkup([
				[InlineKeyboardButton('Ответ 53', callback_data='С_1')],
				[InlineKeyboardButton('Ответ 3', callback_data='С_2')],
				[InlineKeyboardButton('Ответ 12', callback_data='С_3')],
				[InlineKeyboardButton('Ответ 4', callback_data='С_4')],
			])
	return inline_answer_С

def answer_D():
	inline_answer_D = InlineKeyboardMarkup([
				[InlineKeyboardButton('Ответ 32', callback_data='D_1')],
				[InlineKeyboardButton('Ответ 24', callback_data='D_2')],
				[InlineKeyboardButton('Ответ 4', callback_data='D_3')],
				[InlineKeyboardButton('Ответ 6', callback_data='D_4')],
			])
	return inline_answer_D

def answer_E():
	inline_answer_E = InlineKeyboardMarkup([
				[InlineKeyboardButton('Ответ 768', callback_data='E_1')],
				[InlineKeyboardButton('Ответ 840', callback_data='E_2')],
				[InlineKeyboardButton('Ответ 625', callback_data='E_3')],
				[InlineKeyboardButton('Ответ 80', callback_data='E_4')],
			])
	return inline_answer_E