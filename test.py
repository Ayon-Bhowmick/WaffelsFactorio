from zipfile import ZipFile
import shutil
import os

SAVE_PATH_WIN = f"\\Users\\{os.getlogin()}\\AppData\\Roaming\\Factorio\\saves\\waffle.zip"

def get_paths():
    file_paths = []
    for root, directories, files in os.walk("./waffle"):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    print(file_paths)
    return file_paths

with ZipFile("./waffle.zip", "w") as zip:
    for file in get_paths():
        zip.write(file)
with ZipFile("./waffle.zip", "r") as zipObj:
        zipObj.extractall("./waffle")
# shutil.copyfile("./waffle.zip", SAVE_PATH_WIN)
