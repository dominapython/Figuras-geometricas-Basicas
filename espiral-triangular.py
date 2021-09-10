import turtle
t = turtle.Pen()
turtle.bgcolor("Darkblue")
t.shape("turtle")
t.shapesize(1)
# You can choose between 2 and 6 sides for some cool shapes!
sides = 3
colors = ["fuchsia", "chartreuse2", "cyan"]
for x in range(360):
 t.pencolor(colors[x%sides])
 t.forward(x * 3/sides + x)
 t.left(360/sides + 1)
 t.width(x*sides/200)
 t.speed(30)