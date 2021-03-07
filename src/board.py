import collections
import itertools

COLORS = ["GREEN", "YELLOW", "WHITE", "BLACK", "BLUE", "RED"]
NUM_PEGS_PER_ROW = 4

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