import threading

class MyThreading(threading.Thread):
    def __init__(self,n):
        super(MyThreading,self).__init__()
        self.n = n

    def run(self):
        print("current task：", self.n)


if __name__ == "__main__":
    t1 = MyThreading("thread 1")
    t2 = MyThreading("thread 2")

    t1.start()
    t2.start()