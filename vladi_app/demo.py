from time import sleep

import datetime
import json
import logging
import random
import threading

COMPONENTS = [("LANDING", 4, 6), ("CLEANING_AIRPLANE", 7, 9), ("SECURITY_CHECK", 4, 6),
              ("PASSENGERS_ONBOARDING", 6, 8),
              ("TAKEOFF", 3, 5)]
USER_EVERY_X_SECONDS = 10
LOG_FILE = 'general.log'


def set_logging():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.FileHandler(LOG_FILE)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)


def notify(event_status, event_id, user_id):
    start_timestamp = datetime.datetime.now()
    message = {}
    message['user_id'] = str(user_id)
    message['event_status'] = event_status
    message['event_id'] = event_id
    message['timestamp'] = start_timestamp.isoformat()
    logging.info(json.dumps(message))


def single_component_run(name: str, user_id: int, duration_start: float, duration_end: float) -> None:
    reg_duration = random.uniform(duration_start, duration_end)
    notify('STARTED', name, str(user_id))
    sleep(reg_duration)
    notify('SUCCESS', name, str(user_id))


def loan_process(user_id: int):
    for component in COMPONENTS:
        single_component_run(name=component[0],
                             user_id=user_id,
                             duration_start=component[1],
                             duration_end=component[2])


if __name__ == '__main__':
    set_logging()
    user_num = 0
    while True:
        user_num += 1
        t = threading.Thread(target=loan_process, args=(user_num,))
        t.start()
        sleep(USER_EVERY_X_SECONDS)
