# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry
control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# triangle 
triangle = stimuli.Shape(
    vertex_list=geometry.vertices_triangle(angle=60, length1=50, length2=50),
    colour=(160,0,160),
    position=(-80,0)
)
triangle.rotate(180)

hexagon = stimuli.Shape(
    vertex_list=geometry.vertices_regular_polygon(n_edges=6, length=25),
    colour=(255,255,0),
    position=(80,0)
)

triangle_line = stimuli.Line(start_point=(-79,21) , end_point=(-79,71) , line_width=3, colour=(255,255,255))
hexagon_line = stimuli.Line(start_point=(79,21) , end_point=(79,71) , line_width=3, colour=(255,255,255))

triangle_text = stimuli.TextLine(text = "triangle", position=(-79,91), text_colour=(255,255,255))
hexagon_text = stimuli.TextLine(text = "hexagon", position=(79,91), text_colour=(255,255,255))

triangle.present(clear=True, update=False)
hexagon.present(clear=False, update=False)
triangle_line.present(clear=False, update=False)
hexagon_line.present(clear=False, update=False)
triangle_text.present(clear=False, update=False)
hexagon_text.present(clear=False, update=True)

exp.clock.wait(1000)
exp.keyboard.wait()
control.end()