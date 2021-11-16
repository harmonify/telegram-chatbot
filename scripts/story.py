from telegram import Update
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

if __name__ == '__main__':
    print('No direct access allowed!')
    exit()

def storyFn(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Once upon a time, lived a young man named {update.effective_user.full_name}...')

story = CommandHandler('story', storyFn)
