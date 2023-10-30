import os.path
from datetime import datetime
from typing import Final

from utils.files import get_base_path


def get_log_path() -> str:
    path: Final[str] = os.path.join(get_base_path(), "logs", "log-" + str(datetime.now()).split('.')[0].replace(":", "-") + ".txt")
    open(path, "x").close()
    return path


def log(message: str) -> None:
    with open(log_path, "a") as file:
        file.write(str(message) + "\n")


log_path = get_log_path()
