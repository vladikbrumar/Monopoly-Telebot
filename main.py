import player as pl
import property as prop
import bank as bank
import random as rand

import telebot as bot

bot = bot.TeleBot('987522251:AAEdyv5lZ7XZZCaziQHyceF80sXeHxzeqjM')

# some global variables
pl_name = {}
players = {}
# default variables for init player's account
bank_money = 1000000
default_player_money = 1500
default_player_property = {}
default_player_name = 'player' + str(rand.randint(1, 1000000))

# 'say' hello and run bot
@bot.message_handler(commands=['hello'])
def start_message(message):
    # without sense, just for practice and fun :)
    # get name from user's message, if first time add to dict
    global pl_name
    curr_user = message.from_user
    if pl_name.get(curr_user.id) is None:
        pl_name[curr_user.id] = curr_user.first_name
    bot.send_message(message.chat.id, pl_name[curr_user.id] + ', чего тебе?')


# players add theyself into game
@bot.message_handler(commands=['play'])
def play_message(message):
    global players
    # default bot's message if nothing works
    mess_str = 'я забыл, что хотел сказать. хе-хе'

    # set a user to work with and init him as a player ahead
    curr_user = message.from_user

    # check and add first time user into game and create message for him
    if players.get(message.from_user.id) is None:
        if curr_user.first_name is None:
            players[curr_user.id] = pl.Player(default_player_name, default_player_money, default_player_property)
        else:
            players[curr_user.id] = pl.Player(curr_user.first_name, default_player_money, default_player_property)
        # player added
        mess_str = 'Игрок ' + players[curr_user.id].name + ' успешно добавлен в игру. \nФинансовое состояние:\n' + \
                   str(players[curr_user.id].money) + '\nСобственность:\n' + players[curr_user.id].get_properties_stat()
    else:
        # player has been already added
        mess_str = '' + players[curr_user.id].name + ' уже был добавлен в игру. \nФинансовое состояние:\n' + \
                   str(players[curr_user.id].money) + '\nСобственность:\n' + players[curr_user.id].get_properties_stat()

    # bot's message for each user
    bot.send_message(message.chat.id, mess_str)


bot.polling()
