from expyriment import design, control, stimuli

exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

cue = stimuli.TextLine("press a key")
t0 = exp.clock.time
key = exp.keyboard.wait()
t1 = exp.clock.time

dt = (t1-t0)/1000

feedback = stimuli.TextLine(f"It took you {dt} seconds")
feedback.present()

exp.clock.wait(3000)

control.end()

