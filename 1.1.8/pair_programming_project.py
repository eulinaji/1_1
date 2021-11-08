import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# ears
painter.penup()
painter.setposition(-140,110)
painter.pendown()
painter.color("dimgray")
painter.begin_fill()
painter.circle(80,360,10)
painter.end_fill()

painter.penup()
painter.forward(280)
painter.pendown()

painter.color("dimgrey")
painter.begin_fill()
painter.circle(80,360,10)
painter.end_fill()

# head base

painter.penup()
painter.setposition(0,-300)
painter.pendown()

painter.color("whitesmoke")
painter.begin_fill()
painter.circle(250)
painter.end_fill()

# eye 
painter.setposition(-85,-80)
painter.color("dimgrey")
painter.begin_fill()
painter.circle(70)
painter.end_fill()

painter.penup()
painter.forward(180)
painter.pendown()

painter.begin_fill()
painter.circle(70)
painter.end_fill()

# pupils
painter.setposition(-85,-70)
painter.color("black")
painter.begin_fill()
painter.circle(40)
painter.end_fill()

painter.penup()
painter.forward(180)
painter.pendown()

painter.begin_fill()
painter.circle(40)
painter.end_fill()

# highlight
painter.setposition(-85,-50)
painter.color("white")
painter.begin_fill()
painter.circle(10)
painter.end_fill()

painter.penup()
painter.forward(180)
painter.pendown()

painter.begin_fill()
painter.circle(10)
painter.end_fill()

# snout
painter.penup()
painter.setposition(5,-220)
painter.pendown()
painter.color("silver")
painter.begin_fill()
painter.circle(90)
painter.end_fill()

# nose
painter.penup()
painter.setposition(5,-140)
painter.pendown()
painter.color("lavenderblush")
painter.begin_fill()
painter.circle(35)
painter.end_fill()

# smile
painter.penup()
painter.setposition(5,-140)
painter.pendown()
painter.pensize(4)
painter.color("black")
painter.right(90)
painter.circle(35,180)

painter.penup()
painter.setposition(-70,-140)
painter.pendown()
painter.pensize(4)
painter.color("black")
painter.left(180)
painter.circle(35,180)

wn = trtl.Screen()
wn.mainloop()