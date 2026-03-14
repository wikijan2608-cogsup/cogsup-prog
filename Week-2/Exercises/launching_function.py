# Import expyriment modules
from expyriment import design, control, stimuli
control.set_develop_mode()

# Create experiment
exp = design.Experiment(name="Launching Function")
control.initialize(exp)

def launching_function(disrupt_time=False, disrupt_space=False, triggering=False):
    red_square = stimuli.Rectangle(size=(50,50), colour=(255,0,0), position=(-400,0))
    green_square = stimuli.Rectangle(size=(50,50), colour=(0,255,0), position=(0,0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(1000)

    square_length = 50
    step_size = 10
    displacement = 400

    if disrupt_space:
        gap = 50
    else:
        gap = 0

 # this part of the code moves red square to the right 
    while green_square.position[0] - red_square.position[0] > square_length + gap:

        red_square.move((step_size,0))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)

# check for disrupt time
    if disrupt_time:
        exp.clock.wait(200)
    
    if triggering:
        step_size = step_size * 3
    else:
        step_size = step_size
    
# this part of the code moves green square to the right 
    while green_square.position[0] < displacement: 
        green_square.move((step_size, 0))
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)


# test
launching_function(False, False, False) #Michottean launching
launching_function(True, False, False) # launching with temporal gap
launching_function(False,True,False) #lauching with spatial gap
launching_function(False, False, True) # triggering

exp.keyboard.wait()
control.end()