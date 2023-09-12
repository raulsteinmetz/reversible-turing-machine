# tape

STANDART_HEAD_INDEX = 20

TYPE_READ = 0
TYPE_WRITE = 1
TYPE_MOVE = 2

MOVEMENT_LEFT = -1
MOVEMENT_RIGHT = 1
MOVEMENT_STAY = 0

MAXIMUM_TAPE_SIZE = 100

class Tape:
    def __init__(self):
        self.content = ['_'] * MAXIMUM_TAPE_SIZE
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
class Transition:
    def __init__(self):
        self.first_tape_read = '_'
        self.second_tape_read = '_'
        self.third_tape_read = '_'

        self.first_tape_write = '_'
        self.second_tape_write = '_'
        self.third_tape_write = '_'

        self.first_tape_movent = MOVEMENT_STAY
        self.second_tape_movent = MOVEMENT_STAY
        self.third_tape_movent = MOVEMENT_STAY

        self.current_state = 0
        self.next_state = 0

    def __init__(self, reads, writes, movements, state, next_state):

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

        self.current_state = state
        self.next_state = next_state


class TripleTapeTuringMachine:
    def __init__(self, input_tape_string):
        # input tape
        self.tape_one = Tape()

        # history tape
        self.tape_two = Tape()

        # output tape
        self.tape_three = Tape()

        # transitions
        self.transitions = []

        # initial state
        self.initial_state = 0

        # final state
        self.final_state = 0

        # current state
        self.current_state = 0


    def set_input_tape(self, input_tape_string):
        self.tape_one.set_head_index(STANDART_HEAD_INDEX)
        for i in input_tape_string:
            self.tape_one.action(TYPE_WRITE, i)
            self.tape_one.action(TYPE_MOVE, MOVEMENT_RIGHT)
        self.tape_one.set_head_index(STANDART_HEAD_INDEX)

    def set_transitions(self, transitions):
        self.transitions = transitions

    def add_transition(self, transition):
        self.transitions.append(transition)
    
    def set_initial_state(self, state):
        self.initial_state = state
    
    def set_final_state(self, state):
        self.final_state = state


    def run(self):
        # yet to be implemented
        while(self.step()):
            if (self.current_state == self.final_state):
                return True
            
        return False
        

    def step(self):

        movement_transition = False

        # read tapes
        first_tape_read = self.tape_one.action(TYPE_READ, '/')
        second_tape_read = self.tape_two.action(TYPE_READ, '/')
        third_tape_read = self.tape_three.action(TYPE_READ, '/')

        # find transition
        transition = None
        for i in self.transitions:
            if (self.current_state == i.current_state and i.first_tape_read == '/' and i.second_tape_read == '/' and i.third_tape_read == '/'):
                transition = i
                movement_transition = True
                break
            elif(self.current_state == i.current_state and  i.first_tape_read == first_tape_read and i.second_tape_read == second_tape_read and i.third_tape_read == third_tape_read):
                transition = i
                break

        if(transition == None):
            return False

        if (movement_transition):
            # move tapes
            self.tape_one.action(TYPE_MOVE, transition.first_tape_movent)
            self.tape_two.action(TYPE_MOVE, transition.second_tape_movent)
            self.tape_three.action(TYPE_MOVE, transition.third_tape_movent)

        else:
            # write tapes
            self.tape_one.action(TYPE_WRITE, transition.first_tape_write)
            self.tape_two.action(TYPE_WRITE, transition.second_tape_write)
            self.tape_three.action(TYPE_WRITE, transition.third_tape_write)


        # find next state
        self.current_state = transition.next_state


        # tape one state
        q = f' q{self.current_state} '
        before_q = self.tape_one.content[:self.tape_one.head_index + 1]
        after_q = self.tape_one.content[self.tape_one.head_index + 1:]
        print(f'{before_q}({q}){after_q}', end='\n')

        return True
    
    def convert_to_reversible(self):
        pass
    
