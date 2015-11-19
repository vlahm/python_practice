from Queue import Queue
from threading import *
from select import select
import sys
import thread
import tty, termios

def fart(q):
    while True:
       # fd = sys.stdin.fileno()
       # old_settings = termios.tcgetattr(fd)
       # try:
       i, o, e = select([sys.stdin], [], [], 4)
       #     tty.setraw(i)
       #     ch = sys.stdin.read(1)
       # finally:
       #     termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
       q.put(i)

def chili(q):
    while True:
        x = q.get()
        print 'you said' + sys.stdin.readline() 
        q.task_done()

q = Queue(maxsize=0)
thread1 = Thread(target=fart, args=(q,))
thread2 = Thread(target=chili, args=(q,))
thread1.start()
thread2.start()

#print 'go'
#i,o,e = select([sys.stdin], [], [], 5)
#print 'chilidog says' + sys.stdin.readline()


