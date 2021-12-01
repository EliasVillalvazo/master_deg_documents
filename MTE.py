from automata.tm.dtm import DTM

# Problem 1
dtm = DTM(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'1'},
    tape_symbols={'1', '.'},
    transitions={
        'q0': {
            '.': ('q1', '.', 'R'),
        },
        'q1': {
            '1': ('q1', '1', 'R'),
            '.': ('q2', '1', 'L')
        },
        'q2': {
            '1': ('q2', '1', 'L'),
            '.': ('q3', '.', 'R')
        },
    },
    initial_state='q0',
    blank_symbol='.',
    final_states={'q3'}
)
print("Problem 1: Successor function")
my_input_str = '.1111.'
print("Input: " + my_input_str)
dtm.read_input(my_input_str)  # returns TMConfiguration('q4', TMTape('xy..', 3))
dtm.read_input(my_input_str).print()

if dtm.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# Problem 2
dtm = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'1'},
    tape_symbols={'1', '.'},
    transitions={
        'q0': {
            '.': ('q1', '.', 'R'),
        },
        'q1': {
            '1': ('q2', '1', 'R'),
        },
        'q2': {
            '1': ('q2', '.', 'R'),
            '.': ('q3', '.', 'L')
        },
        'q3': {
            '.': ('q3', '.', 'L'),
            '1': ('q4', '1', 'L')
        }
    },
    initial_state='q0',
    blank_symbol='.',
    final_states={'q4'}
)
print("Problem 2: Zero Function")
my_input_str = '.1111.'
print("Input: " + my_input_str)
dtm.read_input(my_input_str)  # returns TMConfiguration('q4', TMTape('xy..', 3))
dtm.read_input(my_input_str).print()
# dtm.read_input('011')  # raises RejectionException
# dtm.read_input_stepwise('01')

if dtm.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# Problem 3
dtm = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    input_symbols={'1'},
    tape_symbols={'1', '.'},
    transitions={
        'q0': {
            '.': ('q1', '.', 'R'),
        },
        'q1': {
            '1': ('q1', '1', 'R'),
            '.': ('q2', '1', 'R')
        },
        'q2': {
            '1': ('q2', '1', 'R'),
            '.': ('q3', '.', 'L')
        },
        'q3': {
            '1': ('q4', '.', 'L')
        },
        'q4': {
            '1': ('q5', '.', 'L')
        },
        'q5': {
            '1': ('q5', '1', 'L'),
            '.': ('q6', '.', 'R')
        }
    },
    initial_state='q0',
    blank_symbol='.',
    final_states={'q6'}
)
print("Problem 3: Sum of two natural numbers")
my_input_str = '.1111.11111.'  # 3 + 4
print("Input: " + my_input_str)
dtm.read_input(my_input_str)  # returns TMConfiguration('q4', TMTape('xy..', 3))
dtm.read_input(my_input_str).print()
# dtm.read_input('011')  # raises RejectionException
# dtm.read_input_stepwise('01')

if dtm.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# Problem 4
dtm = DTM(
    states={'q1.0', 'q1.1', 'q1.2', 'q1.3', 'q1.4', 'q2.1', 'q2.2', 'q2.3'},
    input_symbols={'1'},
    tape_symbols={'1', '.'},
    transitions={
        'q1.0': {
            '.': ('q1.1', '.', 'R'),
        },
        'q1.1': {
            '1': ('q1.2', '1', 'R'),
        },
        'q1.2': {
            '1': ('q1.2', '.', 'R'),
            '.': ('q1.3', '.', 'L')
        },
        'q1.3': {
            '.': ('q1.3', '.', 'L'),
            '1': ('q1.4', '1', 'L')
        },
        'q1.4': {
            '.': ('q2.1', '.', 'R'),
        },
        'q2.1': {
            '1': ('q2.1', '1', 'R'),
            '.': ('q2.2', '1', 'L')
        },
        'q2.2': {
            '1': ('q2.2', '1', 'L'),
            '.': ('q2.3', '.', 'R')
        },
    },
    initial_state='q1.0',
    blank_symbol='.',
    final_states={'q2.3'}
)
print("Problem 4: Constant 1 Function")
my_input_str = '.11111111.'
print("Input: " + my_input_str)
dtm.read_input(my_input_str)  # returns TMConfiguration('q4', TMTape('xy..', 3))
dtm.read_input(my_input_str).print()
# dtm.read_input('011')  # raises RejectionException
# dtm.read_input_stepwise('01')