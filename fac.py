import os
from sys import platform
import shutil
from zipfile import ZipFile
from datetime import date, datetime
import pytz
import subprocess

SAVE_PATH_WIN = f"\\Users\\{os.getlogin()}\\AppData\\Roaming\\Factorio\\saves"
SAVE_PATH_MAC = "~/Library/Application Support/factorio/saves"

def get_paths():
    file_paths = []
    for root, directories, files in os.walk("./waffle"):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def push():
    shutil.copyfile(save_path, os.getcwd() + "\\waffle.zip")
    # with ZipFile("./waffle.zip", "r") as zipObj:
    #     zipObj.extractall("./waffle")
    # os.remove("./waffle.zip")
    os.system("git add *")
    time = datetime.now(pytz.timezone("America/New_York"))
    current_time = time.strftime("%H:%M:%S")
    os.system(f"git commit -m \"Update {date.today()} {current_time}\"")
    os.system("git push")

def pull():
    new_save = "Already up to date." not in str(subprocess.check_output("git pull", shell=True))
    if True:
        # with ZipFile("./waffle.zip", "w") as zip:
        #     for file in get_paths():
        #         zip.write(file)
        shutil.copyfile("./waffle.zip", save_path)
    else:
        print("no new save")

if __name__ == "__main__":
    if platform == "win32":
        print("Windows detected")
        assert os.path.exists(SAVE_PATH_WIN), "Path does not exist"
        save_path = SAVE_PATH_WIN + "\\waffle.zip"
    else:
        pass
    push()
