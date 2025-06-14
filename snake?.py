import turtle
import random
# Set the window size and title.
turtle.setup(600, 400)
turtle.title("Snake Game")

# Create the snake head.
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("green")
snake_head.penup()
snake_head.setposition(0, 0)

# Create the food.
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.setposition(50, 50)

# Create a list to store the snake's body segments.
snake_body = []

# Start the game loop.
while True:

    # Get the user input.
    key = turtle.getcanvas().keys()

    # Move the snake head.
    if key == "Up":
        snake_head.setheading(90)
    elif key == "Down":
        snake_head.setheading(270)
    elif key == "Left":
        snake_head.setheading(180)
    elif key == "Right":
        snake_head.setheading(0)

    snake_head.forward(10)

    # Check if the snake head has collided with the food.
    if snake_head.distance(food) < 10:

        # Move the food to a new random location.
        food.setposition(random.randint(-200, 200), random.randint(-200, 200))

        # Add a new segment to the snake's body.
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.setposition(snake_head.position())
        snake_body.append(new_segment)

    # Move the snake's body.
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i].setposition(snake_body[i - 1].position())

    #snake_body.setposition(snake_head.position())

    # Update the screen.
    turtle.update()

    # Check if the snake has collided with itself.
    for segment in snake_body:
        if snake_head.distance(segment) < 10:
            # Game over!
            turtle.done()
