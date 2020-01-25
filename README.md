# telegram_channel_checker
> Checks a telegram channel and executes actions according messages.

# Install
https://github.com/python-telegram-bot/python-telegram-bot
pip3 install python-telegram-bot --upgrade

https://pypi.org/project/python-dotenv/
pip install python-dotenv

# Set .env info

>
'TELEGRAM_TOKEN': Telegram bot token.  
'CHAT_ID': Chat to listen
'ALLOWED_USER': Users allowed to send commands.

# Create actions

> To create action, use the existing actions as model.

# Registering action

> Make a chain of actions in run_telegram_listener.py

# Run or schedule
python run_telegram_listener.py
