import turtle as t
import random as r

num_sides = 25
path_width = 15
wall_color = "blue"


maze_drawer = t.Turtle
maze_drawer.pensize(5)
maze_drawer.pencolor(wall_color)
maze_drawer.speed('fastest')


wall_len= path_width

for w in range(num_sides):
  wall_len += path_width
  if (w >4):
    maze_drawer.left(90)

    door= r.randint(path_width*2, (wall_len-path_width*2))
    barrier = r.randint(path_width*2, (wall_len-path_width*2))

    while abs(door - barrier) < path_width:
      #new value for barrier
     door= r.randint(path_width*2, (wall_len-path_width*2))

