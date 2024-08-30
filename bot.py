from telegram.ext import Application, CommandHandler, MessageHandler, filters

async def start(update, context):
    await update.message.reply_text('Привет! Я ваш бот.')

async def echo(update, context):
    message = update.message.text
    try:
        num = int(message)
        result = num ** 2
        await update.message.reply_text(f'Квадрат вашего числа: {result}')
    except ValueError:
        await update.message.reply_text(message)

def main():
    application = Application.builder().token("7363980286:AAGwEDjYfxM2ibb3jYRnbX8WRLi9iXBYtPc.").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == '__main__':
    main()
