#----------------------------------------------------
# Assignment 3: ASSIGNEMENT3.PY
# 
# Author: LUKAS WASCHUK 
# Collaborators/References:
#----------------------------------------------------
from riggedSolitaire import Table 

def main():
    '''
    the main function for assignment 3 that stiches everything together, sets up the table class
    rigs the decks, and deals the game, will deal 3 cards to the play pile until the deck is empty, 
    then will compare every card in the play pile against the "foundation" piles moving every card from 
    the play pile to the foundation pile (thats how the assignement was designed). 

    Then iterates through columns 0 - 6 until there is no cards left in them and prints the outcome of the game! 

    Inputs:
            None 

    Returns:
            None 
    '''
    table = Table()
    welcomeBanner()

    badFN = True
    while badFN: #checking for OSError 
        try:
            table.populateDeck(getFileName())
            badFN = False
        except OSError:
            print('Invalid file name, please try again.')
    
    # rig the game and deal the cards out 
    table.rigGame()
    table.dealGame()

    #deal the cards to the playing pile 
    table.displayTable()
    
    # deal all of the cards out of the main deck into the playPile 
    deal_three = True
    while deal_three:
        try:
            table.drawThree() # this is what will cause the assertion error when the deck is empty 
            table.displayTable()
        except AssertionError: #asserts when the deck is empty i.e all the cards are dealt 
            deal_three = False

    play = True
    while play:
        try:
            table.playPileToFoundation() #this is what will cause the assertion error when the deck is empty 
            table.displayTable()
        except AssertionError: # ASSERTS IF THE DECK IS EMPTY (all the cards atre dealt)
            play = False


    # while the game doesnt have a winner, keep iterating through columns 0 - 6 checking every card at the top of those decks 
    # against the 4 foundation piles
    while table.gameWon() == False:
        for index in range(7): # range of the columns (only hardcoded because the playing board of solitare never changes i.e always 7 columns)
            if table.columnToFoundation(index) == True: #if the card actually was moved 
                table.displayTable() 
                if table.gameWon(): # after every card is added to the foundation pile we check if the game is done, 
                    print('-------------------------')
                    print('WINNER!\nThanks for playing. Goodbye...')
                    return 

def getFileName():
    '''
    gets the user input for the file name 

    Inputs:
            None
    
    Returns:
            fileName(str): the file name the user entered
    '''
    fileName = input('Please enter the file you wish to use to initialize your deck: ')
    return fileName

def welcomeBanner():
    '''
    welcome banner for the game, only printed 1x when the game starts 

    Inputs:
            None

    Returns:
            None
    '''
    print('******************')
    print('Klondike Solitaire')
    print('******************')

if __name__ == '__main__':
    main()