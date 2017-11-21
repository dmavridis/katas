from collections import defaultdict

class DFA(object):
    def __init__(self, states, start_state, accepted_states):
        self.states = set(states)
        self.start_state = 'START_STATE'
        self.end_state = 'END_STATE'
        self.transitions = dict()
        self.add_transition(self.start_state, start_state, '')
        for accepted_state in accepted_states:
            self.add_transition(accepted_state, self.end_state, '')

    def add_transition(self, from_, to, trans):
        self.transitions[(from_, to)] = trans
        
    def select_state(self):
        """Select the state with the smallest impact when reduced."""
        from_count = defaultdict(int)
        to_count = defaultdict(int)
        for from_, to in self.transitions:
            if from_ != to:
                from_count[from_] += 1
                to_count[to] += 1
        return min(self.states, key=lambda state: from_count[state] * to_count[state])
        
    def reduce_state(self, state):
        entering = dict()
        exiting = dict()
        loop = None
        for (from_, to), trans in list(self.transitions.items()):
            if from_ == to == state:
                loop = trans
            elif to == state:
                entering[from_] = trans
            elif from_ == state:
                exiting[to] = trans
            if state in (from_, to):
                del self.transitions[(from_, to)]
        loop_trans = '' if loop is None else '(?:{})*'.format(loop)
        for enter_state, enter_trans in entering.items():
            for exit_state, exit_trans in exiting.items():
                if (enter_state, exit_state) in self.transitions:
                    format_ = '(?:{}|{{}})'.format(self.transitions[(enter_state, exit_state)])
                else:
                    format_ = '{}'
                trans = '{}{}{}'.format(enter_trans, loop_trans, exit_trans)
                trans = format_.format(trans)
                self.add_transition(enter_state, exit_state, trans)
        self.states.remove(state)
    
    def reduce(self):
        while self.states:
            state = self.select_state()
            self.reduce_state(state)
        return '^{}$'.format(self.transitions[(self.start_state, self.end_state)])

def generate_regex(n):
    if n == 1:
        return '^(0|1)*$'
    dfa = DFA(range(n+1), n, {0})
    for i in range(n+1):
        dfa.add_transition(i, i * 2 % n, '0')
        dfa.add_transition(i, (i * 2 + 1) % n, '1')
    return dfa.reduce()
    

import re
n = 1

expr = generate_regex(n)
rgx = re.compile(expr)
fails = 0
for num in range(0,1001):
#    print('Testing for: '+str(num))
    if (rgx.match(bin(num)[2:]) is not None) == (num%n == 0):
        continue
    else:
        fails += 1
        print('test fails for ', num)
if fails == 0:
    print("Test passed for", n)