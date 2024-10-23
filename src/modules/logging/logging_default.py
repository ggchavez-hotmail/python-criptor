import json
import time
from colorama import Fore, Style

ERROR = "ERROR"
WARN = "WARN"
CODE_INFO = 200
CODE_ERROR = 500
CODE_WARN = 400


def get_color(level):
    if level == WARN:
        return Fore.YELLOW
    elif level == ERROR:
        return Fore.RED
    else:
        return Fore.WHITE


def get_status_by_level(level):
    if level == WARN:
        return CODE_WARN
    elif level == ERROR:
        return CODE_ERROR
    else:
        return CODE_INFO


def log_final(level, log_data):
    color = get_color(level)
    log_message = f'{color}{level.upper()}: {Style.RESET_ALL}'
    log_message += json.dumps(log_data, indent=4,
                              ensure_ascii=False, sort_keys=True)
    print(log_message)


def logger(level, message):
    log_data = {
        "Timestamp": int(time.time()),
        "Status": get_status_by_level(level),
        "Message": message
    }
    log_final(level, log_data)
