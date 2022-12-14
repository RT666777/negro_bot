from cgitb import text
from itertools import tee
from aiogram import Bot, Dispatcher, executor, types
import logging
from states.create_profile_states import create_bot_profile
from aiogram import filters
from utils.dispatcher import dp
from handlers.me import get_my_profile
from states.setting_bot import *
from states.insert_promo import insert_promo
from states.select_skin import select_ext_skin_state
from states.choose_job import choose_your_job
from handlers.back_button import back_button
from handlers.cancel_button import cancel_button
from handlers.create_profile_bot import choose_nickname_state, choose_skin_color_state, create_profile_in_bot_function
from handlers.settings_bot import choose_new_skin_color, settings_bot
from handlers.settings_bot import choose_new_nickname
from handlers.settings_bot import set_new_nickname
from handlers.settings_bot import set_new_skin_color
from handlers.reputation import add_reputation
from handlers.reputation import rm_reputation
from handlers.process_start import process_start
from handlers.what_is_nigger import what_is_this_nigger
from handlers.promo import input_promo, second_state
from handlers.extension_skins import get_inventory, choose_ext_skin, ext_skin_set
from handlers.jobs import show_works, welder_job, enter_the_welder, welder_start_working, welder_working, taxi_job, enter_the_taxi, taxi_start_working, taxi_working, leave_from_job
from handlers.spenking_sheep import spenking_sheep

import sqlite3
from time import sleep as sl

from utils.anti_flood import anti_flood

logs_path = 'logs/log.log'
tg_channel_to_message = -611281422

#=====================================#
#--------------logging----------------#
#=====================================#
file_log = logging.FileHandler(logs_path)
console_out = logging.StreamHandler()

logging.basicConfig(handlers=(file_log, console_out), 
                    format='[%(asctime)s | %(levelname)s]: %(message)s', 
                    datefmt='%m.%d.%Y %H:%M:%S',
                    level=logging.INFO)

logging.info('\n\n---------------[Bot started!]---------------')

#=====================================#
#-------------bot-settings------------#
#=====================================#
    
def register_handlers_send_msg(dp: Dispatcher):
    dp.register_message_handler(process_start, commands='start')
    dp.register_message_handler(back_button, text=['?????????? ?? ????????'])
    dp.register_message_handler(cancel_button, text=['?????????????????? ?? ?????????????? ????????'], state='*')
    dp.register_message_handler(create_profile_in_bot_function, text=['?????????????? ????????????'])
    dp.register_message_handler(choose_nickname_state, state=create_bot_profile.CHOOSE_NICK)
    dp.register_message_handler(choose_skin_color_state, state=create_bot_profile.CHOOSE_SKIN_COLOR)
    dp.register_message_handler(get_my_profile, text=['Me', 'me', "??", "??"])
    dp.register_message_handler(settings_bot, text=['?????????????????? ????????????'])
    dp.register_message_handler(choose_new_nickname, text=['???????????????? ??????'])
    dp.register_message_handler(choose_new_skin_color, text=['???????????????? ???????? ????????????'])
    dp.register_message_handler(set_new_nickname, state=settings_bot_new.CHOOSE_NEW_NICKNAME)
    dp.register_message_handler(set_new_skin_color, state=settings_bot_new.CHOOSE_NEW_SKIN_COLOR)
    dp.register_message_handler(add_reputation, text=['+rep', 'rep+', '+Rep', 'Rep+', '+??????', '+??????', '??????+', '??????+'])
    dp.register_message_handler(rm_reputation, text=['-rep', 'rep-', '-Rep', 'Rep-', '-??????', '-??????', '??????-', '??????-'])
    dp.register_message_handler(what_is_this_nigger, text=['???? ???? ??????????', '???? ???? ??????????', '???? ???? ??????????', '???? ???? ??????????', '?????? ???? ??????????', '?????? ???? ??????????', '???? ???? ????????', '???? ???? ????????', '???? ???? ????????', '???? ???? ????????'])
    dp.register_message_handler(input_promo, text=['???????????? ????????????????'])
    dp.register_message_handler(second_state, state=insert_promo.STATE_1)
    dp.register_message_handler(get_inventory, text=['??????. ??????????'])
    dp.register_message_handler(choose_ext_skin, text=['?????????????? ????????'])
    dp.register_message_handler(ext_skin_set, state=select_ext_skin_state.STATE_1)
    dp.register_message_handler(show_works, text=['????????????'])
    dp.register_message_handler(welder_job, state=choose_your_job.STATE_1, text=['??????????????'])
    dp.register_message_handler(enter_the_welder, state=choose_your_job.WELDER_CHOOSE, text=['???????????????????? ??????????-????????????????'])
    dp.register_message_handler(welder_start_working, state=choose_your_job.WELDER_CHOOSE, text=['????????????????'])
    dp.register_message_handler(welder_working, state=choose_your_job.WELDER_WORKING, text=['???????????? ??????????'])
    dp.register_message_handler(taxi_job, state=choose_your_job.STATE_1, text=['??????????????'])
    dp.register_message_handler(enter_the_taxi, state=choose_your_job.TAXI_CHOOSE, text=['???????????????????? ??????????-??????????????????'])
    dp.register_message_handler(taxi_start_working, state=choose_your_job.TAXI_CHOOSE, text=['????????????????'])
    dp.register_message_handler(taxi_working, state=choose_your_job.TAXI_WORKING, text=['???????????? ??????????'])
    dp.register_message_handler(leave_from_job, state=choose_your_job.STATE_1, text=['?????????????????? ?? ????????????'])
    dp.register_message_handler(spenking_sheep, text=["?????????????? ????????"])

register_handlers_send_msg(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
