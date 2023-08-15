import os
from sys import platform, argv
import shutil
from datetime import date, datetime
import pytz
import subprocess

SAVE_PATH_WIN = f"\\Users\\{os.getlogin()}\\AppData\\Roaming\\Factorio\\saves"
SAVE_PATH_MAC = "~/Library/Application Support/factorio/saves"

def push():
    shutil.copyfile(save_path, os.getcwd() + "\\waffle.zip")
    os.system("git add *")
    current_time = datetime.now(pytz.timezone("America/New_York"))
    current_time_str = current_time.strftime("%H:%M:%S")
    os.system(f"git commit -m \"Saved {date.today()} {current_time_str}\"")
    os.system("git push")

def pull():
    assert "Already up to date." not in str(subprocess.check_output("git pull", shell=True)), "No new save"
    shutil.copyfile("./waffle.zip", save_path)

if __name__ == "__main__":
    if platform == "win32":
        print("Windows detected")
        assert os.path.exists(SAVE_PATH_WIN), "Path does not exist"
        save_path = SAVE_PATH_WIN + "\\waffle.zip"
    elif platform == "darwin":
        print("Mac detected")
        assert os.path.exists(SAVE_PATH_MAC), "Path does not exist"
        save_path = SAVE_PATH_MAC + "/waffle.zip"
    assert len(argv) == 1, "Incorrect number of arguments"
    assert argv[0] in ("pull, push"), "Invalid argument"
    eval(argv[0] + "()")
