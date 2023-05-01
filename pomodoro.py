import os
import time
import subprocess


app_name = "CoModoro"


format_time = lambda x: f"0{x}" if x < 10 else f"{x}" 
clr = lambda: os.system('cls' if os.name == 'nt' else 'clear')
send_notif = lambda msg: subprocess.Popen(['notify-send', f"{app_name}\n{msg}"])


def format_second(s:float):
    s2m = s/60
    m = int(s2m)
    s = (s2m-m)*60
    return f"{format_time(m)}:{format_time(int(s))}"

def countdown(t, typ:str):
    while t > 0:
        print(f" [+] {typ} time left {format_second(t)}", end="\r")
        time.sleep(1)
        t-=1
    print("")


try:
    clr()
    while True:
        for i in range(1, 5):
            print(f" ---- [{i}/4] ----")

            productive_time = 25*60
            send_notif(f"Productive time {format_second(productive_time)}")
            countdown(productive_time, "Productive")

            break_time = 5*60
            send_notif(f"Break time {format_second(break_time)}")
            countdown(break_time, "Break")
            clr()

        print(" [+] ctrl+c for exit -,-'")
        done_msg = "Yeay 4 section was passed"
        reward_time = 25*60
        print(f" [+] {done_msg}")
        send_notif(f"{done_msg} reward time {format_second(reward_time)}")
        countdown(reward_time, "Reward")
except KeyboardInterrupt:
    clr()
    print(" ---- See you onii chan ^^ ----")
