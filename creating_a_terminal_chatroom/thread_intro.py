import threading

def function1():
    for i in range(10):
        print("One")

def function2():
    for i in range(10):
        print("TWO ")


def function3():
    for i in range(10):
        print("THREE ")

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t3 = threading.Thread(target=function3)

# t1.start()
# t2.start()
# t3.start()

#Threads can only be run once.  If you want to reuse, you must redfine.
t1 = threading.Thread(target=function1)
t1.start()

#If you want to 'pause' the main programin until a thread is done you can!
t1 = threading.Thread(target=function1)
t1.start()
t1.join() #This pauses the main program until the thread is complete
print("Threading rules!")