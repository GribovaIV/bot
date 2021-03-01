from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from config import tocken
from handlers import *


# функция main запускает бота 	

def main():
	bot = Updater(tocken)
	bot.start_polling()
	bot.dispatcher.add_handler(CommandHandler('start',start))
	
	bot.dispatcher.add_handler(MessageHandler(Filters.regex('Теория'),work))
	bot.dispatcher.add_handler(MessageHandler(Filters.regex('В главное меню'),start))
	bot.dispatcher.add_handler(MessageHandler(Filters.regex('Практика'),black_work))	
	bot.dispatcher.add_handler(CallbackQueryHandler(inl_but))

	bot.dispatcher.add_handler(CommandHandler('help',help_1))
	bot.dispatcher.add_handler(MessageHandler(Filters.regex('/help'),help_2))

	bot.dispatcher.add_handler(MessageHandler(Filters.regex('/1'),one))
	bot.dispatcher.add_handler(MessageHandler(Filters.regex('/2'),two))

	
	bot.idle()

# стандартный запуск функции main

if __name__ == '__main__':
	main()