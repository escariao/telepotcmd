
# based on telepot.readthedocs.io
# -*- coding: utf-8 -*-

import datetime  # Importing the datetime library
import telepot   # Importing the telepot library
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot
from time import sleep      # Importing the time library to provide the delays in program
import subprocess

now = datetime.datetime.now() # Getting date and time

def handle(msg):
    chat_id = msg['chat']['id'] # Receiving the message from telegram
    command = msg['text']   # Getting text from the message

    print ('Received:')
    print(command)

    # Comparing the incoming message to send a reply according to it
    getCommand =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    psaux =  getCommand.read()	
    bot.sendMessage(chat_id, str("Command result: \n") + str(psaux.decode()))
	
# Insert your telegram token below
bot = telepot.Bot('token_here')
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)


