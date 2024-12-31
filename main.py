from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

class NewYearBot:
    def __init__(self, token: str):
        self.token = token
        self.updater = Updater(token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.greetings = [
            "Happy New Year! May all your dreams come true this year!",
            "Wishing you happiness, good luck, and all your desires fulfilled in the coming year!",
            "Happy New Year! May this year bring more joy, laughter, and good events!",
            "Happy New Year! May your home be filled with warmth, and your life with light and happiness!"
        ]
        self._setup_handlers()

    def _setup_handlers(self):
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(CommandHandler("greet", self.greet))

    def start(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text("Hey! I'm the New Year bot. Type /greet to get a special greeting!")

    def greet(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(random.choice(self.greetings))

    def run(self):
        self.updater.start_polling()
        self.updater.idle()

def main():
    bot = NewYearBot(token='YOUR_BOT_TOKEN')
    bot.run()

if __name__ == '__main__':
    main()
