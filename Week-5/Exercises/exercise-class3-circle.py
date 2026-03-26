from expyriment import design, control, stimuli, misc
from expyriment.misc import constants

exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

# present both circle and a square
# provide correct feedback
# either KEY_RIGHT or KEY_LEFT
# either correct or incorrect
cue = stimuli.TextLine("select a circle")
cue.present()
exp.clock.wait(1000)

square = stimuli.Rectangle(size=(50,50), position=(-100,0))

circle = stimuli.Circle(radius=25, position=(100,0))

square.present(clear=True, update=False)
circle.present(clear=False, update=True)

key, rt = exp.keyboard.wait(keys=[constants.K_LEFT, constants.K_RIGHT])

if key == constants.K_RIGHT:
    feedback = stimuli.TextLine("Correct")
else:
    feedback = stimuli.TextLine("Incorrect")

feedback.present()
exp.clock.wait(1000)

control.end()
