
from expyriment import design, control, stimuli

exp = design.Experiment(name="Edges")
#control.set_develop_mode()  turn this off to test in regular mode
control.initialize(exp)

screen_width, screen_height = exp.screen.size
square_length = int(round(screen_width * 0.05))
half = square_length / 2

# coordinates relative to screen center in expyriment.
x_left = -(screen_width / 2) + half
x_right = (screen_width / 2) - half
y_top = -(screen_height / 2) + half
y_bottom = (screen_height / 2) - half

bottom_left = stimuli.Rectangle(size=(square_length, square_length), line_width=1, colour=(255, 0, 0), position=(x_left, y_bottom))
bottom_right = stimuli.Rectangle(size=(square_length, square_length), line_width=1, colour=(255, 0, 0), position=(x_right, y_bottom))
top_left = stimuli.Rectangle(size=(square_length, square_length), line_width=1, colour=(255, 0, 0), position=(x_left, y_top))
top_right = stimuli.Rectangle(size=(square_length, square_length), line_width=1, colour=(255, 0, 0), position=(x_right, y_top))

bottom_left.present(clear=True, update=False)
bottom_right.present(clear=False, update=False)
top_left.present(clear=False, update=False)
top_right.present(clear=False, update=True)

exp.clock.wait(1000)
exp.keyboard.wait()
control.end()