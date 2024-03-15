import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle for drawing
artist = turtle.Turtle()
# Set the speed to the maximum
artist.speed(0)
# Set the width of the pen
artist.width(2)

# Colors for our drawing
colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "cyan",
    "magenta",
    "white",
]


def draw_pattern(radius, color1, color2):
    artist.color(color1)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()
    artist.circle(radius, 60)
    artist.color(color2)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()
    artist.circle(radius, 60)


# Main drawing function
def draw_artwork():
    artist.penup()
    # Start drawing from the bottom center
    artist.goto(0, -150)
    artist.pendown()

    # 36 repetitions for 360 degrees
    for _ in range(36):
        color1 = random.choice(colors)
        color2 = random.choice(colors)
        # Ensure we get two distinct colors
        while color2 == color1:
            color2 = random.choice(colors)
        draw_pattern(150, color1, color2)
        # Rotate the pattern by 10 degrees
        artist.right(10)

    artist.hideturtle()


# Call the drawing function
draw_artwork()

# Keep the window open
turtle.mainloop()
