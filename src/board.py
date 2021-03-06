import collections
import itertools
import random

COLORS = ["GREEN", "YELLOW", "WHITE", "BLACK", "BLUE", "RED"]
COLORS_MAP = {"g": "GREEN", "y": "YELLOW", "w": "WHITE", "bk": "BLACK", "bu": "BLUE", "r": "RED"}
NUM_PEGS_PER_ROW = 4
DEBUG = False

def create_all_possible_solutions():
    return list(itertools.product(COLORS, repeat=NUM_PEGS_PER_ROW))

def compare_rows(guess, solution):
    num_whites = 0
    num_blacks = 0
    assert(len(guess) == NUM_PEGS_PER_ROW)
    assert(len(guess) == len(solution))
    solution_counter = collections.Counter(solution)
    ## Loop once and note all the black indices
    black_indices = set()
    for i, peg in enumerate(solution):
        if guess[i] == peg:
            black_indices.add(i)
            solution_counter[peg] -= 1
    num_blacks = len(black_indices)
    for i, peg in enumerate(guess):
        if i in black_indices:
            continue
        if solution_counter[peg] >= 1:
            num_whites += 1
            solution_counter[peg] -= 1
    return num_blacks, num_whites

def parse_input(input_string):
    pass

def play_game():
    print("Enter moves as a comma separated string")
    print("Possible keys %s" % COLORS_MAP)
    print("Example: bk,bu,g,g")
    solutions = list(create_all_possible_solutions())
    solution = random.choice(solutions)
    if DEBUG:
        print(solution)
    num_guesses = 0
    while True:
        print("Enter Move:")
        move = raw_input()
        parsed_move = move.strip().lower().split(",")
        assert(len(parsed_move) == NUM_PEGS_PER_ROW)
        move_tuple = tuple([COLORS_MAP[peg] for peg in parsed_move])
        num_guesses += 1
        num_blacks, num_whites = compare_rows(move_tuple, solution)
        print("%s Black pegs and %s white pegs" %(num_blacks, num_whites))
        if num_blacks == 4:
            print("WOOHOO YOU WIN!!!")
            break
        if num_guesses >= 10:
            print("YOU LOSE YOU DUMB FUCK")
            break

play_game()

def test1():
    SOLUTION = ('GREEN', 'GREEN', 'GREEN', 'YELLOW')
    GUESS1 = ('GREEN', 'GREEN', 'GREEN', 'YELLOW')
    num_blacks, num_whites = compare_rows(GUESS1, SOLUTION)
    assert(num_blacks == 4)
    assert(num_whites == 0)

    GUESS2 = ('WHITE', 'WHITE', 'BLACK', 'GREEN')
    num_blacks, num_whites = compare_rows(GUESS2, SOLUTION)
    assert(num_blacks == 0)
    assert(num_whites == 1)

    GUESS3 = ('GREEN', 'WHITE', 'BLACK', 'GREEN')
    num_blacks, num_whites = compare_rows(GUESS3, SOLUTION)
    assert(num_blacks == 1)
    assert(num_whites == 1)

    GUESS4 = ('BLUE', 'WHITE', 'BLACK', 'RED')
    num_blacks, num_whites = compare_rows(GUESS4, SOLUTION)
    assert(num_blacks == 0)
    assert(num_whites == 0)

test1()