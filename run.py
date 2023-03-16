# 1. Start
# 2. Display instructions and ask to press any key to start (validate)
# 3. Ask for player's name (validate)
# 4. Ask to pick a symbol (X or O) (validate) save as global variable
# 5. Create board (python list)
# 6. Display board
# 7. Player starts -> Ask player to make a move (validate) check numbers, is already taken (is not dash inside)
# 8. Display board after player's move
# 9. Computer randomly select it's move (function check position)
# 10. Display board after player's move + computer's move
# 11. Check for winner - if there's 3 in a row in any of: (check after every input)
# check rows
# check columns
# check diagonal
# 12. Check for tie - if the board is full
# 13. If there is no winner/tie -> repeat 7 - 12
# 14. If there is a winner/tie -> print message
# 15. Ask the player to play again (Y/N) (validate)
# No -> end game
# Yes -> Reset and flip players (Computer starts) (make sure it starts with clear board)


board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

# def main():

# Function for displaying board
def display_board():
    print(board[0] + "     | " + board[1] + " | " + board[2] + "       1 | 2 | 3")
    print("    --+---+--       --+---+--")
    print(board[3] + "     | " + board[4] + " | " + board[5] + "       4 | 5 | 6")
    print("    --+---+--       --+---+--")
    print(board[6] + "     | " + board[7] + " | " + board[8] + "       7 | 8 | 9")


print(display_board())


# main()
