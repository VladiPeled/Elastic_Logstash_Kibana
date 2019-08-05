import datetime
import json
import logging
import random
import threading
from copy import copy
from time import sleep

COMPONENTS = [("USER_APPLIED", 4, 6), ("BUSINESS_CREDIT_REPORTS", 7, 9), ("SEASONALITY", 4, 6),
              ("BUSINESS_STATE_771", 6, 8),
              ("BV_STRATEGY", 3, 5)]
USER_EVERY_X_SECONDS = 10

LOG_FILE = 'general.log'

LOG_MESSAGE = {"message": "client event", "level": "INFO", "logger_name": "rto.bv_utils.real_time_offer",
               "path": "/opt/bluevine/py-packages/bv_utils/real_time_offer.py", "stack_trace": "", "alert": False,
               "levelno": 20, "pathname": "/opt/bluevine/py-packages/bv_utils/real_time_offer.py",
               "filename": "real_time_offer.py", "module": "real_time_offer", "exc_text": None, "stack_info": None,
               "lineno": 151, "funcName": "_log_statistics", "created": 1561640281.6117356,
               "msecs": 611.7355823516846, "relativeCreated": 2420.635938644409, "thread": 139832278255424,
               "threadName": "MainThread", "processName": "MainProcess", "process": 23323,
               "hash_key": "EMAIL_COMPARISONS.END", "hash_name": "55902", "event_id": "EMAIL_COMPARISONS",
               "user_id": "55902", "user_status": "N/A", "event_status": "FAILURE",
               "timestamp": "2019-06-27T12:58:01.610342", "component": "Risk",
               "@timestamp": "2019-06-27T12:58:01.611Z", "tags": [], "service_name": "Risk",
               "process_type": "risk script", "process_env": "ec2",
               "service_hostname": "staging-af-riskob-2-i-0a07d47e63945096f.bluevine.com",
               "operator_name": "email_comparisons", "owner": "dvir.naim",
               "execution_date": "2019-06-27 11:50:58.844259+00:00"}

# LOG_MESSAGE = {}


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
    message = copy(LOG_MESSAGE)
    message['user_id'] = str(user_id)
    message['event_status'] = event_status
    message['event_id'] = event_id
    message['timestamp'] = start_timestamp.isoformat()
    message['@timestamp'] = start_timestamp.isoformat()
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
