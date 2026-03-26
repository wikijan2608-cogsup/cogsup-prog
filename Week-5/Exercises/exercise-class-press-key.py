from expyriment import design, control, stimuli

exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

cue = stimuli.TextLine("press a key")
key = exp.keyboard.wait()

feedback = stimuli.TextLine(f"you pressed + {key}")
feedback.present()

exp.clock.wait(3000)

control.end()




