# a116_buggy_image.py
import turtle as trtl
spider = trtl.Turtle()

# draw spider body
spider.pensize(40)
spider.circle(20)

# define the number, length, and angle of legs
legs = 8
length = 70
angles = 365 / legs
spider.pensize(5)

# draw spider legs
n = 0
while (n < legs):
  spider.goto(0,20)
  spider.setheading(angles*n)
  spider.forward(length)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()