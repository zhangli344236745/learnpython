import threading

def run(n):
    print("current tasks:",n)

if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=("threading1",))
    t2 = threading.Thread(target=run,args=("threading2",))
    t1.start()
    t2.start()