import schedule
import time


def display_messsage(message):
    print(message)
    return schedule.CancelJob


def schedule_message(message, at):
    schedule.every().day.at(at).do(display_messsage, message)
    print('Message scheduled at {}'.format(at))
    while True:
        schedule.run_pending()
        time.sleep(1)


schedule_message('Client meeting', '16:04')
