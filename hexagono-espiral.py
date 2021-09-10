import turtle
t = turtle.Pen()
t.shape("turtle")
colores =['red','orange','yellow','cyan','green','purple']
turtle.bgcolor('black')
for i in range(360):
	t.pencolor(colores[i%6])
	t.width(i/100+1)
	t.forward(i)
	t.left(59)
	t.speed(20)