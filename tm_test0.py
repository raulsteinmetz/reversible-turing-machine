import tm
from rtm import ReversibleTuringMachine

from tm_54_converter import parse_tm

def test0():
    entry, transitions = parse_tm('input_ex1.txt')
    tmn = tm.TripleTapeTuringMachine(entry)
    tmn.set_input_tape(entry)
    tmn.set_initial_state(0)
    tmn.set_final_state(5)

    for t in transitions:
        tmn.add_transition(t)

    if(tmn.run(print_tapes=True, print_transition=False)):
        print("Accepted")
    else:
        print("Rejected")


def test1():
    entry, transitions = parse_tm('input_ex1.txt')
    tmn = tm.TripleTapeTuringMachine(entry)
    tmn.set_input_tape(entry)
    tmn.set_initial_state(0)
    tmn.set_final_state(5)

    for t in transitions:
        tmn.add_transition(t)

    rtmn = ReversibleTuringMachine(tmn)
    rtmn.add_history()


    if(rtmn.run(print_tapes=True, print_transition=False)):
        print("Accepted")
    else:
        print("Rejected")

if __name__ == '__main__':
    test1()
    #test0()