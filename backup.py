import os
import datetime
import shutil
def backup_files(source, destination):
    date= datetime.date.today()

    backup_files= os.path.join(destination, f"backup_{date}.tar.gz")
    shutil.make_archive(backup_files.replace('.tar.gz', ''), 'gztar', source)

source="/mnt/c/Users/priya/Desktop/python zero to hero"
destination="/mnt/c/Users/priya/Desktop/python zero to hero/backups"

backup_files(source,destination)