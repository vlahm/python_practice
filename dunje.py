import numpy as np
import time
from copy import deepcopy

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


keys = range(100)
starting_vals = np.repeat('   ', 100)
base_dicty = dict(zip(keys, starting_vals))

class level(object):
    
    def __init__(self):
        self.player = [55, ' ^ ']
        self.dicty = dict(zip(keys, starting_vals))
        
    def update_dicty(self, pos, val):
        if val == 'first':
          #  keys = range(100)
          #  starting_vals = np.repeat('   ', 100)
          #  self.dicty = dict(zip(keys, starting_vals))
            self.dicty[self.player[0]] = ' ^ '
            print '3'#
            ordered = sorted(self.dicty.items())
            vals = list()
            for i in range(100):
                vals.append(ordered[i][1])
            arranged = list(chunks(vals, 10))
            self.print_frame(arranged)
        else:
            self.dicty = deepcopy(base_dicty)
            self.dicty[pos] = val
            ordered = sorted(self.dicty.items())
            vals = list()
            for i in range(100):
                vals.append(ordered[i][1])
            arranged = list(chunks(vals, 10))
            self.print_frame(arranged) 
    
    def print_frame(self, data):
        print ' ' + ''.join(np.repeat('---', 10))
        for i in range(10):
            x = ''.join(data[i])#.tolist()[0])#
            print '|' + x + '|'
        print ' ' + ''.join(np.repeat('---', 10))
        print '4'#
       
    def process_changes(self, user_input):
        if user_input == 'first':
            self.update_dicty(0, 'first')

        elif user_input == '\x1b[D':
            next_space = self.player[0] - 1
            if (next_space in [' o ', ' x ', ' 8 ', '{0}', ' | '] or self.player[1] in [' ^ ', ' v ', ' > ']) or self.player[0] % 10 == 0 or self.player[0] == 0:
                self.player[1] = ' < '
            else:
                self.player = [next_space, ' < ']
            self.update_dicty(self.player[0], self.player[1])

        elif user_input == '\x1b[A':
            next_space = self.player[0] - 10
            if (next_space in [' o ', ' x ', ' 8 ', '{0}', '---'] or self.player[1] in [' < ', ' v ', ' > ']) or self.player[0] < 10:
                self.player[1] = ' ^ '
            else:
                self.player = [next_space, ' ^ ']
            self.update_dicty(self.player[0], self.player[1])
   
        elif user_input == '\x1b[C':
            next_space = self.player[0] + 1
            if (next_space in [' o ', ' x ', ' 8 ', '{0}', ' | '] or self.player[1] in [' < ', ' v ', ' ^ ']) or self.player[0] % 10 == 9:
                self.player[1] = ' > '
            else:
                self.player = [next_space, ' > ']
            self.update_dicty(self.player[0], self.player[1])

        elif user_input == '\x1b[B':
            next_space = self.player[0] + 10
            if (next_space in [' o ', ' x ', ' 8 ', '{0}', '---'] or self.player[1] in [' < ', ' ^ ', ' > ']) or self.player[0] > 89:
                self.player[1] = ' v '
            else:
                self.player = [next_space, ' v ']
            self.update_dicty(self.player[0], self.player[1])
x = level()

def play(user_input = 'none'):
    if user_input == 'none':
        print '1'#
        x.process_changes('first')
        print '5'#
        new = _GetchUnix()
        play(user_input = new())
    elif user_input == 'qqq':
        print 'Running away, eh?'
        time.sleep(1) 
        print 'Coward!'
        time.sleep(1)
        print 'I\'ll see you next time'
        time.sleep(1)
    elif user_input in ['\x1b[A', '\x1b[B', '\x1b[C', '\x1b[D']: 
        print '6'#
        x.process_changes(user_input)
        new = _GetchUnix()
        play(user_input = new())
    else:
        print 'Arrows move, \'qqq\' quits'
        new = _GetchUnix()
        play(user_input = new())
        

play()






