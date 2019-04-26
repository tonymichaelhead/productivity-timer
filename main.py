# import time
from threading import Timer
from bullet import Input

def alert_finished():
    print(f"Good job!! You did {task} for {time} mins.")
    log_task(task, time)

def log_task(task, time):
    f = open("task_log.txt", "w")
    f.write(f"Did {task} for {time} mins.")
    f.close()

cli = Input(prompt="What task? 📝 >", strip=False)
task = cli.launch()

cli = Input(prompt="How long? ⏰ >", strip=False)

# Set timer
time = int(cli.launch())

timer = Timer(time, alert_finished)
timer.start()