# this is james and abigail's battleship project


def choosePosition(player_n, board):
    """
    This function lets a player choose
    where on the board to place his/her two ships
    """
    print " "
    print "Player %r: select your first slot number for your ship:" % player_n
    print " "
    drawBoard(board)
    slot_1 = int(raw_input("Slot 1 Position Number: > "))
    board[slot_1] = "X"
    print "Player %r: select your second slot number for your ship:" % player_n
    drawBoard(board)
    slot_2 = int(raw_input("Slot 2 Position Number: > "))
    while (slot_1 + 3 != slot_2 and slot_1 - 3 != slot_2 and slot_1 + 1 != slot_2 and slot_1 - 1 != slot_2):
        print "Invalid choice! Try again!"
        slot_2 = int(raw_input("Slot 2 Position Number: > "))
    board[slot_2] = "X"
    for index, each in enumerate(board):
        if(each != "X"):
            board[index] = " "
        else:
            board[index] = "SNH"


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
            if each_slot == "SNH":
                print "its the opponents turn"
                return
        print "you sunk my battleship!"










guess = 4
opponents_board = [
    " ", " ", "M",
    " ", "SNH", "SH",
    " ", "M", " "
]

checkIfHitOrMiss(guess, opponents_board)
