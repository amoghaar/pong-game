from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")  # Set the color of the ball to white
        self.shape("circle")  # Set the shape of the ball to a circle
        self.penup()  # Lift the pen, so no drawing occurs during movements
        self.x_move = 10  # Set the initial x-axis movement speed of the ball
        self.y_move = 10  # Set the initial y-axis movement speed of the ball
        self.ball_speed = 0.1  # Set the initial speed of the ball

    def move(self):
        # Move the ball by updating its x and y coordinates
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)  # Set the new position of the ball

    def bounce(self):
        # Reverse the y-axis movement direction to simulate a bounce
        self.y_move *= -1

    def bounce_back(self):
        # Reverse the x-axis movement direction to simulate a bounce back
        self.x_move *= -1
        # Increase the speed of the ball slightly when it bounces back
        self.ball_speed *= 0.9

    def start_again(self):
        # Reset ball parameters when a point is scored
        self.ball_speed = 0.1  # Reset the speed of the ball
        self.goto(x=0, y=0)  # Move the ball back to the center
        self.x_move *= -1  # Reverse the x-axis movement direction
        self.y_move *= -1  # Reverse the y-axis movement direction
