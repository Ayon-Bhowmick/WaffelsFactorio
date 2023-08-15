import os
from sys import platform
import shutil
from zipfile import ZipFile

SAVE_PATH_WIN = f"\\Users\\{os.getlogin()}\\AppData\\Roaming\\Factorio\\saves"
SAVE_PATH_MAC = "~/Library/Application Support/factorio/saves"

def push():
    shutil.copyfile(save_path, os.getcwd() + "\\waffle.zip")
    with ZipFile("./waffle.zip", "r") as zipObj:
        zipObj.extractall("./waffle")
    os.remove("./waffle.zip")

def pull():
    pass

if __name__ == "__main__":
    if platform == "win32":
        print("Windows detected")
        assert os.path.exists(SAVE_PATH_WIN), "Path does not exist"
        save_path = SAVE_PATH_WIN + "\\waffle.zip"
        push()
    else:
        pass
