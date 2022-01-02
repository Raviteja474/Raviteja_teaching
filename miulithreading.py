import threading
import time

def dining_help(name):
    print(f"serving idly to {name}\n")
    time.sleep(1)
    print(f"serving Dosa to {name}\n")
    time.sleep(1)
    print(f"serving pongal to {name}\n")
    time.sleep(1)
    print(f"serving sambar to {name}\n")
    time.sleep(1)
    print(f"serving tea to {name}\n")
    time.sleep(1)
    print(f"serving coffee to {name}\n")
    time.sleep(1)

start_time =time.time()

thread_1 = threading.Thread(target=dining_help,args=("ravi",))
thread_2 = threading.Thread(target=dining_help,args=("avi",))
thread_3 = threading.Thread(target=dining_help,args=("Bharath",))
thread_4 = threading.Thread(target=dining_help,args=("Mahi",))
thread_5 = threading.Thread(target=dining_help,args=("visu",))
thread_6 = threading.Thread(target=dining_help,args=("sumanth",))

thread_1.start()
time.sleep(1)
thread_2.start()
time.sleep(1)
thread_3.start()
time.sleep(1)
thread_4.start()
time.sleep(1)
thread_5.start()
time.sleep(1)
thread_6.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()
thread_6.join()

end_time =time.time()
print(f"Program ran for {end_time-start_time}")