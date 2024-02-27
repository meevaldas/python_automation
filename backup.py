import os
import shutil
import schedule
import datetime

source_dir = "/home/ariel/Pictures/books"
destination_dir ="/home/ariel/Videos/Backups"


def copy_folder_to_directory(source, destination):
    today = datetime.date.today()
    dest_dir = os.path.join(destination, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to the {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in the {dest_dir}")


copy_folder_to_directory(source_dir, destination_dir)