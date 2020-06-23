from zipfile import ZipFile
import os
import zipfile
import subprocess
from bomb_builder import myLocalDirectory as myDirectory

extension = ".zip"


def triggerBombXTimes(x):
    for i in range(x):
        os.chdir(myDirectory)
        for item in os.listdir(myDirectory):
            if item.endswith(extension):
                file_name = os.path.abspath(item)
                zip_ref = zipfile.ZipFile(file_name)
                zip_ref.extractall("{}\Bomb{}".format(myDirectory, i))
                zip_ref.close()
                subprocess.Popen(r'explorer /select,' +
                                 "{}\Bomb{}".format(myDirectory, i) + r'\test 0.txt')
