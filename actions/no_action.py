

class no_action:

    def __init__(self, next=None):
        self.next = next

    def action(self, telegram_msg):
        print('No action recognized.')
