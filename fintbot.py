import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, Application

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Словарь для хранения количества монет пользователей
user_coins = {}

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    await update.message.reply_text(f'Привет! Нажми на монету, чтобы заработать FINT монеты. У тебя сейчас {user_coins[user_id]} FINT.',
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪙", callback_data='click')]]))

# Обработка нажатий на кнопку
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    user_id = update.effective_user.id
    if user_id not in user_coins:
        user_coins[user_id] = 0
    user_coins[user_id] += 1
    await query.edit_message_text(text=f'Ты заработал 1 FINT монету! У тебя сейчас {user_coins[user_id]} FINT.',
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪙", callback_data='click')]]))

# Обработка ошибок
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    # Вставьте сюда ваш токен Telegram Bot API
    token = '7466076481:AAHA2cmHsrfqlcYbrrrt00VBnh41jMHxtVE'
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_error_handler(error)

    application.run_polling()

if __name__ == '__main__':
    main()
