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
        self.tm.final_state = 'r10'
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
        
    def add_reversing(self):
        # go left
        self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_STAY, MOVEMENT_LEFT, MOVEMENT_STAY], 'r0', 'r1', type_=STATE_INTERMEDIATE))
        r_idx = 1
        old_t = self.tm.transitions.copy()
        for ti in old_t:
            if ti.type_ == STATE_INTERMEDIATE and 'c' not in ti.current_state and 'r' not in ti.current_state:
                # find out the effective state that leads to it
                te = None
                for te_ in self.tm.transitions:
                    if te_.next_state == ti.current_state:
                        te = te_
                        break
                if te is None:
                    raise Exception("Invalid transition")
                
                self.tm.add_transition(Transition(['/', ti.current_state, '/'], ['/', '_', '/'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'r1', 'r' + str(r_idx + 1)))

                # reversion + erase history
                read1 = te.first_tape_write
                write1 = te.first_tape_read
                move = MOVEMENT_LEFT
                if (ti.first_tape_move == MOVEMENT_LEFT):
                    move = MOVEMENT_RIGHT

                self.tm.add_transition(Transition([read1, '/', '/'], [write1, '/', '/'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'r' + str(r_idx + 1), 'r' + str(r_idx + 2), type_=STATE_EFFECTIVE))
                self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [move, MOVEMENT_LEFT, MOVEMENT_STAY], 'r' + str(r_idx + 2), 'r1', type_=STATE_INTERMEDIATE))


                r_idx += 3

        self.tm.add_transition(Transition(['/', '_', '/'], ['/', '/', '/'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'r1', 'f'))
        self.tm.final_state = 'f'


    def apply_conversion(self):
        self.add_history()
        self.add_copying()
        self.add_reversing()


    def run(self, print_tapes=False, print_transition=False):
        return self.tm.run(print_tapes, print_transition)