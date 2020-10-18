import turtle


def pen_jump(pen, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def turtle_setup(width=800, height=800):
    turtle.Screen()
    turtle.setup(width, height)
    turtle.clearscreen()
    turtle.title("Bohr (turtle) atom")


def turtle_pen(shape="turtle", speed=10, size=3, colors=("blue", "green")):
    pen = turtle.Turtle()
    pen.shape(shape)
    pen.speed(speed)
    pen.pensize(size)
    pen.color(*colors)
    pen_jump(pen, 0, 0)
    pen.stamp()
    return pen


def turtle_teardown(pen):
    pen.hideturtle()
    turtle.exitonclick()


def draw_atom(pen, radius, levels, electrons_per_level, electron_size=15, electron_color="red"):
    full_circle = 360
    for level in range(levels):
        r = radius * (level + 1)                           # concentric circles
        electrons_in_level = electrons_per_level[level]
        arcs = full_circle / electrons_in_level            # arcs between each electron
        circumference = 0
        pen_jump(pen, 0, -r)                               # centering
        while circumference < full_circle:
            pen.dot(electron_size, electron_color)
            pen.circle(r, arcs)
            circumference = circumference + arcs

            

totalAtoms = int(input('Enter number of atoms -> '))

for k in range(totalAtoms):
    
    electrons_per_level = []
    levels = eval(input('How many levels? '))
    first_level_radius = 45

    for i in range(levels):
        e = eval(input(f'Electrons in level {str(i + 1)}: '))
        electrons_per_level.append(e)

    print(electrons_per_level)

    turtle_setup()
    pen = turtle_pen()
    draw_atom(pen, first_level_radius, levels, electrons_per_level)
    turtle_teardown(pen)
    
   


