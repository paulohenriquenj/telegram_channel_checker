

class fans_off:

    def __init__(self, next=None):
        self.next = next

    def telegram_command(self):
        return '/fan_off'

    def action(self, telegram_msg):
        if telegram_msg == self.telegram_command():
            print('Vamos deligar os fans')
            return

        if self.next:
            self.next.action(telegram_msg)
