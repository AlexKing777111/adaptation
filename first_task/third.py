import os
import re
from pathlib import *

rootdir = Path(__file__).parent
regexp = re.compile("(.*zip$)|(.*rar$)|(.*r01$)")

for root, dirs, files in os.walk(rootdir):
    for file in files:
        if regexp.match(file):
            print(file)
            print(
                f"В названии файла {file} "
                f'{file.split(".")[0].count("a")} букв a'
            )
            print(
                f"В названии файла {file} " f'{len(file.split(".")[0])} букв'
            )
