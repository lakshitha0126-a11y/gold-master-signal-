import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID', '0'))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Welcome to Gold Master Signal!\n\n'
        'Use /help to see commands.'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        '/start - Start bot\n'
        '/help - Help\n'
        '/signal BUY or SELL - Admin signal'
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('Admin only.')
        return
    message = ' '.join(context.args)
    if not message:
        await update.message.reply_text('Usage: /signal BTCUSDT BUY Entry 90000 SL 89000 TP 92000')
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='📊 GOLD MASTER SIGNAL\n\n' + message
    )

if __name__ == '__main__':
    if not TOKEN or not ADMIN_ID:
        raise RuntimeError('Set BOT_TOKEN and ADMIN_ID environment variables')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('signal', signal))
    print('Gold Master Signal Bot started')
    app.run_polling()
