from datetime import datetime
import time
import os

cwd = os.getcwd()
file_name = "hello_time_file.txt"

file_path = os.path.join(cwd, file_name)  # Replace with your file name

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully!")
else:
    print("The file does not exist.")


while True:
    now = datetime.now()
    hello_file = open(file_name, "a")
    hello_file.write(now.strftime("%d_%m_%Y-%H:%M:%S\n"))
    time.sleep(2)