
PEG_SVG = '''<svg height="40" width="40">
  <circle cx="20" cy="20" r="8" stroke="black" stroke-width="3" fill="{}" />
</svg> 
 '''

BLACK_PEG = PEG_SVG.format("black")
WHITE_PEG = PEG_SVG.format("white")
EMPTY_PEG_SVG = '''<svg height="40" width="40">
  <circle cx="20" cy="20" r="8" stroke="white" stroke-width="3" fill="white" />
</svg> 
 '''

GUESS_SVG = '''<svg height="40" width="40">
  <circle cx="20" cy="20" r="18" stroke="black" stroke-width="3" fill="{}" />
</svg> 
 '''

def create_row(guess, num_black, num_white):
    black_white = create_black_white(num_black, num_white)
    guess_row = create_guess(guess)
    return '''
    <span className="row" style="display: flex">
        <div className="black-white-response">
            {}
        </div>
        <div className="guess-response">
            {}
        </div>
    </span>
    '''.format(black_white, guess_row)

def create_black_white(num_black, num_white):
    pegs = [BLACK_PEG] * num_black + [WHITE_PEG] * num_white + [EMPTY_PEG_SVG] * (4 - num_white - num_black)
    return '<div className="pegs">{}</div>'.format(" ".join(pegs))

def create_guess(guess):
    row = [GUESS_SVG.format(color) for color in guess]
    return '<div className="guess">{}</div>'.format(" ".join(row))
