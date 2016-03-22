import numpy as np
import time

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

class level(object):
    
    def __init__(self):
        self.dicty = 'unwritten'
        player = ('55', '^')
        
    def update_dicty(self, pos, val):
        if val == 'first':
            keys = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
            keys2 = [str(i) for i in range(10,100,1)]
            keys.extend(keys2)
            starting_vals = np.repeat('   ', 100)
            self.dicty = dict(zip(keys, starting_vals))
            ordered = sorted(self.dicty.items())
            vals = list()
            for i in range(100):
                vals.append(ordered[i][1])
            arranged = list(chunks(vals, 10))
            self.print_frame(arranged)
        else:
            self.dicty[pos] = ' ' + val + ' '
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
        
    def write_to_board(self, user_input):
        if user_input == 'first':
            self.update_dicty('00', 'first')
        else:
            self.update_dicty('00', user_input)
        # self.row = np.repeat('   ', 10)
        # self.board = np.matrix([self.row, self.row, self.row, self.row, self.row,
            # self.row, self.row, self.row, self.row, self.row])
    
x = level()

def play(user_input = 'none'):
    if user_input == 'none':
        x.write_to_board('first')
        new = raw_input('> ')
        play(user_input = new)
    elif user_input == 'q':
        print 'Running away, eh?'
        time.sleep(1) 
        print 'Coward!'
        time.sleep(1)
        print 'I\'ll see you next time'
        time.sleep(1)
    else :
        x.write_to_board(user_input)
        new = raw_input('> ')
        play(user_input = new)

play()





