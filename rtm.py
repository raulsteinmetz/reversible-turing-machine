from tm import TripleTapeTuringMachine, MOVEMENT_STAY, MOVEMENT_RIGHT,\
                     MOVEMENT_LEFT, TYPE_WRITE, TYPE_MOVE, STATE_EFFECTIVE, STATE_INTERMEDIATE


class ReversibleTuringMachine:
    def __init__(self, tm:TripleTapeTuringMachine):
        self.tm = tm

    def add_history(self):
        for t in self.tm.transitions:  
            if t.type_ == STATE_EFFECTIVE:
                t.second_tape_write = str(t.next_state)
            elif t.type_ == STATE_INTERMEDIATE:
                t.second_tape_move = MOVEMENT_RIGHT

    def add_copying(self):
        # last transition should have as next state the first state of the copying machine
        # after that, just adding the coppying transictions should be enough
        pass

    def run(self, print_tapes=False, print_transition=False):
        return self.tm.run(print_tapes, print_transition)