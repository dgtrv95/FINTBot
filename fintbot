import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Словарь для хранения количества монет пользователей
user_coins = {}

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    update.message.reply_text(f'Привет! Нажми на монету, чтобы заработать FINT монеты. У тебя сейчас {user_coins[user_id]} FINT.',
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪙", callback_data='click')]]))

# Обработка нажатий на кнопку
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    user_id = update.effective_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    user_coins[user_id] += 1
    query.edit_message_text(text=f'Ты заработал 1 FINT монету! У тебя сейчас {user_coins[user_id]} FINT.',
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪙", callback_data='click')]]))

# Обработка ошибок
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    # Вставьте сюда ваш токен Telegram Bot API
    token = 'YOUR_TELEGRAM_BOT_TOKEN'
    updater = Updater(token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
