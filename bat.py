from turtle import Turtle


class Bat(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Bat object using the Turtle class

    def creating_paddle(self, positive_negative, yaxis):
        # Create and set up the paddle
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.shapesize(stretch_wid=5, stretch_len=1)  # Adjust the size of the paddle
        self.penup()  # Lift the pen, so no drawing occurs during movements
        self.goto(x=positive_negative, y=yaxis)  # Position the paddle

    def up(self):
        # Move the paddle up by adjusting its y-coordinate
        new_positive_y = self.ycor() + 20  # Increment the y-coordinate
        self.goto(self.xcor(), new_positive_y)  # Set the new position

    def down(self):
        # Move the paddle down by adjusting its y-coordinate
        new_negative_y = self.ycor() - 20  # Decrement the y-coordinate
        self.goto(self.xcor(), new_negative_y)  # Set the new position
