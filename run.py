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


# Function for displaying board
def display_board():
    print("")
    print(board[0] + "   | " + board[1] + " | " + board[2] + "      1 | 2 | 3")
    print("  --+---+--      --+---+--")
    print(board[3] + "   | " + board[4] + " | " + board[5] + "      4 | 5 | 6")
    print("  --+---+--      --+---+--")
    print(board[6] + "   | " + board[7] + " | " + board[8] + "      7 | 8 | 9")
    print("")


print(display_board())


# 1. Start

# def main():

# 2. Display instructions and ask to press any key to start (validate)
print("")
print("")
print("              WELCOME TO TIC-TAC-TOE GAME !!!")
print("")
print("")
print("How to play:")
print("1. The game is played on a board that's 3 squares by 3 squares")
print("2. You are X, the computer is O. \
    Players take turns putting their marks in empty squares")
print("3. You put a mark by pressing a number on a keyboard \
    that corresponds with empty square (see board below)")
print("4. The first player to get 3 of their marks in a row \
    (up, down, across, or diagonally) is the winner")
print("5. When all 9 squares are full, the game is over. \
    If no player has 3 marks in a row, the game ends in a tie")
print("")
print(display_board())
print("")
print("Press any key to start...")
print("")

# 3. Ask for player's name (validate)
user_name = input("What's your name? ")
print("")
print(f"It's your turn {user_name}")
print("")

# 4. Ask player to make a move (validate) check numbers, is already taken (is not dash inside)
user_selection = int(input("Pick a number from 1-9 and press Enter: "))
print("")

print("")
print(display_board())
print("")


# main()
