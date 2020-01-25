import telegram
import os
from dotenv import load_dotenv
import logging 

load_dotenv()


class telegram_helper:

    env_vars = ['TELEGRAM_TOKEN', 'CHAT_ID', 'ALLOWED_USER']
    telegram_token = ''
    chat_id = ''
    allowed_user = ''

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.load_env_info()
        self.bot = telegram.Bot(token=self.telegram_token)

    def load_env_info(self):
        for env_var in self.env_vars:
            try:
                setattr(self, env_var.lower(), os.getenv(env_var))
            except Exception as e:
                print(e)
                exit()

    def send_video(self, video_path):
        ''' Send video to telegram chat '''
        logging.info('Send video')
        self.bot.send_video(
            chat_id=self.chat_id,
            video=open(video_path, 'rb'),
            supports_streaming=True,
            timeout=120
        )

    def get_channel_msg(self):
        print(self.bot.get_updates())

    def is_msg_from_authorized_user(self, user_name):
        if self.allowed_user == '*':
            return True
        
        if user_name in self.allowed_user:
            return True

        return False

    def verify_updates(self):
        updates = self.bot.get_updates()

        logging.info(f'{len(updates)} msgs found')

        for update in updates:
            logging.debug('------')
            logging.debug(update.update_id)
            logging.debug(update.message.text)
            logging.debug('------')

            if self.is_msg_from_authorized_user(update.message.from_user.name) and self.is_update_msg_id_greater_than_last_executed(update):
                logging.info ('Exec command')
                self.write_message_id(update)
                yield update

    def is_update_msg_id_greater_than_last_executed(self, update):
        if os.path.isfile('msg_last_executed_id'):
            file_id = open('msg_last_executed_id', 'r')
            content = file_id.read()
            file_id.close()

            logging.debug(f'content_id [{content}] ')
            logging.debug(f'msg_id [{update.message.message_id}] ')
            
            if content and  update.message.message_id > int(content):
                return True

        return False

    def write_message_id(self, update):
        file_id = open("msg_last_executed_id", 'w')
        file_id.write(str(update.message.message_id))
        file_id.close()
