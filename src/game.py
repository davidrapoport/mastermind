from board import create_all_possible_solutions, compare_rows, NUM_PEGS_PER_ROW
from solver import Solver
from ui import create_row
import random

COLORS_MAP = {"g": "GREEN", "y": "YELLOW", "w": "WHITE", "bk": "BLACK", "bu": "BLUE", "r": "RED"}
DEBUG = False
RUN_SIMULATION = True

def play_simulation():
    solver = Solver()
    num_guesses = 0
    solutions = list(create_all_possible_solutions())
    solution = random.choice(solutions)
    print("Solution is {}".format(solution))
    with open("output.html", "w") as f:
        while True:
            if num_guesses == 0:
                move =  ("GREEN", "GREEN", "YELLOW", "YELLOW")
            else:
                move = solver.pick_move()
            print("Making move: {}".format(move))
            num_blacks, num_whites = compare_rows(move, solution)
            f.write(create_row(move, num_blacks, num_whites))
            print("%s Black pegs and %s white pegs" %(num_blacks, num_whites))
            if solver.has_won():
                print("WOOHOOO!!!")
                break
            solver.make_move(move, num_blacks, num_whites)
            num_guesses += 1
            if num_guesses >= 10:
                print("BAD ALGORITHM!!!")
                break



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

if __name__ == "__main__":
    if RUN_SIMULATION:
        play_simulation()
    else:
        play_game()