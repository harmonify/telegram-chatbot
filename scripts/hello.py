from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

if __name__ == '__main__':
    print('No direct access allowed!')
    exit()

def helloFn(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /hello is issued."""
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

hello = CommandHandler('hello', helloFn)
