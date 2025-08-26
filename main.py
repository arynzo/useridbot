from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8165417080:AAG_OZzbR1JGYfIwfjaSQYvF_zrhgWSTNjw"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = [[KeyboardButton("ID Fetcher", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True, one_time_keyboard=True)
    
    await update.message.reply_text("👇 Click button to share a contact:", reply_markup=reply_markup)

# Jab user contact share kare
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    if contact:
        user_id = contact.user_id
        phone = contact.phone_number
        first_name = contact.first_name
        await update.message.reply_text(f"✅ Contact Received:\n\n👤 Name: {first_name}\n📱 Phone: {phone}\n🆔 User ID: {user_id}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.CONTACT, contact_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
