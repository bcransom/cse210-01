# INITIAL ATTEMPT = UNSUCCESSFUL

def main():

    play_game = True
    # play_game = input("Do you want to play tic-tac-toe? (Y/N)")

    # while play_game.capitalize is True:
        
    one = "1"
    two = "2"
    three = "3"
    four = "4"
    five = "5"
    six = "6"
    seven = "7"
    eight = "8"
    nine = "9"

    print(f"{one} | {two} | {three} ")
    print("- + - + -")
    print(f"{four} | {five} | {six} ")
    print("- + - + -")
    print(f"{seven} | {eight} | {nine} ")

    def play():
        player = input("Please choose a square (1-9) ")
        
            if player == "X" or "Y": 
                print("That square has already been chosen. Please try again.")
                player = input("Please choose a square (1-9) ")
            else: 
                return player

    print()
    print("Player One")
    play()


    def spot():
        if player == "1":
            one = "X"
            one = "player"
            two = "player"
            three = "player"
            four = "player"
            five = "player"
            six = "player"
            seven = "player"
            eight = "player"
            nine = "player"
        

main()