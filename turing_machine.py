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

        # second tape
        self.tape_two = Tape()

        # third tape
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
        # logic probably not working yet, thats just the general idea


        movement_transition = False

        # read tapes
        first_tape_read = self.tape_one.action(TYPE_READ, '/') # the error is here, the trainsition needs to be '/'
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
    




def main():
    tripleTapeTuringMachine = TripleTapeTuringMachine("aaaaaa#bbbbbb")
    tripleTapeTuringMachine.set_input_tape("aaaaaa#bbbbbb")
    tripleTapeTuringMachine.set_initial_state(0)
    tripleTapeTuringMachine.set_final_state(12)

    transition_1 = Transition(['a', '_', '_'], ['X', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 0, 1)
    transition_2 = Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_STAY], 1, 2)
    transition_3 = Transition(['a', '_', '_'], ['a', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 2, 1)
    transition_4 = Transition(['#', '_', '_'], ['#', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 2, 3)
    transition_5 = Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_STAY], 3, 4)
    transition_6 = Transition(['Y', '_', '_'], ['Y', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 4, 5)
    transition_7 = Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_STAY], 5, 4)
    transition_8 = Transition(['b', '_', '_'], ['Y', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 4, 6)
    transition_9 = Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_LEFT, MOVEMENT_STAY, MOVEMENT_STAY], 6, 7)
    transition_10 = Transition(['a', '_', '_'], ['a', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 7, 6)
    transition_11 = Transition(['Y', '_', '_'], ['Y', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 7, 6)
    transition_12 = Transition(['#', '_', '_'], ['#', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 7, 6)
    transition_13 = Transition(['X', '_', '_'], ['X', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 7, 8)
    transition_14 = Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_STAY], 8, 0)
    transition_15 = Transition(['X', '_', '_'], ['X', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 0, 9)
    transition_16 = Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_STAY], 9, 0)
    transition_17 = Transition(['#', '_', '_'], ['#', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 0, 10)
    transition_18 = Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_STAY], 10, 11)
    transition_19 = Transition(['Y', '_', '_'], ['Y', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 11, 10)
    transition_20 = Transition(['_', '_', '_'], ['_', '_', '_'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 11, 12)

    tripleTapeTuringMachine.add_transition(transition_1)
    tripleTapeTuringMachine.add_transition(transition_2)
    tripleTapeTuringMachine.add_transition(transition_3)
    tripleTapeTuringMachine.add_transition(transition_4)
    tripleTapeTuringMachine.add_transition(transition_5)
    tripleTapeTuringMachine.add_transition(transition_6)
    tripleTapeTuringMachine.add_transition(transition_7)
    tripleTapeTuringMachine.add_transition(transition_8)
    tripleTapeTuringMachine.add_transition(transition_9)
    tripleTapeTuringMachine.add_transition(transition_10)
    tripleTapeTuringMachine.add_transition(transition_11)
    tripleTapeTuringMachine.add_transition(transition_12)
    tripleTapeTuringMachine.add_transition(transition_13)
    tripleTapeTuringMachine.add_transition(transition_14)
    tripleTapeTuringMachine.add_transition(transition_15)
    tripleTapeTuringMachine.add_transition(transition_16)
    tripleTapeTuringMachine.add_transition(transition_17)
    tripleTapeTuringMachine.add_transition(transition_18)
    tripleTapeTuringMachine.add_transition(transition_19)
    tripleTapeTuringMachine.add_transition(transition_20)
    

    if(tripleTapeTuringMachine.run()):
        print("Accepted")
    else:
        print("Rejected")





if __name__ == '__main__':
    main()
