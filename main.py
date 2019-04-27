import time
from datetime import datetime, timedelta
# from threading import Timer # will probz remove
from bullet import Bullet, Input

class ProductivityTimer:
    def __init__(self):
        self.running = True

    def show_menu(self):
        cli = Bullet(prompt="What would you like to do?", 
                     choices=["Do task", "View log", "Exit"], 
                     bullet="🔥")
        choice = cli.launch()

        if choice is "Do task":
            self.do_task()
        elif choice is "View log":
            self.read_logs()
        elif choice is "Exit":
            self.running = False
        # print(running)

    def do_task(self):
        cli = Input(prompt="What task? 📝 >", strip=False)
        task = cli.launch()

        cli = Input(prompt="How long? ⏰ >", strip=False)

        # Set timer
        duration = int(cli.launch())

        try:
            print("Press CTRL+C to cancel timer and log time.")
            time.sleep(duration)
            self.alert_finished(task, duration)
        except KeyboardInterrupt:
            print("\nTimer cancelled and time logged!")
            # TODO: duration passed should time executed before cancelled
            self.alert_finished(task, duration)
        

    def alert_finished(self, task, duration):
        print(f"Good job!! You did {task} for {duration} mins.")
        self.log_task(task, duration)

    def log_task(self, task, duration):
        now = datetime.now()
        time_started = datetime.now() - timedelta(minutes=duration)
        time_started_formatted = time_started.strftime("%Y-%m-%d %H:%M")
        f = open("task_log.txt", "a")
        f.write(f"{time_started_formatted} Did {task} for {duration} mins.\n")
        f.close()

    def read_logs(self):
        try:
            f = open("task_log.txt", "r")
            print(f.read())
        except:
            print("You don't have any logged tasks yet!")
            

app = ProductivityTimer()

while(app.running):
    app.show_menu()