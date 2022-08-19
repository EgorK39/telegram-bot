import telebot
from config import TOKEN, keys
from extensions import APIException, CryptoCripto

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def help(message: telebot.types.Message):
    text = "Для начала работы введите комманду боту в следующем формате:\n<имя валюты, цену на которую надо узнать> " \
           "\n<имя валюты, в которой надо узнать цену первой валюты> " \
           "\n<количество переводимой валюты> \nУвидеть список всех оступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты: "
    for key in keys.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text"])
def convert(message: telebot.types.Message):
    try:
        text_splited = message.text.split(" ")
        if len(text_splited) != 3:
            raise APIException("Слишком много значений, попробуй еще раз!")
        base, quote, amount = text_splited
        nummer2_2 = CryptoCripto.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя. \n{e} ")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду \n{e} ")
    else:
        text = f"Цена {amount} {base} в {quote} - {nummer2_2 * float(amount)}"
        bot.send_message(message.chat.id, text)


bot.polling()
