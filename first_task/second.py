import argparse
import os
from pathlib import *
from zipfile import *

from exceptions import *


def unzip(archive: str, folder: str):
    """Extract archive in folder."""
    counter = 0
    FILES_COUNTER = 0
    DIRS_COUNTER = 0
    windows_path = Path(__file__)
    unzip_folder = windows_path.parents[0].joinpath(folder)
    archive_folder = windows_path.parents[0].joinpath(archive)
    if not unzip_folder.exists():
        unzip_folder.mkdir()
    try:
        read_archive = ZipFile(archive_folder, "r")
    except BadZipFile:
        raise ZIPError("Выбранный файл не является ZIP-архивом.")
    except FileNotFoundError:
        raise ArchiveNotFoundError("ZIP-архив не обнаружен.")
    count_archive = len(read_archive.infolist())
    for i in range(0, count_archive):
        file = read_archive.infolist()[i].filename
        if unzip_folder.joinpath(file).exists():
            pass
        else:
            read_archive.extract(file, path=unzip_folder)
    for root, dirs, files in os.walk(unzip_folder):
        DIRS_COUNTER += len(dirs)
        FILES_COUNTER += len(files)
    print(
        f"Архив успешно распакован. "
        f"Количество папок ---  {DIRS_COUNTER}. "
        f"Количество файлов --- {FILES_COUNTER}"
    )


parser = argparse.ArgumentParser(description="Extract archive to folder")
parser.add_argument("archive", type=str, help="Input name of archive")
parser.add_argument("folder", type=str, help="input name of folder")
args = parser.parse_args()
print(f"Идет распаковка архива {args.archive} в папку {args.folder}")
unzip(args.archive, args.folder)
