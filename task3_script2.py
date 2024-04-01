"""
for compelete exiting write number after 20 second beacuse the 
input function still running!!!!
"""
import random
import threading as th
import time
T = 0
F = 0
e = 0
def dTob(dec): 
    binary = format(dec,'04b')
    return binary
def exam_numbers():
    while True:
        global T 
        global F
        exam = random.randint(0,15)
        print(format(exam,'04b'))
        write = int(input("write dec:"))
        if(write == exam):
            if(e == 0):
                T += 1
        else:
            if(e == 0):
                F += 1
        if(e == 1):
            break
def exiting():
    global e
    time.sleep(20)
    print("current answer: ",T)
    print("uncurrent answer: ",F)
    e = 1
    
thread1 = th.Thread(target=exiting) #make a thread object for exit without interrupt
thread1.start()
exam_numbers()
out_Task3_S2 = T
