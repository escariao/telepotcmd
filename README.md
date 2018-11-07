# telepotcmd
An adaptation to send via telegram commands to your OS.


# Installation
------------

First Update and Upgrade

`$ sudo apt-get update`

`$ sudo apt-get upgrade`

pip:

`$ pip install telepot`

`$ pip install telepot --upgrade  # UPGRADE`
    
Get a token
-----------

To use the `Telegram Bot API <https://core.telegram.org/bots/api>`_, you first
have to `get a bot account <http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/>`_
by `chatting with BotFather <https://core.telegram.org/bots#6-botfather>`_.

BotFather will give you a **token**, something like ``123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ``.
With the token in hand, you can start using telepot to access the bot account.

Test the account
----------------

    >>> import telepot
    >>> bot = telepot.Bot('***** PUT YOUR TOKEN HERE *****')
    >>> bot.getMe()
    {'first_name': 'Your Bot', 'username': 'YourBot', 'id': 123456789}


Edit your Bot (thecmdBot.py)
----------------
Just go to the line `bot = telepot.Bot('')` and put your token

Ok, now run `python thecmdBot.py`
