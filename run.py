import random  # Import the random module


# Function to create a grid
def create_grid(size):
    return [['O' for _ in range(size)] for _ in range(size)]


# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))


# Function to place battleships randomly on the grid
def place_battleships(grid, num_ships):
    size = len(grid)
    for _ in range(num_ships):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        grid[x][y] = 'S'


# Function to check if a guess is on the grid and not already guessed
def is_valid_guess(guess, size, guessed_cells):
    x, y = guess
    return (0 <= x < size) and (0 <= y < size) and (guess not in guessed_cells)


# Function for computer's guess
def computer_guess(size, guessed_cells):
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    while (x, y) in guessed_cells:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
    return x, y


# Define default names
computer_name = "Computer"
player_name = "Player"


# Main game logic
def play_battleships(grid_size, num_ships):
    grid = create_grid(grid_size)
    place_battleships(grid, num_ships)
    guessed_cells = set()
    user_wins = 0
    computer_wins = 0
    attempts = 0

    player_name = input("Enter your name: ")
    computer_name = input("Enter the computer's name: ")
    print("Welcome, {}! Let's play Battleships against Computer_ {}!"
          .format(player_name, computer_name))
    print_grid(grid)

    while attempts < 5:  # Max 5 attempts
        # Player's turn
        while True:
            guess = input("Enter your guess (row column): ").split()
            if len(guess) != 2:
                print("Please enter row and column numbers.")
                continue

            # Check if both inputs are digits
            if not guess[0].isdigit() or not guess[1].isdigit():
                print("Please enter numbers for row and column.")
                continue

            x, y = map(int, guess)
            if not is_valid_guess((x, y), grid_size, guessed_cells):
                print("Invalid guess. Please enter a valid cell.")
                continue

            break

        attempts += 1
        guessed_cells.add((x, y))
        if grid[x][y] == 'S':
            print("Hit! You sank a battleship!")
            user_wins += 1
            grid[x][y] = 'X'
        else:
            print("Miss! Try again.")

        print_grid(grid)

        if all('S' not in row for row in grid):
            print("Congratulations, {}! You sank all the battleships."
                  .format(player_name))
            user_wins += 1
            break

        # Computer's turn
        comp_x, comp_y = computer_guess(grid_size, guessed_cells)
        print("{}'s guess: ({}, {})".format(computer_name, comp_x, comp_y))
        if grid[comp_x][comp_y] == 'S':
            print("{} hit your battleship!".format(computer_name))
            computer_wins += 1
            grid[comp_x][comp_y] = 'X'
        else:
            print("{} missed!".format(computer_name))

        print_grid(grid)

        if all('S' not in row for row in grid):
            print("{} wins! It sank all your battleships."
                  .format(computer_name))
            computer_wins += 1
            break

    if attempts >= 5:  # If attempts reach 5
        print("Game over! Maximum attempts reached.")
        print("Thanks for playing, {}!".format(player_name))

    print("{}'s Wins: {}".format(player_name, user_wins))
    print("{}'s Wins: {}".format(computer_name, computer_wins))

    # Ask if user wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_battleships(grid_size, num_ships)
    else:
        print("Goodbye, {}!".format(player_name))


# Start the game
grid_size = 5
num_ships = 3
play_battleships(grid_size, num_ships)
