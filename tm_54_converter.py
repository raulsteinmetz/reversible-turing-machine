from collections import deque
from tm import Transition, MOVEMENT_STAY, MOVEMENT_LEFT, MOVEMENT_RIGHT

movements = {'R': MOVEMENT_RIGHT, 'L': MOVEMENT_LEFT, 'S': MOVEMENT_STAY}

def open_file(tm_5_file_path: str):
    try:
        with open(tm_5_file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file '{tm_5_file_path}' was not found.")
    except IOError as e:
        print(f"An error occurred while trying to open the file: {e}")

def get_transitions_5(tm_5_def: str):
    lines = tm_5_def.split('\n')
    return [lines[i] for i in range(len(lines)) if i not in [0, 1, 2, 3, len(lines) - 1]]

def reformat_transitions_5(transitions_5: list):
    tmp = [s.replace(',', '') for s in transitions_5]
    tmp = [s.replace('(', '') for s in tmp]
    tmp = [s.replace(')', '') for s in tmp]
    tmp = [s.replace('=', '') for s in tmp]
    tmp = [s.replace('B', '_') for s in tmp]
    return tmp


def convert(tm_5_file_path: str):
    # n faco ideia se ta funfando kkkk
    transitions_5 = reformat_transitions_5(get_transitions_5(open_file(tm_5_file_path)))
    print(transitions_5)
    transitions_4 = []

    for t in transitions_5:
        mvtr_index = int(t[0]) - 1 + len(transitions_5)
        for transition in transitions_4:
            if transition.current_state == mvtr_index:
                mvtr_index += 100


        transitions_4.append(Transition([t[1], '_', '_'], [t[3], '_', '_'], \
                                        [MOVEMENT_STAY, MOVEMENT_STAY, MOVEMENT_STAY], \
                                            int(t[0]) - 1, mvtr_index))
        transitions_4.append(Transition(['/', '/', '/'], ['/', '/', '/'], \
                                        [movements[t[4]], MOVEMENT_STAY, MOVEMENT_STAY], \
                                        mvtr_index, int(t[2]) - 1))
        
    
    transitions_4.pop()

    return transitions_4

def get_entry(tm_5_file_path: str):
    with open(tm_5_file_path) as file:
        return list(file.readlines() [-1:][0])

def parse_tm(tm_5_file_path: str):
    return get_entry(tm_5_file_path), \
        convert(tm_5_file_path)


def main():
    entry, transitions = parse_tm('input_ex1.txt')
    


if __name__ == '__main__':
    main()