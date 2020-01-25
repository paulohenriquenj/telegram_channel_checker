from telegram_helper import telegram_helper
from telegram_commands import telegram_commands

from actions.camera_send_record import camera_send_record
from actions.fans_off import fans_off
from actions.no_action import no_action


telegram = telegram_helper()
chain = camera_send_record(
        fans_off(
            no_action(
                
            )
        )
    )

for update in telegram.verify_updates():
    chain.action(update.message.text)


# t = telegram_helper(
#     camera_send_record(
#         fans_off(
#             no_action(
                
#             )
#         )
#     )
# )
# t.verify_updates()