
from telegram_helper import telegram_helper
from record_video import record_video

class camera_send_record:

    def __init__(self, next=None):
        self.next = next

    def telegram_command(self):
        return '/status'

    def action(self, telegram_msg):
        if telegram_msg == self.telegram_command():
            record_video().record_video_time(10)
            telegram_helper().send_video(
                record_video.file_mp4
            )
            return

        if self.next:
            self.next.action(telegram_msg)
