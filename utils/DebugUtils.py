from utils import References
from datetime import datetime


def get_log_path():
    path: str = References.base_path + "logs\\log " + str(datetime.now()).split('.')[0].replace(":", "-") + ".txt"
    f = open(path, "x")
    f.close()
    return path


def log(message: str, path):
    file = open(path, "a")
    file.write(str(message) + "\n")
    file.close()
