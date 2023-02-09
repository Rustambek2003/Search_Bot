from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from tinydb import TinyDB
from tinydb.table import Document


admin_id = '996172963'
db = TinyDB('kinolar.json',indent = 4)
TOKEN = '5766174948:AAERI4lwWYzIfSPaLDBE9gWugxMpNAMgmVE'

def start(update:Update, context:CallbackContext):
    bot = context.bot
    # chat_id = update.message.chat.id
    keyboar = ReplyKeyboardMarkup([
        ["Admin panel", 'Statistika']
    ])

    bot.sendMessage(chat_id=admin_id,text="Assalomu alaykum 𓅓\n\nKino kodini kiriting ✔️", reply_markup=keyboar)
    # bot.sendMessage(chat_id=chat_id,text="Assalomu alaykum 𓅓\n\nKino kodini kiriting ✔️")
    
def admin(update:Update, context:CallbackContext):
    bot = context.bot
    Keyboar = ReplyKeyboardMarkup([
        ["Kino qo'shish", "Kinoni o'chirish"]
    ])
    bot.sendMessage(chat_id = admin_id,
    text = "Admin paneldasiz",
    reply_markup = Keyboar
    )

def qushish(update:Update, context:CallbackContext):
    bot = context.bot
    msg_id = update.message.message_id

    bot.sendMessage(chat_id = admin_id,text='Kino kodini kiriting: ')
    msg_kod = update.message.message_id
    while msg_id != msg_kod:
        kod = update.message.text

    bot.sendMessage(chat_id = admin_id,text='Kinoni tashlang: ')
    msg_kino = update.message.message_id
    while msg_id != msg_kino:
        Id = update.message.video
        Text = update.message.text

    kino = Document({
        "Id":Id,
        "text":Text
    },doc_id = kod)
    db.insert(kino)
    bot.sendMessage(chat_id = admin_id,text="Kino saqlandi")
    

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Admin panel'),admin))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Kino qo'shish"),qushish))

updater.start_polling()
updater.idle()