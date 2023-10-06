from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()  # Lift the pen, so no drawing occurs during movements
        self.hideturtle()  # Hide the turtle icon
        self.color("white")  # Set the text color to white
        self.left_score = 0  # Initialize the left player's score to 0
        self.right_score = 0  # Initialize the right player's score to 0
        self.update_score()  # Call the method to display the initial score

    def update_score(self):
        # Display the scores on the screen
        self.goto(x=-100, y=230)
        self.write(f"{self.left_score}", align="center", font=("Courier", 50, "normal"))
        self.goto(x=100, y=230)
        self.write(f"{self.right_score}", align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        # Update the left player's score and refresh the display
        self.left_score += 1
        self.clear()  # Clear the previous score display
        self.update_score()  # Update and display the new score

    def r_point(self):
        # Update the right player's score and refresh the display
        self.right_score += 1
        self.clear()  # Clear the previous score display
        self.update_score()  # Update and display the new score
