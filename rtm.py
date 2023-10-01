from tm import Transition, TripleTapeTuringMachine,\
                     MOVEMENT_STAY, MOVEMENT_RIGHT,\
                     MOVEMENT_LEFT, TYPE_WRITE, TYPE_MOVE,\
                     STATE_EFFECTIVE, STATE_INTERMEDIATE


class ReversibleTuringMachine:
    def __init__(self, tm:TripleTapeTuringMachine):
        self.tm = tm
        self.original_transitions = tm.transitions.copy()

    def add_history(self):
        for t in self.tm.transitions:  
            if t.type_ == STATE_EFFECTIVE:
                t.second_tape_write = t.next_state
            elif t.type_ == STATE_INTERMEDIATE:
                t.second_tape_move = MOVEMENT_RIGHT

    def add_copying(self):
        self.tm.final_state = '#'
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
        self.tm.add_transition(Transition(['_', '/', '/'], ['/', '/', '/'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'c3', 'r#'))
        
    def add_reversing(self):
        r_itr = 0
        self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_RIGHT, MOVEMENT_STAY, MOVEMENT_STAY], 'r#', 'r##', STATE_INTERMEDIATE))
        self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'], [MOVEMENT_STAY, MOVEMENT_LEFT, MOVEMENT_STAY], 'r##', 'r###', STATE_INTERMEDIATE))

        for transition in self.original_transitions[::-1]:
            if transition.type_ == STATE_INTERMEDIATE:
                # r0 -> reverse
                self.tm.add_transition(Transition(['/', transition.current_state, '/'],
                                                   ['/', '/', '/'], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'r###', f'r{r_itr}', STATE_INTERMEDIATE))

                # reverse movement in tape one
                self.tm.add_transition(Transition(['/', '/', '/'], ['/', '/', '/'],
                                                   [-transition.first_tape_move, MOVEMENT_STAY, MOVEMENT_STAY],
                                                     'r' + str(r_itr), 'r' + str(r_itr + 1), type_=STATE_INTERMEDIATE))
                
                # undo transition
                for effective in self.original_transitions:
                    if effective.next_state == transition.current_state:
                        self.tm.add_transition(Transition([effective.first_tape_write, effective.second_tape_write, '/'],
                                               [effective.first_tape_read, '_', '/'],
                                               [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], f'r{r_itr + 1}', f'r##', type_=STATE_EFFECTIVE))
                        
                        break
                
                r_itr += 2
        self.tm.add_transition(Transition(['/', '_', '/' ], ['/', '/', '/' ], [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], 'r###', 'final'))
        self.tm.set_final_state('final')


    def apply_conversion(self):
        self.add_history()
        self.add_copying()
        self.add_reversing()



    def run(self, print_tapes=False, print_transition=False):
        return self.tm.run(print_tapes, print_transition)
    