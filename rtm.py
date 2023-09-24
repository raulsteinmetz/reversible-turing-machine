from tm import Transition, TripleTapeTuringMachine,\
                     MOVEMENT_STAY, MOVEMENT_RIGHT,\
                     MOVEMENT_LEFT, TYPE_WRITE, TYPE_MOVE,\
                     STATE_EFFECTIVE, STATE_INTERMEDIATE


class ReversibleTuringMachine:
    def __init__(self, tm:TripleTapeTuringMachine):
        self.tm = tm

    def add_history(self):
        for t in self.tm.transitions:  
            if t.type_ == STATE_EFFECTIVE:
                t.second_tape_write = t.next_state
            elif t.type_ == STATE_INTERMEDIATE:
                t.second_tape_move = MOVEMENT_RIGHT

    def add_copying(self):
        self.tm.final_state = 'r0'
        self.tm.transitions[-1].next_state = 'c#'
        self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_LEFT, MOVEMENT_STAY, MOVEMENT_STAY], 'c#', 'c##', type_=STATE_INTERMEDIATE))
        self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_LEFT, MOVEMENT_STAY, MOVEMENT_STAY], 'c##', 'c0'))
        for alpha in self.tm.alphabet:
            self.tm.add_transition(Transition([alpha, '/', '/'], ['/', '/', '/'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'c0', 'c1'))
        self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_LEFT, MOVEMENT_STAY, MOVEMENT_STAY], 'c1', 'c0', type_=STATE_INTERMEDIATE))
        self.tm.add_transition(Transition(['_', '/', '/'], ['/', '/', '/'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'c0', 'c2'))
        self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_STAY], 'c2', 'c3', type_=STATE_INTERMEDIATE))
        for alpha in self.tm.alphabet:
            self.tm.add_transition(Transition([alpha, '/', '/'], ['/', '/', alpha], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'c3', 'c4'))
        self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_RIGHT], 'c4', 'c3', type_=STATE_INTERMEDIATE))
        self.tm.add_transition(Transition(['_', '/', '/'], ['/', '/', '/'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'c3', 'r0'))
        

        pass


    def apply_conversion(self):
        self.add_history()
        self.add_copying()


    def run(self, print_tapes=False, print_transition=False):
        return self.tm.run(print_tapes, print_transition)