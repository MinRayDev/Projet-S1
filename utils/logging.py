from datetime import datetime
from utils.files import get_base_path


def set_log_path() -> str:
    path: str = get_base_path() + "/logs/log-" + str(datetime.now()).split('.')[0].replace(":", "-") + ".txt"
    file = open(path, "x")
    file.close()
    return path


def log(message: str) -> None:
    with open(log_path, "a") as file:
        file.write(str(message) + "\n")


log_path = set_log_path()
