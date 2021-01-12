from datetime import datetime

def write_log_file(device, mess, type_mess):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %d-%m-%Y")
    file_log = open("logs/{}.log".format(device), "a+")
    line = "{0}\t{1}\t{2}\n".format(current_time, mess, type_mess)
    file_log.write(line)

def read_log_file(device):
    file_log = open("logs/{}.log".format(device), "r")

# write_log_file("a", "Read file success !", 1)