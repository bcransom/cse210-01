def main():

    # use a list of lists to define the board
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    # define function to print the board: print_board. Use the variable board as a parameter.
    def print_board(board):
        """Use a for loop to loop through each list within the board list to print.
        Parameters
            list: board as defined above
        Return: Print each row in board list.
        """
        
        # to print each row or each list within the board, use a for loop. 
        for row in board: 
            print(row)

    
    def select_square():
        """we will use this function over and over again to ask the user
        for a number to put on the board. 
        Parameters: none
        Return: selection from user
        """
        
        # prompt user to select a square with 'selection' variable
        # confirm that selection is a number between 1-9
        selection = int(input("Choose a square (1-9): "))
        # confirm that selection is a number
        if not 1 <= selection <= 9:
            raise ValueError
        return selection
    
    
    print_board(board)
    # confirm that selection is a number between 1-9
    try: 
        selection = select_square()
    except ValueError:
        print("Sorry, please select a number 1-9.")

    # define a function 'convert_selection' that returns the user selection into the correct placement in the list
    def convert_selection(selection):
        """"Take user selection and convert it into the board placement.
        Parameters: selection
        Return: board placement
        """
        # I subtract one so that my range is now 0–8. Then, I can use floor division and modulo to supply the rows and columns.
        selection -= 1
        # return a tuple (an immutable data type that won't change) using parentheses.
        return (selection // 3, selection % 3)
    
    # define a function that takes in the selection tuple and the board as arguments and makes the correct change to the board.
    def place_piece(selection, board):
        """function will change the board to X or O by using the selection tuple and board as provided.
        Parameters: user selection, board
        Return: new board assignment - either X or O"""
        
        board[selection[0]][selection[1]] = "X"



# possible use? 
    #     board[selection - 1] = player

    # def next_player(current):
    #     if current == "" or current == "o":
    #         return "x"
    #     elif current == "x":
    #         return "o"

main()