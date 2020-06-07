import numpy as np
import time
from copy import deepcopy
import random

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

catalog = [np.transpose(np.array([np.repeat(range(10), 10), range(10) * 10, np.repeat('   ', 100)])),
           self_loc = 0]

class level(object):
    def check_available(self):
        available_spaces = []
        for i in range(100):
            if catalog[i,2] == '   ':
                available_spaces.append(catalog[i,0:2].tolist())
        return np.array(available_spaces)
      
    def populate(self):
        catalog[99][2] = ' ^ '
        catalog[00][2] = ' @ '
        avail = self.check_available()
        asp_idx = np.random.choice(len(avail), 
            size=random.randrange(3,7), replace=False)
        catalog[asp_idx,2] = ' ~ '

    def print_frame(self):
        print ' ' + ''.join(np.repeat('---', 10))
        lines = list(chunks(catalog[:,2], 10))
        for i in range(10):
            x = ''.join(lines[i])
            print '|' + x + '|'
        print ' ' + ''.join(np.repeat('---', 10))
 
#class player(object):
#    def move(self, usr_input):
#        
#        if usr_input == '\x1b[D':
            
        


x = level()
x.populate()
x.print_frame()
        
        

