import random  # Import the random module


# Function to create a grid
def create_grid(size):
    return [['O' for _ in range(size)] for _ in range(size)]