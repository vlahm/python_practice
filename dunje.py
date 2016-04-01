import numpy as np
import time
from copy import deepcopy

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

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
                self.player = ' ^ '
            else:
                self.player = [next_space, ' ^ ']
            self.update_dicty(self.player[0], self.player[1])
   
#current issue: cant go sideways then up, doesn't recognize ceiling 
x = level()

def play(user_input = 'none'):
    if user_input == 'none':
        print '1'#
        x.process_changes('first')
        print '5'#
        new = raw_input('> ')
        play(user_input = new)
    elif user_input == 'q':
        print 'Running away, eh?'
        time.sleep(1) 
        print 'Coward!'
        time.sleep(1)
        print 'I\'ll see you next time'
        time.sleep(1)
    else:
        print '6'#
        x.process_changes(user_input)
        new = raw_input('> ')
        play(user_input = new)

play()






