from random import randint
import thread, sys, select, time
from threading import *
from Queue import Queue

#def dodger():
#    x = '|__________|'
#    for i in range(1,10):
#        print x
#
#dodger()
#
#
#def dodger():
#    line9 = '|__________|'
#    line8 = '|__________|'
#    line7 = '|__________|'
#    line6 = '|__________|'
#    line5 = '|__________|'
#    line4 = '|__________|'
#    line3 = '|__________|'
#    line2 = '|__________|'
#    line1 = '|__________|'
#    line0 = '|__________|'
#
#def firstline():
#    space0 = '_'
#    space1 = '_'
#    space2 = '_'
#    space3 = '_'
#    space4 = '_'
#    space5 = '_'
#    space6 = '_'
#    space7 = '_'
#    space8 = '_'
#    space9 = '_'
#
#    obstacle = randint(0,9)
#    = 'space%s' %obstacle
#
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
    
    for i in range(len(state0)):
        print state0[i]

    return state0
    
#def raw_input_with_timeout(timeout=0.1):
#    timer = threading.Timer(timeout, thread.interrupt_main)
#    astring = None
#    try:
#        timer.start()
#        astring = raw_input()
#    except KeyboardInterrupt:
#        pass
#    timer.cancel()
#    return astring

def commencer(q):
    lines = initializer()
    while True:
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
        direction = q.get()
        V_pos = temp7b.index('V')
        temp7b = temp6
        if V_pos > 0 and direction == 7:
            temp7b[V_pos-1] = 'V'
        elif V_pos < 11 and direction == 8:
            temp7b[V_pos+1] = 'V'
        else:
            temp7b[V_pos] = 'V'
        V_pos = 0
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

#        for i in state0:
#            print i
#            if i == 'line9':
#                line9 = line8
#            elif i == 'line8':
#                temp7 = list(line7)
#                for i in temp7:
#                    if i == '_' or i == '0':
#                        pass
#                    else:
#                        temp7[i] = '_'
#                line8 = "".join(temp7)
#            elif i == 'line7':
#    #            temp7 = list(line7)
#    #            for i in temp7:
#    #                if direction[-1] = 'j'
#                temp6 = list(line6)
#                temp7 = list(line7)
#                for i in temp7:
#                    if i == 'V':
#                        pass
#                    else:
#                       temp7[i] = temp6[i]
#                line7 = "".join(temp7)
#            elif i == 'line6':
#                line6 = line5
#            elif i == 'line5':
#                line5 = line4
#            elif i == 'line4':
#                line4 = line3
#            elif i == 'line3':
#                line3 = line2 
#            elif i == 'line2':
#                line2 = line1 
#            elif i == 'line1':
#                line1 = line0
#            else:
#                pass
#                
#        nextstate = [line9, line8, line7, line6, line5, line4, line3, line2, line1, line0]
#    
#        for i in range(len(nextstate)):
#            print nextstate[i]
#
#initializer()

def movement(q):
    while True:
        direction, null1, null2 = select.select([sys.stdin], [], [], 0.2)
        q.put(direction)
#while True:
#direction <- 'd'
#    direction <- raw_input()

q = Queue(maxsize=0)
move_V = Thread(target=movement, args=(q,))
iterate_field = Thread(target=commencer, args=(q,))
move_V.setDaemon(True)
#iterate_field.setDaemon(True)
move_V.start()
iterate_field.start()
