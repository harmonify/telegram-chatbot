import os
from dotenv import load_dotenv
from telegram.ext import Updater
from scripts.hello import hello
from scripts.story import story

def main(args=None):
    """The main routine."""
    load_dotenv()

    apiToken = os.getenv('API_TOKEN')
    updater = Updater(token=apiToken, use_context=True)

    # Add handlers
    updater.dispatcher.add_handler(story)
    updater.dispatcher.add_handler(hello)

    updater.start_polling()
    updater.idle()

    return 0

if __name__ == '__main__':
    main()
