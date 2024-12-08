import os

# print(os.system('df -h'))
# print(os.system('free -h'))
# print(os.system('du -h'))
# print(os.system('top'))
# print(os.system('uptime'))

def check_disk_file(command):
    print(os.system(command))


def check_disk_util(command):
    print(os.system(command))


def check_ram(command):
    print(os.system(command))


def check_process(command):
    print(os.system(command))


def check_uptime(command):
    print(os.system(command))


# check_disk_file('df -h')
# check_disk_util('du -h')
# check_ram('free -h')
# check_process('top')
check_uptime('uptime')
