import random 

unknown_messages = [
    "cazzo fai? questo non è un comando",
    "zio porco, cosa vuol dire?!",
    "Ch'ha detto?",
    "Questo non è un comando. Per sta volta passi, la prossima volta chiamo la PPPPPPPPPolizia"
]

greetings = [
    "Ciao",
    "Mandi",
    "Buonasega",
    "Buongiorno",
    "Ben tornato",
    "Ciao amore",
    "Yooo",
    "Ehilà",
    "Salve",

]


def saluti(update, context):
    
    user = update['message']['message_id']
    username = update['message']['from_user']['username'] # mi da from = None 
    context.bot.send_message(chat_id=update.effective_chat.id, text = generate_random_messages(greetings, username))
    
def unknown_command(update, context):

    context.bot.send_message(chat_id=update.effective_chat.id, text = generate_unknown_messages()) 

def generate_random_messages(array_messages, username):
    
    index = random.randint(0, len(array_messages)-1)

    if greetings[index] != "Ciao amore":

        if username == 'ilvenerabilemaestro':
            return greetings[index] + ' Maestro'
        
        elif username == 'Figor98':
            return greetings[index] + ' Igor!'
        
        elif username == 'Max989898':
            return greetings[index] + ' Mago'
        
        elif username == 'valeriadm_98':
            return greetings[index] + ' Valeria'
        
        elif username == 'F_i_l_ippo':
            return greetings[index] + ' Fil'
        
        else:
            return greetings[index] + ' chiunque tu sia'
        
    
    else:
        return greetings[index]

def generate_unknown_messages():

    index = random.randint(0, len(unknown_messages)-1)
    return unknown_messages[index]

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


