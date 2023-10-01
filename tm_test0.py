import tm
from rtm import ReversibleTuringMachine

from tm_54_converter import parse_tm


def test1():
    entry, transitions, _, alpha_tm = parse_tm('./input_ex3.txt')
    tmn = tm.TripleTapeTuringMachine(entry, alphabet=alpha_tm)
    tmn.set_input_tape(entry)
    tmn.set_initial_state('q0')

    for t in transitions:
        tmn.add_transition(t)

    rtmn = ReversibleTuringMachine(tmn)
    rtmn.apply_conversion()

    if(rtmn.run(print_tapes=True, print_transition=True)):
        print("\n\nAccepted")
    else:
        print("\n\nRejected")

    print('FINAL STATE: ' + rtmn.tm.current_state)
    print('FINAL TAPES')
    rtmn.tm.print_tapes(rtmn.tm.current_state, rtmn.tm.tape_one.head_index, rtmn.tm.tape_two.head_index, rtmn.tm.tape_three.head_index)

if __name__ == '__main__':
    test1()