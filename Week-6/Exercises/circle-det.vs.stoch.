import random
from expyriment import design, control, stimuli, misc
from expyriment.misc import constants

exp = design.Experiment()
# adding variable names 
exp.add_data_variable_names(["block", "trial", "circle_position", "key_pressed", "correct", "reaction_time"])

control.set_develop_mode()
control.initialize(exp)

# first block: deterministic 
block_one = design.Block(name="deterministic")
trial_one = design.Trial()
cue = stimuli.TextLine("select the circle")
cue.preload()
trial_one.add_stimulus(cue)
block_one.add_trial(trial_one)

# circle always on the right 
position_det = ["right", "right", "right", "right"]

for position in position_det:
    trial = design.Trial()
    square = stimuli.Rectangle(size=(50, 50), position=(-100, 0), colour=(255, 0, 255))
    circle = stimuli.Circle(radius=25, position=(100, 0), colour=(0, 255, 255))
    square.preload()
    circle.preload()
    trial.add_stimulus(square)   # stimuli[0]
    trial.add_stimulus(circle)   # stimuli[1]
    block_one.add_trial(trial)

exp.add_block(block_one)

# 2nd block: stochastic
block_two = design.Block(name="stochastic")
trial_one = design.Trial()
cue = stimuli.TextLine("select the circle")
cue.preload()
trial_one.add_stimulus(cue)
block_two.add_trial(trial_one)

# circle alternating 
position_stoch = ["left", "left", "right", "right"]
random.shuffle(position_stoch) # shuffling the positions so it is random

for position in position_stoch:
    trial = design.Trial()
    if position == "right":
        square = stimuli.Rectangle(size=(50, 50), position=(-100, 0), colour=(255, 0, 255))
        circle = stimuli.Circle(radius=25, position=(100, 0), colour=(0, 255, 255))
    else:
        square = stimuli.Rectangle(size=(50, 50), position=(100, 0), colour=(255, 0, 255))
        circle = stimuli.Circle(radius=25, position=(-100, 0), colour=(0, 255, 255))
    square.preload()
    circle.preload()
    trial.add_stimulus(square)   # stimuli[0]
    trial.add_stimulus(circle)   # stimuli[1]
    block_two.add_trial(trial)

exp.add_block(block_two)

control.start()

# for block in experimental blocks
for block in exp.blocks:
 
    if block.name == "deterministic":
        position = position_det
    else:
        position = position_stoch
 
    trial_index = 0 # because first I need to present text 
    for trial in block.trials:
        if trial_index == 0:
            trial.stimuli[0].present()
            exp.clock.wait(1000)
            trial_index += 1
        else:
            circle_position = position[trial_index - 1]  # -1 bc there is trial with the text
            trial.stimuli[0].present(clear=True, update=False)   # square
            trial.stimuli[1].present(clear=False, update=True)   # circle
 
            key, rt = exp.keyboard.wait(keys=[constants.K_LEFT, constants.K_RIGHT])
 
            if circle_position == "right" and key == constants.K_RIGHT:
                correct = "correct"
            elif circle_position == "left" and key == constants.K_LEFT:
                correct = "correct"
            else:
                correct = "incorrect"
 
            feedback = stimuli.TextLine("correct" if correct == "correct" else "incorrect")
            feedback.present()
            exp.clock.wait(1000)
 
            key_name = "left" if key == constants.K_LEFT else "right" # this is to make keys readable, bc they are saved as numbers
            exp.data.add([block.name, trial.id, circle_position, key_name, correct, rt])
 
            trial_index += 1
 
control.end()