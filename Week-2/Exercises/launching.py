# Import the main modules of expyriment
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Squares")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

red_square = stimuli.Rectangle(size=(50,50), colour=(255,0,0), position=(-400,0))
green_square = stimuli.Rectangle(size=(50,50), colour=(0,255,0), position=(0,0))

red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)

#step parameters
square_length = 50     # square width
step_size = 10         # movement speed in pixels per frame
displacement = 400     # total distance the red square travels

while green_square.position[0] - red_square.position[0] > square_length:
# move red square to the right
    red_square.move((step_size,0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)

while green_square.position[0] < displacement: 
    green_square.move((step_size, 0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)

exp.keyboard.wait()
control.end()