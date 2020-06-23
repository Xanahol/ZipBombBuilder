from zipfile import ZipFile
import os
import zipfile
import subprocess
from bomb_builder import myLocalDirectory as myDirectory

extension = ".zip"


def triggerBombXTimes(x):
    for i in range(x):
        #I Extract files and open the directory
