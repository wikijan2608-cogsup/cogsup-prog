from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

exp = design.Experiment(name="kanizsa squares", background_colour=C_GREY)
control.set_develop_mode()
control.initialize(exp)
control.start(exp)

screen_width, screen_height = exp.screen.size

#Square side length = 25% of screen width 
#Circle radius = 5% of screen width
square_length = int(round(screen_width * 0.25))
circle_radius = int(round(screen_width * 0.05))

circle_origin = [
    (-square_length / 2, -square_length / 2),  # top-left
    (square_length / 2, -square_length / 2),   # top-right
    (-square_length / 2, square_length / 2),   # bottom-left
    (square_length / 2, square_length / 2),    # bottom-right
]

top_left_c = stimuli.Circle(radius=circle_radius, position=circle_origin[0], colour=(255,255,255))
top_right_c = stimuli.Circle(radius=circle_radius, position=circle_origin[1], colour=(255,255,255))
bottom_left_c = stimuli.Circle(radius=circle_radius, position=circle_origin[2], colour=(30,30,30))
bottom_right_c = stimuli.Circle(radius=circle_radius, position=circle_origin[3], colour=(30,30,30))

exp.screen.clear()
top_left_c.present(clear=False, update=False)
top_right_c.present(clear=False, update=False)
bottom_left_c.present(clear=False, update=False)
bottom_right_c.present(clear=False, update=False)

# make a rectangle 
rectangle = stimuli.Rectangle(position=(0,0), size=(square_length, square_length), colour=C_GREY)
rectangle.present(clear=False, update=False)

exp.screen.update()
exp.clock.wait(1000)
exp.keyboard.wait()
control.end()

