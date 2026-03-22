from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")
fixation.preload() # loading before timing starts, no delays
text.preload()

t0 = exp.clock.time # time before presenting fixation
fixation.present()
t1= exp.clock.time # time after presentation
dt = t1-t0 # time taken to present fixation

exp.clock.wait(1000 - dt) # if fixation = 1s, you need to subtract the fixation presentation

text.present()
t2 = exp.clock.time

exp.clock.wait(1000 - dt)

fix_duration = (t2 - t1)/1000 # how long fixation was present?
units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()