import turtle
'''
#clcoding.com
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)

for i in range (800):
    t.forward(i*2/3+i)
    t.right(90.3)
#clcoding.com  
'''
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background for contrast

# Set up the turtle
star = turtle.Turtle()
# Fast speed
star.color("yellow")  # Yellow star
star.width(3)  # Thicker lines for visibility

# Coordinates of a 5-point star (assuming center at (0,0))
points = [
    (0, 100),     # Top point
    (58, -80),    # Bottom right
    (-95, 31),    # Left middle
    (95, 31),     # Right middle
    (-58, -80),   # Bottom left
    (0, 100)      # Back to top to close the star
]

# Function to draw star using .goto()
def draw_star():
    star.penup()
    star.goto(points[0])  # Move to the first point
    star.pendown()

    for point in points[1:]:
        star.goto(point)  # Draw the star by going to each point in order

# Draw the star
draw_star()

# Hide the turtle
star.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
