from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler, CallbackContext
import random

# lista delle mosse possibili del bot
mosse_bot = [
    "Carta",
    "Forbici",
    "Sasso"
]

def morra(update: Update, context: CallbackContext) -> None:


    # definizione pulsanti
    keyboard = [
        [
            InlineKeyboardButton("Si", callback_data='Si'),
            InlineKeyboardButton("No", callback_data='No'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('vuoi giocare sul serio a morra cinese?', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    query.answer()

    answer = query.data
    
    # se vuoi giocare parte la scelta della mossa che vuoi fare
    if answer == 'Si':
        play(update, context)
    elif answer == 'No':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Ok, allora ciao")
    else:
        genera_mossa(update, context, answer) # il bot fa la sua mossa
        
# metodo in cui si sceglie che mossa fare
def play(update, context):

    button_list = [
        InlineKeyboardButton("Carta", callback_data='Carta'),
        InlineKeyboardButton("Forbici", callback_data='Forbici'),
        InlineKeyboardButton("Sasso", callback_data='Sasso')
    ]

    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2)) 
    context.bot.send_message(chat_id=update.effective_chat.id,  text="Scegli la mossa", reply_markup=reply_markup)

# costruisco menu per le scelte
def build_menu(buttons,n_cols,header_buttons=None,footer_buttons=None):

  menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]

  if header_buttons:
    menu.insert(0, header_buttons)
  if footer_buttons:
    menu.append(footer_buttons)
  return menu

# generazione mossa casuale da parte del bot
# controllo su chi vince
def genera_mossa(update, context, answer):

    index = random.randint(0, len(mosse_bot)-1)
    mossa_casuale_bot = mosse_bot[index] # mossa casuale che effettuerà il bot

    print("Il bot ha scelto: " + mossa_casuale_bot)
    if answer == 'Carta' and mossa_casuale_bot == 'Forbici':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Peccato, hai perso..." + mossa_casuale_bot + " batte " + answer)

    elif answer == 'Carta' and mossa_casuale_bot == 'Sasso':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Diamine, ho perso..." + answer + " batte " + mossa_casuale_bot)

    elif answer == 'Carta' and mossa_casuale_bot == 'Carta':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Pari zio porco")

    elif answer == 'Forbici' and mossa_casuale_bot == 'Carta':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Diamine, ho perso..." + answer + " batte " + mossa_casuale_bot)

    elif answer == 'Forbici' and mossa_casuale_bot == 'Sasso':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Peccato, hai perso... " + mossa_casuale_bot + " batte " + answer)

    elif answer == 'Forbici' and mossa_casuale_bot == 'Forbici':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Pari zio cane")
    elif answer == 'Sasso' and mossa_casuale_bot == 'Carta':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Peccato, hai perso..." + mossa_casuale_bot + " batte " + answer)

    elif answer == 'Sasso' and mossa_casuale_bot == 'Forbici':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Diamine, ho perso..." + answer + " batte " + mossa_casuale_bot)

    elif answer == 'Sasso' and mossa_casuale_bot == 'Sasso':
        context.bot.send_message(chat_id=update.effective_chat.id,  text="Pari")




