# this is james and abigail's battleship project
def checkIfHitOrMiss(guess, opponents_board):
    """
    This function will check whether a guess
    is a hit or a miss and print out the result
    """
    opponents_slot = opponents_board[guess]
    if opponents_slot == " ":
        print "Miss!"
        opponents_board[guess] = "M"
    if opponents_slot == "M" or opponents_slot == "SH":
        print "You've already guess this! Try again."
    if opponents_slot == "SNH":
        print "You've hit the ship!"
        opponents_board[guess] = "SH"
        for each_slot in opponents_board:
            # check each to see if it is 'SNH'
            # because if so, game is not over






guess = 4
opponents_board = [
    " ", " ", "M",
    " ", "SNH", "SH",
    " ", "M", " "
]

checkIfHitOrMiss(guess, opponents_board)
