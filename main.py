from turtle import Screen
from bat import Bat
from ball import Ball
import time
from score import Score

# Create objects
screen = Screen()  # Create a screen object
screen.tracer(0)  # Turn off-screen updates, for smooth animation
l_bat = Bat()  # Create a left paddle
r_bat = Bat()  # Create a right paddle
ball = Ball()  # Create a ball
score = Score()  # Create a score tracker

# Setting up the screen
screen.title("Pong Game")  # Set the window title
screen.bgcolor("black")  # Set the background color
screen.setup(width=800, height=600)  # Set the dimensions of the window
l_bat.creating_paddle(350, 0)  # Create the left paddle at (350, 0)
r_bat.creating_paddle(-350, 0)  # Create the right paddle at (-350, 0)

# Keyboard bindings
screen.listen()  # Start listening for keyboard input
screen.onkeypress(fun=l_bat.up, key="Up")  # Bind the Up arrow key to move the left paddle up
screen.onkeypress(fun=l_bat.down, key="Down")  # Bind the Down arrow key to move the left paddle down
screen.onkeypress(fun=r_bat.up, key="w")  # Bind 'w' to move the right paddle up
screen.onkeypress(fun=r_bat.down, key="s")  # Bind 's' to move the right paddle down

# Game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen to show any changes
    ball.move()  # Move the ball
    time.sleep(ball.ball_speed)  # Delay to control the speed of the game

    # Check if the ball hits the top or bottom wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Check if the ball hits a paddle and bounce back
    if ball.xcor() > 340 and ball.distance(l_bat) < 75 or ball.xcor() > -1800 and ball.distance(r_bat) < 30:
        ball.bounce_back()

    # Check if the ball goes out of bounds on the right side
    if ball.xcor() > 360:
        score.l_point()  # Update the left player's score
        ball.start_again()  # Reset the ball to the center

    # Check if the ball goes out of bounds on the left side
    if ball.xcor() < -360:
        score.r_point()  # Update the right player's score
        ball.start_again()  # Reset the ball to the center

# Close the screen on click
screen.exitonclick()
