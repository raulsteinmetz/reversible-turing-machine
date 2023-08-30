# tape

STANDART_HEAD_INDEX = 20

TYPE_READ = 0
TYPE_WRITE = 1
TYPE_MOVE = 2

MOVEMENT_LEFT = -1
MOVEMENT_RIGHT = 1
MOVEMENT_STAY = 0

MAXIMUM_TAPE_SIZE = 1000

class tape:
    def __init__(self):
        self.content = ['b'] * MAXIMUM_TAPE_SIZE
        self.head_index = STANDART_HEAD_INDEX

    def action(self, type, complement):
        if type == TYPE_READ:
            return self.content[self.head_index]
        elif type == TYPE_WRITE:
            self.content[self.head_index] = complement
            return True
        elif type == TYPE_MOVE:
            self.head_index += complement
            return True
        else:
            raise Exception("Unknown action type")
        
    def set_head_index(self, index):
        self.head_index = index
    
    def get_head_index(self):
        return self.head_index
    

# triple tape turing machine
class transition:
    def __init__(self):
        self.first_tape_read = 'b'
        self.second_tape_read = 'b'
        self.third_tape_read = 'b'

        self.first_tape_write = 'b'
        self.second_tape_write = 'b'
        self.third_tape_write = 'b'

        self.first_tape_movent = MOVEMENT_STAY
        self.second_tape_movent = MOVEMENT_STAY
        self.third_tape_movent = MOVEMENT_STAY

    def __init__(self, reads, writes, movements):

        for i in range(3):
            if (movements[i] != MOVEMENT_STAY):
                if(reads[i] != '/' or writes[i] != '/'):
                    raise Exception("Invalid transition")

        self.first_tape_read = reads[0]
        self.second_tape_read = reads[1]
        self.third_tape_read = reads[2]

        self.first_tape_write = writes[0]
        self.second_tape_write = writes[1]
        self.third_tape_write = writes[2]

        self.first_tape_movent = movements[0]
        self.second_tape_movent = movements[1]
        self.third_tape_movent = movements[2]


class tripleTapeTuringMachine:
    def __init__(self, input_tape_string):
        # input tape
        self.tape_one = tape()

        # second tape
        self.tape_two = tape()

        # third tape
        self.tape_three = tape()

        # transitions
        self.transitions = []

        # states
        self.states = []

        # initial state
        self.initial_state_index = 0
        # final state
        self.final_state_index = 0


    def set_input_tape(self, input_tape_string):
        self.tape_one.set_head_index(200)
        for i in input_tape_string:
            self.tape_one.action(TYPE_WRITE, i)
            self.tape_one.action(TYPE_MOVE, MOVEMENT_RIGHT)
        self.tape_one.set_head_index(200)

    def set_transitions(self, transitions):
        self.transitions = transitions

    def add_transition(self, transition):
        self.transitions.append(transition)
    
    def set_states(self, states):
        self.states = states

    def add_state(self, state):
        self.states.append(state)

    def set_initial_state_index(self, state_index):
        self.initial_state_index = state_index
    
    def set_final_state_index(self, state_index):
        self.final_state_index = state_index


    def run(self):
        # yet to be implemented
        pass

    def step(self):
        # logic probably not working yet, thats just the general idea

        # read tapes
        first_tape_read = self.tape_one.action(TYPE_READ, None)
        second_tape_read = self.tape_two.action(TYPE_READ, None)
        third_tape_read = self.tape_three.action(TYPE_READ, None)

        # find transition
        transition = None
        for i in self.transitions:
            if(i.first_tape_read == first_tape_read and i.second_tape_read == second_tape_read and i.third_tape_read == third_tape_read):
                transition = i
                break

        if(transition == None):
            return False

        # write tapes
        self.tape_one.action(TYPE_WRITE, transition.first_tape_write)
        self.tape_two.action(TYPE_WRITE, transition.second_tape_write)
        self.tape_three.action(TYPE_WRITE, transition.third_tape_write)

        # move tapes
        self.tape_one.action(TYPE_MOVE, transition.first_tape_movent)
        self.tape_two.action(TYPE_MOVE, transition.second_tape_movent)
        self.tape_three.action(TYPE_MOVE, transition.third_tape_movent)

        return True