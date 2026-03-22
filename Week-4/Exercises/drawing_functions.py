from expyriment import design, control, stimuli
import random
import math

FPS = 60 # frames per second, standard screen refresh rate
MSPF = 1000 / FPS # milliseconds per frame (more robust than using 16.67) 

def to_frames(t):
    return math.ceil(t / MSPF) # converts time in ms to number of frames

def to_time(num_frames):
    return num_frames * MSPF # converts number of frames to ms

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1= exp.clock.time
    dt = t1-t0 
    return dt
    # return the time it took to draw

def present_for(stims, num_frames):
    if num_frames == 0:
        return
    dt = timed_draw(stims) # time needed for correction
    if dt > 0:
        t = to_time(num_frames) # convert frames to time
        exp.clock.wait(t-dt)


""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
load([fixation])

n = 20
positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
load(squares)

durations = []

t0 = exp.clock.time
for square in squares:
    if not square.is_preloaded:
        print("Preloading function not implemented correctly.")
    stims = [fixation, square] 
    present_for(stims, 500)
    t1 = exp.clock.time
    durations.append(t1-t0)
    t0 = t1

print(durations)

control.end()