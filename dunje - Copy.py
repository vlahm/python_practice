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

rows = range(10)
cols = range(10)
tups = zip(np.repeat(rows,10),cols*10)
catalog = zip(tups,np.repeat('   ',100))

class level(object):
    def populate(self,catalog):
        coords = [catalog[x][0] for x in range(100)]
        entities = [catalog[x][1] for x in range(100)]

        available_spaces = []
        for i in range(len(vals)):
            if vals[i] == '   ':
                available_spaces.append(keys[i])
        self.coords = np.random.choice(available_spaces, size=random.randrange(3,7), replace=False)
        self.icons = np.repeat(' ~ ', len(self.coords))
        self.updates = zip(self.coords, self.icons)
        global_updates.append(self.updates)







keys = range(100)
starting_vals = np.repeat('   ', 100)
base_dicty = dict(zip(keys, starting_vals))
global_updates = []

class level(object):
    
    def __init__(self):
        self.player = [55, ' ^ ']
        self.dicty = dict(zip(keys, starting_vals))
        
    def update_dicty(self, pos, val, other_updates=global_updates):
        if val == 'first':
          #  keys = range(100)
          #  starting_vals = np.repeat('   ', 100)
          #  self.dicty = dict(zip(keys, starting_vals))
            self.dicty[self.player[0]] = ' ^ '
            print '3'#
            for i in range(len(other_updates[0])):
                self.dicty[other_updates[0][i][0]] = other_updates[0][i][1]
            ordered = sorted(self.dicty.items())
            vals = list()
            for i in range(100):
                vals.append(ordered[i][1])
            arranged = list(chunks(vals, 10))
            self.print_frame(arranged)
        else:
            self.dicty = deepcopy(base_dicty)
            self.dicty[pos] = val
            for i in range(len(other_updates[0])):
                self.dicty[other_updates[0][i][0]] = other_updates[0][i][1]
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

class cobra(object):
    
    def __init__(self, level):
        self.hit_points = random.randrange(9,12)
        self.damage = range(1,3)
        self.item_class = 1
        
    def populate(self, level):
        vals = level.dicty.values()
        keys = level.dicty.keys()
        available_spaces = []
        for i in range(len(vals)):
            if vals[i] == '   ':
                available_spaces.append(keys[i])
        self.coords = np.random.choice(available_spaces, size=random.randrange(3,7), replace=False)
        self.icons = np.repeat(' ~ ', len(self.coords))
        self.updates = zip(self.coords, self.icons)
        global_updates.append(self.updates)
        
test = cobra(x)
test.populate(x)

def play(user_input):
    if user_input == 'setup':
        x.process_changes('first')
    elif user_input == 'start':
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
        x.process_changes(user_input)
        new = _GetchUnix()
        play(user_input = new())
    else:
        print 'Arrows move, \'qqq\' quits'
        new = _GetchUnix()
        play(user_input = new())
        

play('setup')
play('start')






