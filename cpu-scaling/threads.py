import threading

def print_smth(smth):
    print(smth)

t = threading.Thread(target=print_smth, args=("Hello",))
t.daemon = True
t.start()

print("thread started")