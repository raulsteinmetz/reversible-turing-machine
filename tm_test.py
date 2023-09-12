import tm as tm
from tm_54_converter import parse_tm

def test1():
    tripleTapeTuringMachine = tm.TripleTapeTuringMachine("aaaaaa#bbbbbb")
    tripleTapeTuringMachine.set_input_tape("aaaaaa#bbbbbb")
    tripleTapeTuringMachine.set_initial_state(0)
    tripleTapeTuringMachine.set_final_state(12)

    transition_1 = tm.Transition(['a', '_', '_'], ['X', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 0, 1)
    transition_2 = tm.Transition(['/', '/', '/'], ['/', '/', '/'], [tm.MOVEMENT_RIGHT, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 1, 2)
    transition_3 = tm.Transition(['a', '_', '_'], ['a', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 2, 1)
    transition_4 = tm.Transition(['#', '_', '_'], ['#', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 2, 3)
    transition_5 = tm.Transition(['/', '/', '/'], ['/', '/', '/'], [tm.MOVEMENT_RIGHT, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 3, 4)
    transition_6 = tm.Transition(['Y', '_', '_'], ['Y', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 4, 5)
    transition_7 = tm.Transition(['/', '/', '/'], ['/', '/', '/'], [tm.MOVEMENT_RIGHT, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 5, 4)
    transition_8 = tm.Transition(['b', '_', '_'], ['Y', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 4, 6)
    transition_9 = tm.Transition(['/', '/', '/'], ['/', '/', '/'], [tm.MOVEMENT_LEFT, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 6, 7)
    transition_10 = tm.Transition(['a', '_', '_'], ['a', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 7, 6)
    transition_11 = tm.Transition(['Y', '_', '_'], ['Y', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 7, 6)
    transition_12 = tm.Transition(['#', '_', '_'], ['#', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 7, 6)
    transition_13 = tm.Transition(['X', '_', '_'], ['X', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 7, 8)
    transition_14 = tm.Transition(['/', '/', '/'], ['/', '/', '/'], [tm.MOVEMENT_RIGHT, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 8, 0)
    transition_15 = tm.Transition(['X', '_', '_'], ['X', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 0, 9)
    transition_16 = tm.Transition(['/', '/', '/'], ['/', '/', '/'], [tm.MOVEMENT_RIGHT, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 9, 0)
    transition_17 = tm.Transition(['#', '_', '_'], ['#', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 0, 10)
    transition_18 = tm.Transition(['/', '/', '/'], ['/', '/', '/'], [tm.MOVEMENT_RIGHT, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 10, 11)
    transition_19 = tm.Transition(['Y', '_', '_'], ['Y', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 11, 10)
    transition_20 = tm.Transition(['_', '_', '_'], ['_', '_', '_'], [tm.MOVEMENT_STAY, tm.MOVEMENT_STAY, tm.MOVEMENT_STAY], 11, 12)

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



def test2():
    entry, transitions = parse_tm('input_ex1.txt')
    tmn = tm.TripleTapeTuringMachine(entry)
    tmn.set_input_tape(entry)
    tmn.set_initial_state(0)
    tmn.set_final_state(6)

    for t in transitions:
        tmn.add_transition(t)

    if(tmn.run(print_tapes=True, print_transition=True)):
        print("Accepted")
    else:
        print("Rejected")

if __name__ == '__main__':
    # test1()
    test2()