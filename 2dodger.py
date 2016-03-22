from random import randint
import thread, sys, select, time
from threading import *
from Queue import Queue

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

#getch = _GetchUnix()
#print getch()
def obstacle_generator():
    line0 = list('___________')
    obstacle = randint(0,10)
    for i in range(11):
        if i == obstacle:
            line0[i] = '0'
        else:
            continue
    line0 = "".join(line0)
    return line0


def initializer():
    line0 = obstacle_generator()

    line9 = '___________'
    line8 = '___________'
    line7 = '_____V_____'
    line6 = '___________'
    line5 = '___________'
    line4 = '___________'
    line3 = '___________'
    line2 = '___________'
    line1 = '___________'
        
    state0 = [line9, line8, line7, line6, line5, line4, line3, line2, line1, line0]
    
#    for i in range(len(state0)):
#        print state0[i]

    return state0

    
def commencer():
    lines = initializer()
#    for i in range(10):
    while True:
 #       if i == 6:
  #          break
        time.sleep(0.3)
        lines[0] = lines[1] #line9 = line8

        temp7 = list(lines[2])
        for i in range(len(temp7)):
            if temp7[i] == '_' or temp7[i] == '0':
                pass
            else:
                temp7[i] = '_'
        lines[1] = "".join(temp7) #line8 = modified line7

        temp6 = list(lines[3])
        temp7b = list(lines[2])
#        if q.empty == True:
#            temp7b = temp6
#        else: 
#            direction = q.get()
#            print 'chili' + direction
#            V_pos = temp7b.index('V')
#            print 'vpos = %r' % V_pos
#            temp7b = temp6
#            if V_pos > 0 and direction == '7':
 #               print 'read 7'
#                temp7b[V_pos-1] = 'V'
#            elif V_pos < 11 and direction == '8':
#                temp7b[V_pos+1] = 'V'
#            else:
#                temp7b[V_pos] = 'V'
#            V_pos = 0
      #  for i in range(len(temp7)):
      #      if temp7[i] == 'V':
      #          pass
      #      else:
      #         temp7[i] = temp6[i]
        lines[2] = "".join(temp7b) #line7 = testing stage

        lines[3] = lines[4]
        lines[4] = lines[5]
        lines[5] = lines[6]
        lines[6] = lines[7]
        lines[7] = lines[8]
        lines[8] = lines[9]
        lines[9] = obstacle_generator() 

        next_state = lines
        for i in next_state:
            print i

#x = _GetchUnix()
#def movement(q):
#    while True:
#        x = _GetchUnix()
#        q.put(x())

#        if x:
#            q.put(x())
#        else:
#            continue
#        x = None
 #       time.sleep(1)
#        print "here's %s " % q.get()
#        direction, null1, null2 = select.select([sys.stdin], [], [], 0.2)
 #       q.put(direction)

#while True:
#direction <- 'd'
#    direction <- raw_input()

commencer()
#q = Queue(maxsize=0)
#move_V = Thread(target=movement, args=(q,))
#iterate_field = Thread(target=commencer, args=(q,))
#move_V.setDaemon(True)
##iterate_field.setDaemon(True)
#move_V.start()
#iterate_field.start()
