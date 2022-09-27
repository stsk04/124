import turtle as t
import random as r

num_sides = 25
path_width = 15
wall_color = "blue"


maze_drawer = t.Turtle()
maze_drawer.pensize(5)
maze_drawer.pencolor(wall_color)
maze_drawer.speed('fastest')


wall_len= path_width*2

for w in range(num_sides):
  wall_len += path_width
  if (w >4):
    maze_drawer.left(90)

    door= r.randint(path_width*2, (wall_len-path_width*2))
    barrier = r.randint(path_width*2, (wall_len-path_width*2))

    while abs(door - barrier) < path_width:
      #new value for barrier
      door= r.randint(path_width*2, (wall_len-path_width*2))

    if (door<barrier):
      #draw door
      maze_drawer.forward(door)
      maze_drawer.pu()
      maze_drawer.fd(path_width*2)
      maze_drawer.pd()

      #draw barrier
      maze_drawer.fd(barrier-(door+path_width*2))
      maze_drawer.left(90)
      maze_drawer.fd(path_width*2)
      maze_drawer.backward(path_width*2)
      maze_drawer.right(90)

      #draw remaining portion of wall
      maze_drawer.fd(wall_len-barrier)
    
    else:
      #draw barrier first
      maze_drawer.fd(barrier)
      maze_drawer.left(90)
      maze_drawer.fd(path_width*2)
      maze_drawer.backward(path_width*2)
      maze_drawer.right(90)

      #draw door
      maze_drawer.forward(door-(barrier))
      maze_drawer.pu()
      maze_drawer.fd(path_width*2)
      maze_drawer.pd()
      
      #draw remaining portion of wall
      maze_drawer.fd(wall_len-door-path_width*2)




wn = t.Screen()
wn.mainloop()
