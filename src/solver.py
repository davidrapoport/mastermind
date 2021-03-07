import board
import collections
import itertools

def filter_possibilities(possible_solutions, move, num_blacks, num_whites):
    return [solution for solution in possible_solutions 
            if is_valid(solution, move, num_blacks, num_whites)]

## Checks to see if a given solution is still a valid one given
## That we have made the guess and received num_blacks/whites as output 
def is_valid(solution, guess, num_blacks, num_whites):
    solution_counter = collections.Counter(solution)
    ## Check the black pegs first to ensure that there are exactly
    ## num_blacks position + color matches.
    num_blacks_remaining = num_blacks
    black_indices = set()
    for i, peg in enumerate(guess):
        if peg == solution[i]:
            black_indices.add(i)
            num_blacks_remaining -= 1
            solution_counter[peg] -= 1
    if num_blacks_remaining != 0:
        return False
    ## Check that there is exactly one color match per white
    ## (that was not already counted as a black)
    for i, peg in enumerate(guess):
        if i in black_indices:
            continue
        if solution_counter[peg] > 0:
            solution_counter[peg] -= 1
            num_whites -= 1
    if num_whites != 0:
        return False
    return True

def get_all_black_white_pairs():
    possible = []
    for num_black, num_white in itertools.product(range(5), range(5)):
        if num_black + num_white > 4:
            continue
        if num_black == 3 and num_white == 1:
            continue
        possible.append((num_black, num_white))
    return possible

class Solver:

    def __init__(self):
        self.possible_solutions = board.create_all_possible_solutions()
        self.all_possible_moves = self.possible_solutions

    def pick_move(self):
        if len(self.possible_solutions) == 1:
            return self.possible_solutions[0]
        move_results = []
        for move in self.all_possible_moves:
            max_possibilities = -1
            for num_blacks, num_whites in get_all_black_white_pairs():
                max_possibilities = max(max_possibilities, 
                                        len(filter_possibilities(self.possible_solutions, move, 
                                                                num_blacks, num_whites)))
            move_results.append((move, max_possibilities))
        move_results.sort(key=lambda x: x[1])
        return move_results[0][0]
    
    def make_move(self, move, num_blacks, num_whites):
        # print("%s possible solutions prior to filtering" % len(self.possible_solutions))
        # print("Solution still in result: {}".format(('BLACK', 'GREEN', 'BLUE', 'RED') in self.possible_solutions))
        self.possible_solutions = filter_possibilities(self.possible_solutions, move, num_blacks, num_whites)
        self.all_possible_moves.remove(move)
        # print("%s possible solutions after filtering" % len(self.possible_solutions))
        # print("Solution still in result: {}".format(('BLACK', 'GREEN', 'BLUE', 'RED') in self.possible_solutions))


    def has_won(self):
        return len(self.possible_solutions) == 1

def test_is_valid():
    SOLUTION = ('GREEN', 'GREEN', 'GREEN', 'YELLOW')
    GUESS1 = ('GREEN', 'GREEN', 'GREEN', 'YELLOW')
    assert(is_valid(SOLUTION, GUESS1, 4, 0))
    assert(not is_valid(SOLUTION, GUESS1, 0, 0))
    assert(not is_valid(SOLUTION, GUESS1, 0, 4))
    assert(not is_valid(SOLUTION, GUESS1, 2, 2))

    GUESS2 = ('WHITE', 'WHITE', 'BLACK', 'GREEN')
    assert(is_valid(SOLUTION, GUESS2, 0, 1))
    assert(not is_valid(SOLUTION, GUESS2, 1, 1))
    assert(not is_valid(SOLUTION, GUESS2, 0, 2))
    assert(not is_valid(SOLUTION, GUESS2, 0, 0))

    GUESS3 = ('GREEN', 'WHITE', 'BLACK', 'GREEN')
    assert(is_valid(SOLUTION, GUESS3, 1, 1))
    assert(not is_valid(SOLUTION, GUESS3, 0, 1))
    assert(not is_valid(SOLUTION, GUESS3, 2, 2))
    assert(not is_valid(SOLUTION, GUESS3, 0, 0))


    GUESS4 = ('BLUE', 'WHITE', 'BLACK', 'RED')
    assert(is_valid(SOLUTION, GUESS4, 0, 0))
    assert(not is_valid(SOLUTION, GUESS4, 1, 1))
    assert(not is_valid(SOLUTION, GUESS4, 0, 2))
    assert(not is_valid(SOLUTION, GUESS4, 2, 0))



if __name__ == "__main__":
    test_is_valid()