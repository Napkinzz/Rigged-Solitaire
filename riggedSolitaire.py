#----------------------------------------------------
# Assignment 3: Rigged Solitaire
# 
# Author: LUKAS WASCHUK 
# Collaborators/References:
#----------------------------------------------------

class CardNode:
    VALID_SUITS = ['D', 'S', 'H', 'C']
    VALID_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    
    # DO NOT CHANGE __init__ method
    def __init__(self, rank, suit, faceUp = True):
        '''
        Initializes a doubly linked list node that stores information about a card. 
        Cards have a suit and rank, and may be face up or down. Asserts that the provided
        suit and rank are valid.

        Input:
          - rank (string): represents number 2-10, Jack, Queen, King, Ace
          - suit (string): represents spade, heart, diamond, or club
          - faceUp (Boolean): represents whether the card is face up (True) or face down (False)

        Returns: None
        '''        
        assert type(rank) == str, "Rank must be a string"
        assert type(suit) == str, "Suit must be a string"
        assert type(faceUp) == bool, "Visible must be boolean"
        
        assert len(suit) == 1, 'Suit must be a single character'
        assert len(rank) == 1, 'Rank must be a single character'
        
        suit = suit.upper()
        rank = rank.upper()
        assert (suit in CardNode.VALID_SUITS), "Invalid Suit provided: {}.".format(suit)
        assert (rank in CardNode.VALID_RANKS), "Invalid Rank provided: {}.".format(rank)
        
        self.__rank = rank
        self.__suit = suit
        self.__faceUp = faceUp
        self.__next = None
        self.__previous = None
    
    # DO NOT CHANGE getRank method   
    def getRank(self):
        '''Returns the rank of the card. No input.'''
        return self.__rank
    
    # DO NOT CHANGE getSuit method
    def getSuit(self):
        '''Returns the suit of the card. No input.'''
        return self.__suit
    
    # DO NOT CHANGE isFaceUp method
    def isFaceUp(self):
        '''Returns whether the card is face up (True) or down (False). No input.'''
        return self.__faceUp
    
    # DO NOT CHANGE turnOver method
    def turnOver(self):
        '''
        Changes the card from face up to face down, or from face down to face up.
        Input: N/A  
        Returns: None.
        '''
        self.__faceUp = not(self.__faceUp)
      
    # DO NOT CHANGE getNext method    
    def getNext(self):
        '''Returns the reference to whatever is next (either None or a CardNode). No input.'''
        return self.__next
    
    # DO NOT CHANGE setNext method
    def setNext(self, newNext):
        '''
        Updates the next reference.
        Input: newNext (None or a CardNode) - the object that will come next
        Returns: None
        '''        
        assert (isinstance(newNext, CardNode) or newNext==None),\
               'Cannot set next to {}'.format(type(newNext))
        self.__next = newNext
    
    # DO NOT CHANGE getPrevious method    
    def getPrevious(self):
        '''Returns the reference to whatever is previous (either None or a CardNode). No input.'''
        return self.__previous
    
    # DO NOT CHANGE setPrevious method
    def setPrevious(self, newPrevious):
        '''
        Updates the previous reference.
        Input: newPrevious (None or a CardNode) - the object that will come previous
        Returns: None
        '''          
        assert (isinstance(newPrevious, CardNode) or newPrevious == None),\
               'Cannot set next to {}'.format(type(newPrevious))
        self.__previous = newPrevious      
    
    
    def __lt__(self, anotherCardNode):
        '''
        Checks if the rank / suit of a card is less then the rank / suit of another card 

        Inputs:
                anotherCardNode(card): the card to compare against 
        
        Returns:
                bool: True: if x < y (where x and y are cards )
                      False: if x !< y or x == y (where x and y are cards )
        '''
        ranks = ["A", '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', "Q", "K"]
        suits = ["D", "S", "H", "C"] 

        #changing the str ranks / suits of a card to a integer form or ranks (by index) to compare against
        cardRank, anotherCardRank = ranks.index(self.getRank()), ranks.index(anotherCardNode.getRank())
        cardSuit, anotherCardSuit = suits.index(self.getSuit()), suits.index(anotherCardNode.getSuit())

        if cardRank < anotherCardRank:
            return True 

        elif cardRank == anotherCardRank:
            if cardSuit < anotherCardSuit:
                return True 
            else:
                return False
        else:
            return False 
    
    def __gt__(self, anotherCardNode):
        '''
        Checks if the rank / suit of a card is greater then the rank / suit of another card 

        Inputs:
                anotherCardNode(card): the card to compare against 
        
        Returns:
                bool: True: if x > y (where x and y are cards )
                      False: if x !> y or x == y (where x and y are cards )
        '''
        ranks = ["A", '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', "Q", "K"]
        suits = ["D", "S", "H", "C"] 

        #changing the str ranks / suits of a card to a integer form or ranks (by index) to compare against
        cardRank, anotherCardRank = ranks.index(self.getRank()), ranks.index(anotherCardNode.getRank())
        cardSuit, anotherCardSuit = suits.index(self.getSuit()), suits.index(anotherCardNode.getSuit())

        if cardRank > anotherCardRank:
            return True 

        elif cardRank == anotherCardRank:
            if cardSuit > anotherCardSuit:
                return True 
            else:
                return False
        else:
            return False 
    
    def isPreviousRank(self, anotherCardNode):
        '''
        Returns true if the card is exactly one rank less then another card. i.e is queen one less then king = True 

        Inputs:
                anotherCardNode(card): the card to be compared against 
        
        Returns:
                bool: True: if the cards is exactly one less rank then the card we compare against
                      False: if the rank is more then one less, or rank is more, or rank is equal
        '''
        ranks = ["A", '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', "Q", "K"]

        # changing the ranks to a integer to compare against 
        cardRank, anotherCardRank = ranks.index(self.getRank()), ranks.index(anotherCardNode.getRank())

        if anotherCardRank != 0 and cardRank == anotherCardRank-1: #is anotherCardRank is 0 we know its a ace and nothing is smaller then an ace.
            return True 
        else:
            return False 
        
    
    # DO NOT CHANGE __str__ method         
    def __str__(self):
        '''
        If face up, a string showing the rank and suit of the card will be returned.
        If face down, a string showing the back of the card will be returned.
        Input: N/A
        Returns: string representation of the CardNode
        '''
        s = '['
        if self.__faceUp:
            s += ' ' + self.__rank + self.__suit
        s += ' ]'
        return s


class CardList():
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the CardList, which is very similar to a Doubly Linked List.
        A CardList can only have CardNodes and None in its sequence.
        Input: N/A
        Returns: None
        '''
        self.__head = None  # do not change
        self.__tail = None  # do not change
        self.__size = 0     # do not change
    
    # DO NOT CHANGE getHead method     
    def getHead(self):
        '''Returns head of list (either a CardNode or None). No input.'''
        return self.__head
    
    # DO NOT CHANGE getTail method
    def getTail(self):
        '''Returns tail of list (either a CardNode or None). No input.'''
        return self.__tail
    
    # DO NOT CHANGE getSize method
    def getSize(self):
        '''Returns number of CardNodes in sequence. No input.'''
        return self.__size    
    
    # DO NOT CHANGE add method
    def add(self, cardNode):
        '''
        Adds a CardNode to the beginning (head) of the CardList and updates the size.
        Notice the similarity between this and the Doubly Linked List add method.
        Input: cardNode (must be a CardNode)
        Returns: None
        '''
        temp = cardNode
        temp.setPrevious(None) #make sure node is on its own
        temp.setNext(None)     #make sure node is on its own   
        temp.setNext(self.__head)
        if self.__head != None:  # there is a head
            self.__head.setPrevious(temp)
        else:                    # adding to empty list
            self.__tail=temp
        self.__head = temp
        self.__size += 1

    # DO NOT CHANGE append method
    def append(self, cardNode):
        '''
        Appends a CardNode to the end (tail) of the CardList and updates the size.
        Notice the similarity between this and the Doubly Linked List append method.
        Input: cardNode (must be a CardNode)
        Returns: None
        '''        
        temp = cardNode
        temp.setPrevious(None) #make sure node is on its own
        temp.setNext(None)     #make sure node is on its own
        if (self.__head == None):
            self.__head=temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail=temp
        self.__size +=1  
    
     
    def pop(self):
        '''
        Removes the last card from the cardlist and returns it 

        Inputs:
                None 

        Returns:
                data(card) = the last card of the deck 
        '''
        assert self.__size > 0, 'NOTHING IN DECK' #just incase its called then the deck is empty 

        if self.__size == 1: #for when there is only one item in the card list
            data = self.__tail
            self.__tail = None #changing head and tail to None i.e empty linked list 
            self.__head = None 
           
            data.setPrevious(None) #removing any links from data (the node)
            data.setNext(None)
            self.__size -= 1
            return data 
        else:
            data = self.__tail
            previous = self.__tail.getPrevious()
            #making the previous card the new tail of the card list 
            self.__tail = previous
            previous.setNext(None)

            # removing the last card of the cardlist (by setting its previous to None )
            data.setPrevious(None)
            # updating the size of the cardlist 
            self.__size -= 1
            return data 


    def sort(self):
        '''
        Sorts a deck of cards by the rank / suit 

        Inputs:
                None

        Returns: 
                None 
        ''' 
        current = self.__head
        sortedPointer = self.__head
        if self.__head == None or self.__size == 1:
            return  
        
        if self.__size == 2:
            if current > current.getNext():
                self.swap(current, current.getNext())
            return 
        
        while current.getNext() != None:
            if current and  current > current.getNext(): # will not call current.getnext() as the swap method will move the self.head over by 1 space 
                self.swap(current, current.getNext())
                sortedPointer = current.getPrevious() #resets the sorted pointer every iteration

            else: # if it doesnt go into the 'if' statement we move the head over by one 
                current = current.getNext()

            while sortedPointer.getPrevious() != None:     #checks everything on the sorted side of the linked list (everything to the left of sorted pointer till it hits None)
                if sortedPointer.getPrevious() > sortedPointer: # will not call sortedPointer.getPrevious() as the swap method will move the sorted pointer back by 1 space
                    self.swap(sortedPointer.getPrevious(), sortedPointer)
                else:# if it doesnt go into the 'if' statement we move the head of the sorted pointer back by one 
                    sortedPointer = sortedPointer.getPrevious()
        return 

 

    def swap(self, swap1, swap2):
        '''
        A sub-method to be called by the sort function to swap the places of two adjacent nodes in the cardlist(). the order of the input does not matter as they are adjacent so no matter 
        the order they will end up in the same spots. have to add mroe inputs then just self becuase it is used for a pointer other than self.__head 
        sortedPointer uses this method to swap things in the sorted side of the cardList

        Inputs:
                swap1(card): the first card
                swap2(card): the second card 

        Returns:
                None, as the Dlinked list (cardlsit) is updated and not created into a new Cardlist() instance 

        '''

        #CASE 1 ONLY 2 CARDS 
        if self.__size == 2:
            swap1.setNext(None)
            swap1.setPrevious(swap2)

            swap2.setNext(swap1)
            swap2.setPrevious(None)

            self.__head = swap2
            return 


        # CASE 2 SWAPPING THE HEAD 
        if swap1.getPrevious() == None:
            temp = swap2.getNext()

            swap1.setPrevious(swap2)
            swap1.setNext(temp)
            temp.setPrevious(swap1)

            swap2.setPrevious(None)
            swap2.setNext(swap1)
          
            self.__head = swap2
            return  
        
        #case 3 SWAPPING THE TAIL 
        if swap2.getNext() == None:

            temp = swap1.getPrevious()

            swap1.setNext(None)
            swap1.setPrevious(swap2)

            swap2.setNext(swap1)
            swap2.setPrevious(temp)
            temp.setNext(swap2)
            self.__tail = swap1
            return 

        # CASE 4 THEY ARE BOTH IN THE MIDDLE 
        else:
            temp1 = swap1.getPrevious() # card before swap1
            temp2 = swap2.getNext() # card after swap2

            swap1.setNext(temp2)
            temp2.setPrevious(swap1)
            swap1.setPrevious(swap2)
            
            swap2.setPrevious(temp1)
            temp1.setNext(swap2)
            swap2.setNext(swap1)
            return



    def __str__(self):
        ''' 
        Returns a string rep of the cardlist 

        Inputs:
                None

        Returns:
                string(str): the string rep of the decklist 
        '''
        current = self.__head
        string = '| '
        while current != None:
            string = string + str(current) + ' '
            current = current.getNext()
        string = string + '|'
        return string


class CardStack():
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the CardStack, which is essentially a linked Stack.
        Input: N/A
        Returns: None
        '''        
        self.__cards = CardList()  # do not change
    
    def push(self, card):
        '''
        Puts a card on the top of a cardstack i.e deck, afdter checking if either the deck is empty or if the previous card is exactly one less
        rank then the cards we are adding in. self.__tail is the top of the deck 

        Inputs:
                card(cardNode): the card we are trying to add to the deck 

        Returns:
                bool: True: if the cards was added 
                      False: if the card was not added 
        ''' 

        if self.__cards.getSize() == 0 or self.__cards.getTail().isPreviousRank(card): 
            self.__cards.append(card)
            return True 
        else:
            return False 

    def pop(self):
        '''
        returns the 'top' card in the deck (the tail of the cardDeck), just using the pop() method we made before 

        Inputs:
                None

        Returns:
                self.__cards.pop()(cardNode): the card removed from the top of the carddeck
        '''
        return self.__cards.pop()
    
    def peak(self):
        '''
        shows the top card in the deck, i.e the tail of the linked list.

        Inputs:
                None

        Returns:
                self.__cards.getTail()(cardNode): the top of the deck
        ''' 
        return self.__cards.getTail() 
    
    def isEmpty(self):
        '''
        checks to see if the card stack is empty 

        Inputs:
                None

        Returns:
                bool:
                        True: if the deck is empty 
                        False: is there is atleast one card in it
        '''
        return self.__cards.getSize() == 0
    
    def __str__(self):
        '''
        Returns the string rep of the top card in the decklist, or "--" if it is empty 

        Inputs:
                None 

        Returns:
                '--'(str): if the deck is empty 
                str(self.__cards.getTail())(str): string rep of the top of the deck if the deck is not empty 
        '''
        if self.__cards.getSize() == 0:
            return "--"
        else:
            return str(self.__cards.getTail() )
    

   
class Table:
    # DO NOT CHANGE __init__ method
    def __init__(self):
        '''
        Initializes the Solitaire table. On the table, we will have 1 deck of cards, 
        1 playing pile, 4 foundation piles, and the 7 columns of cards.
        Input: N/A
        Returns: None
        '''
        NUM_COLUMNS = 7
        self.__deck = CardList()        # do not change
        self.__playingPile = CardList() # do not change
        self.__clubs = CardStack()      # do not change
        self.__hearts = CardStack()     # do not change
        self.__spades = CardStack()     # do not change
        self.__diamonds = CardStack()   # do not change
                
        self.__columns = []
        for col in range(NUM_COLUMNS):
            self.__columns.append(CardList())  # do not change      
     
    # DO NOT CHANGE populateDeck method 
    def populateDeck(self, filename):
        '''
        Adds cards to deck based on information in provided text file. We can assume that if
        we can read from the text file, it contains information for a complete and valid deck.
        Input: filename (str) - name of text file
        Returns: None
        '''
        # Important assumption in this implementation: 
        # the top of the deck is at the tail of our CardList
        
        fin = open(filename, 'r')
        for line in fin:
            cardStr = line.strip()
            self.__deck.add(CardNode(cardStr[0], cardStr[1], False)) 
        fin.close()
    
    def rigGame(self):
        '''
        sorts the deck using the previously created method 

        Inputs: 
                None 

        Returns:
                None 
        '''
        self.__deck.sort()
        
        
    def dealGame(self):
        '''
        Deals the cards to the table, starting with col 0 with 1 card, up to col 6 with 7 cards, and the rightmost card being flipped over 

        Inputs:
                None

        Returns:
                None 
        '''
        
        for i in range(len(self.__columns)):
            for j in range(i, len(self.__columns)):
                self.__columns[j].append(self.__deck.pop())
                
            self.__columns[i].getTail().turnOver()
            
        # #to test it 
        # for i in range(len(self.__columns)):
        #     print(self.__columns[i])


    def drawThree(self):
        '''
        deals three cards from the deck into the playing pile all faced up 

        Inputs:
                None 

        Returns:
                None 
        ''' 
        for i in range(3):
            card = self.__deck.pop()
            card.turnOver()
            self.__playingPile.append(card)          
        print('-------------------------')
        print('Dealing three cards to playing pile...\n')
            

    def playPileToFoundation(self):
        '''
        checks the drop card in the playing pile deck and sees if it can be put into a foundation pile. 
        i.e if the pile is empty the card is a ace, or if it isnt empty checks if the card in the foundation pile is exactly one less then the
        card we want to add. adds the card back to the play pile if it could not be added 

        Inputs:
                None 

        Returns:
                True: if the card was added to a foundation pile 
                False: if the card was not added 
        '''
        playCard = self.__playingPile.pop()
        suit = playCard.getSuit()
        added = False 

        if suit == "D":
            if self.__diamonds.isEmpty() == True:
                if playCard.getRank() == "A":
                    self.__diamonds.push(playCard)
                    added = True
            elif self.__diamonds.push(playCard) == True:
                #self.__diamonds.push(playCard)
                added = True

        elif suit == "S":
            if self.__spades.isEmpty() == True:
                if playCard.getRank() == "A":
                    self.__spades.push(playCard)
                    added = True
            elif self.__spades.push(playCard) == True:
                #self.__spades.push(playCard)
                added = True

        elif suit == "H":
            if self.__hearts.isEmpty() == True:
                if playCard.getRank() == "A":
                    self.__hearts.push(playCard)
                    added = True
            elif self.__hearts.push(playCard) == True:
                #self.__hearts.push(playCard)
                added = True

        elif suit == "C":
            if self.__clubs.isEmpty() == True:
                if playCard.getRank() == "A":
                    self.__clubs.push(playCard)
                    added = True
            elif self.__clubs.push(playCard) == True:
                #self.__clubs.push(playCard)
                added = True

        if added == True:
            print('-------------------------')
            print('Moving {} from playing pile to foundation pile...\n'.format(playCard))
            return True 
        else:

            self.__playingPile.add(playCard)
            return False

    def PPTF_test(self): # playPileToFoundation tests NEEDED PRIV ATTR 
        '''
        the test for play pile to foundation cause we need to use priv attributes to test 

        Inputs:
                None

        Returns:
                None 
        '''
        while self.__playingPile.getSize() != 0:
            self.__playingPile.pop()

        self.__playingPile.add(CardNode("A", "S"))
        self.__playingPile.add(CardNode("A", "H"))
        self.__playingPile.add(CardNode("A", "C"))
        self.__playingPile.add(CardNode("A", "D"))
        self.__playingPile.add(CardNode("2", "D"))
        self.__playingPile.add(CardNode("4", "D"))
        self.__playingPile.add(CardNode("3", "D"))


        print('playing pile', self.__playingPile) 

        print('card added?', self.playPileToFoundation()) #trying 6S
        print('playing pile', self.__playingPile) 
        print('foundation pile for spades', self.__spades)

        print('card added?', self.playPileToFoundation()) #trying AS
        print('playing pile', self.__playingPile) 
        print('foundation pile for spades', self.__spades)

        print('card added?', self.playPileToFoundation()) #trying AH
        print('playing pile', self.__playingPile) 
        print('foundation pile for hearts', self.__hearts)

        print('card added?', self.playPileToFoundation()) #trying AC
        print('playing pile', self.__playingPile) 
        print('foundation pile for clubs', self.__clubs)

        print('card added?', self.playPileToFoundation()) #trying AD
        print('playing pile', self.__playingPile) 
        print('foundation pile for daimonds', self.__diamonds)


        print('card added?', self.playPileToFoundation()) #trying 2D TRUE 
        print('playing pile', self.__playingPile) 
        print('foundation pile for daimonds', self.__diamonds)

        print('card added?', self.playPileToFoundation()) #trying 4D FALSE
        print('playing pile', self.__playingPile)  
        print('foundation pile for daimonds', self.__diamonds)

        print('card added?', self.playPileToFoundation()) #trying 3D True
        print('playing pile', self.__playingPile) 
        print('foundation pile for daimonds', self.__diamonds)


    def columnToFoundation(self, fromIndex):
        playCard = self.__columns[fromIndex].pop()
        suit = playCard.getSuit()
        added = False

        if suit == "D":
            if self.__diamonds.isEmpty() == True:
                if playCard.getRank() == "A":
                    self.__diamonds.push(playCard)
                    added = True 
            elif self.__diamonds.push(playCard) == True:
                #self.__diamonds.push(playCard)
                added = True 

        elif suit == "S":
            if self.__spades.isEmpty() == True:
                if playCard.getRank() == "A":
                    self.__spades.push(playCard)
                    added = True 
            elif self.__spades.push(playCard) == True:
                #self.__spades.push(playCard)
                added = True 

        elif suit == "H":
            if self.__hearts.isEmpty() == True:
                if playCard.getRank() == "A":
                    self.__hearts.push(playCard)
                    added = True 
            elif self.__hearts.push(playCard) == True:
                #self.__hearts.push(playCard)
                added = True 

        elif suit == "C":
            if self.__clubs.isEmpty() == True:
                if playCard.getRank() == "A":
                    self.__clubs.push(playCard)
                    added = True 
            elif self.__clubs.push(playCard) == True:
                #self.__clubs.push(playCard)
                added = True 
        
        if added == True:
            if self.__columns[fromIndex].getTail() != None:
                self.__columns[fromIndex].getTail().turnOver()
            print('-------------------------')
            print('Moving {} from column {} to foundation pile...\n'.format(playCard, fromIndex))
            return True 
        else:
            self.__columns[fromIndex].append(playCard)
            return False

    def CTF_test(self, fromIndex): # columnToFoundation tests, NEED PRIVATE ATTR
        '''
        column to foundation testing. I did the testing here so i can make appropiate settings to actually try out the methods.
        I needed to use the private attributes

        Inputs:
                None 

        Returns:
                None
        '''
        print('foundation pile for daimonds', self.__diamonds)
        ranks = ["A", '2', '3', '4', '5', '6']

        #filling the decks a little bit
        for rank in ranks: 
            self.__diamonds.push(CardNode(rank, "D"))

        for rank in ranks:
            self.__spades.push(CardNode(rank, "S"))

        for rank in ranks:
            self.__clubs.push(CardNode(rank, "C"))

        for rank in ranks:
            self.__hearts.push(CardNode(rank, "H"))
        self.__hearts.push(CardNode('7', "H"))
       

        print('column deck', self.__columns[fromIndex]) #TRYING 7D 
        print('was the rightmost card added?', self.columnToFoundation(6))
        print('foundation pile for daimonds', self.__diamonds)
        print('column deck', self.__columns[fromIndex])

        print('column deck', self.__columns[fromIndex]) # TRYING 7S
        print('was the rightmost card added?', self.columnToFoundation(6))
        print('foundation pile for spades', self.__spades)
        print('column deck', self.__columns[fromIndex])

        print('column deck', self.__columns[fromIndex]) #TRYING 7C
        print('was the rightmost card added?', self.columnToFoundation(6))
        print('foundation pile for clubs', self.__clubs)
        print('column deck', self.__columns[fromIndex])

        print('column deck', self.__columns[fromIndex]) #trying 8h
        print('was the rightmost card added?', self.columnToFoundation(6))
        print('foundation pile for hearts ', self.__hearts)
        print('column deck', self.__columns[fromIndex])

        print('column deck', self.__columns[fromIndex]) #trying 9h 
        print('was the rightmost card added?', self.columnToFoundation(6))
        print('foundation pile for hearts ', self.__hearts)
        print('column deck', self.__columns[fromIndex])

        print('column deck', self.__columns[fromIndex]) #trying TC, checking to see what happens when its not added 
        print('was the rightmost card added?', self.columnToFoundation(6))
        print('column deck', self.__columns[fromIndex])

    def displayTable(self):
        '''
        Prints the "game UI" 

        Inputs:
                None

        Returns:
                None 
        '''
        print("Foundation Piles:")
        print('{}, {}, {}, {}'.format(self.__clubs, self.__hearts, self.__spades, self.__diamonds))

        print('\nBoard:')
        
        for i in range(len(self.__columns)):
            
            if self.__columns[i].getSize() == 0: # to add the double space on the empty column like the sample has 
                print('Column {}: {}'.format(i, '|  |'))
            else:
                print('Column {}: {}'.format(i, self.__columns[i]))

        if self.__playingPile.getTail() == None:
            print('\nPlaying Cards:\n{}\n'.format("--"))
        else:
            print('\nPlaying Cards:\n{}\n'.format(self.__playingPile.getTail()))
        
    def gameWon(self):
        '''
        Checks if the game is actually over, i.e there is a winner. i checked it by 
        looking at the top card in each of the foundation piles and if all 4 are 
        kings the game MUST be over (because of the push() method checking for exactly 
        one rank lower in the pile before it adds a card). )
        
        Inputs:
                None 

        Returns:
                bool:
                    True: if the game is won, i.e all the cards are in there foundation piles 
                    False: if the game isnt over yet, i.e more cards to put in foundation piles 
        '''
        if (str(self.__diamonds.peak()) == '[ KD ]' and
           str(self.__clubs.peak()) == '[ KC ]' and
           str(self.__spades.peak()) == '[ KS ]' and
           str(self.__hearts.peak())== '[ KH ]'):
           return True
        else:
            return False 

    def GW_test(self):
        '''
        tests for the GAME WON method. had to make here so i can create FULL foundation piles 
        using the private attributes 

        Inputs:
                None 

        Returns:
                None
        '''
        ranks = ["A", '2', '3', '4', '5', '6', '7', '8', '9', "T", "J", "Q", "K"]

        for rank in ranks:
            self.__diamonds.push(CardNode(rank, "D"))

        for rank in ranks:
            self.__spades.push(CardNode(rank, "S"))

        for rank in ranks:
            self.__clubs.push(CardNode(rank, "C"))

        for rank in ranks:
            self.__hearts.push(CardNode(rank, "H"))
        
        print('FULL FOUNDATION PILE! IS IT  A WINNER?', self.gameWon()) #testing a game that is a winner -----------TRUE 

        self.__hearts.pop()
        print('NOT FULL FOUNDATION PILE! IS IT  A WINNER?', self.gameWon()) #testing a game that is not a winner --------- FALSE 
        


################################
## Functions to Test classes  ##
################################
def testCardNode():
    card1 = CardNode('A', 'h')
    print(card1)
    # write additional tests here

    ######################## LESS THAN TESTS #####################################
    '''
    # rank less then (same suit) comparing AH < 5H returns true
    card2 = CardNode('5', 'h')
    print(card2)
    print(card1 < card2)
    '''

    '''
    # rank greater then (same suit) COMPARING 5H < AH returns false 
    card2 = CardNode('5', 'h')
    print(card2)
    print(card2 < card1)
    '''

    '''
    #rank the same SUIT less then COMPARING AH < AS RETURNS FALSE 
    card2 = CardNode('A', 's')
    print(card2)
    print(card1 < card2)
    '''
    
    '''
    #rank the same SUIT less then COMPARING AS < AH RETURNS TRUE 
    card2 = CardNode('A', 's')
    print(card2)
    print(card2 < card1)
    '''

    '''
    # comparing to itself WILL RETURN FALSE 
    print(card1 < card1)
    '''

    '''
    #comparing different ranks/ suits AH < 7D  RETURNS TRUE  
    card2 = CardNode('7', 'D')
    print(card2)
    print(card1 < card2)
    '''

#################### GREATER THAN TESTS ###############################################
    '''
    # rank greater then (same suit) comparing AH > 5H returns FALSE 
    card2 = CardNode('5', 'h')
    print(card2)
    print(card1 > card2)
    '''

    '''
    # rank greater then (same suit) COMPARING 5H > AH returns false 
    card2 = CardNode('5', 'h')
    print(card2)
    print(card2 > card1)
    '''

    '''
    #rank the same SUIT greater then COMPARING AH > AS RETURNS TRUE  
    card2 = CardNode('A', 's')
    print(card2)
    print(card1 > card2)
    '''
    
    '''
    #rank the same SUIT greater then COMPARING AS > AH RETURNS FALSE  
    card2 = CardNode('A', 's')
    print(card2)
    print(card2 > card1)
    '''

    '''
    # comparing to itself WILL RETURN FALSE 
    print(card1 < card1)
    '''

    '''
    #comparing different ranks/ suits AH > 7D  RETURNS FALSE 
    card2 = CardNode('7', 'D')
    print(card2)
    print(card1 > card2)
    '''

########################## PREVIOUS RANK TESTING #####################################
    '''
    # comparing  is K one less then Q
    card2 = CardNode("K", "H")
    card3 = CardNode("Q", "D")
    print('is {} one less then {}?'.format(card2, card3), end = ' ')
    print(card2.isPreviousRank(card3))
    '''

    '''
    # comparing is Q one less then K 
    card2 = CardNode("Q", "H")
    card3 = CardNode("K", "D")
    print('is {} one rank less then {}?'.format(card2, card3), end = ' ')
    print(card2.isPreviousRank(card3))
    '''

    '''
    # comaring 7 6 
    card2 = CardNode("7", "D")
    card3 = CardNode("6", "S")
    print('is {} one rank less then {}?'.format(card2, card3), end = ' ')
    print(card2.isPreviousRank(card3))
    '''

    '''
    # comaring 6 7 
    card2 = CardNode("6", "D")
    card3 = CardNode("7", "S")
    print('is {} one rank less then {}?'.format(card2, card3), end = ' ')
    print(card2.isPreviousRank(card3))
    '''

    '''
    #comparing A 9 
    card2 = CardNode("A", "D")
    card3 = CardNode("9", "S")
    print('is {} one rank less then {}?'.format(card2, card3), end = ' ')
    print(card2.isPreviousRank(card3))
    '''

    '''
    # comaring 2 A
    card2 = CardNode("2", "D")
    card3 = CardNode("A", "S")
    print('is {} one rank less then {}?'.format(card2, card3), end = ' ')
    print(card2.isPreviousRank(card3))
    '''

    '''
    # comaring A 2 
    card2 = CardNode("A", "D")
    card3 = CardNode("2", "S")
    print('is {} one rank less then {}?'.format(card2, card3), end = ' ')
    print(card2.isPreviousRank(card3))
    '''

def testCardList():
    card1 = CardNode('A', 'h')   
    deck = CardList()
    deck.add(card1)
    
    # write additional tests here
    ############################# TESTING POP() METHOD ########################################
    '''
    # testing the POP method on more then 1 card
    #adding more cards to the deck 
    card2 = CardNode('K', 'S') 
    card3 = CardNode('6', 'C') 
    deck.add(card2)
    deck.add(card3)

    print('size before pop {}'.format(deck.getSize()))
    removedCard = deck.pop()
    print(removedCard)
    print('size after pop {}'.format(deck.getSize()))
    '''

    '''
    #testing pop on just one card 
    print('size before pop {}'.format(deck.getSize()))
    removedCard = deck.pop()
    print(removedCard)
    print('size after pop {}'.format(deck.getSize()))
    '''

    '''
    #testing pop on empty deck WILL RETURN ASSERTION ERROR AS DECK IS EMPTY 
    deck1 = CardList()
    print('size before pop {}'.format(deck.getSize()))
    removedCard = deck1.pop()
    print(removedCard)
    print('size after pop {}'.format(deck.getSize()))
    '''

    ############################# TESTING SORT() METHOD ##############################################
    '''
    #adding more cards to the deck 
    card2 = CardNode('K', 'S') 
    card3 = CardNode('6', 'C') 
    card4 = CardNode('7', 'D') 
    card5 = CardNode('A', 'S') 
    card6 = CardNode('9', 'H') 
    card7 = CardNode('9', 'C') 
    card8 = CardNode('K', 'H') 
    card9 = CardNode('4', 'D') 
    card10 = CardNode('A', 'D') 
    deck.add(card2)
    deck.add(card3)
    deck.add(card4)
    deck.add(card5)
    deck.add(card6)
    deck.add(card7)
    deck.add(card8)
    deck.add(card9)
    deck.add(card10)

    print("UNSORTED DECK:")
    print(deck)

    deck.sort()
    print("SORTED DECK:")
    print(deck)
    ''' 


    ##############################TESTING STR METHOD ###########################################
    '''
    print('deck with just one card in it')
    print(deck)

    #adding more cards to the deck 
    card2 = CardNode('K', 'S') 
    card3 = CardNode('6', 'C') 
    deck.add(card2)
    deck.add(card3)
    print('after adding two more cards.')
    print(deck)

    #empty deck 
    deck2 = CardList()
    print('empty deck')
    print(deck2)
    '''

def testCardStack():
    stack = CardStack()
    card1 = CardNode('A', 'h')
    stack.push(card1)
    # write additional tests here
    ############################# TESTING PUSH() ##############################
    '''
    #adding cards 
    card2 = CardNode('2', 'h')
    card3 = CardNode('3', 'h')
    card4 = CardNode('4', 'd')
    card5 = CardNode('8', 's')
    card6 = CardNode('5', 'c')
    
    stack.push(card2) #true 
    stack.push(card3) #true 
    stack.push(card4) #true 
    stack.push(card5) #False 
    stack.push(card6) #true 
    '''

    ############################### TESTING POP() #############################################
    '''
    popCard = stack.pop() # should be card 6
    print(popCard, 'was removed from the deck') # card 6 was returned 
    '''

    ################################ TESTING PEAK() #########################################
    '''
    print('the top card in the deck is:', stack.peak()) #peaking 
    print(stack.pop(), 'was removed from the deck') #removing another card from the deck 
    print('the top card in the deck is:', stack.peak()) # checking if peak updated 
    '''

    #################################### TESTING ISEMPTY() ###############################
    '''
    print('is the deck empty?', stack.isEmpty()) # returns false as there is one card in the deck 
    print(stack.pop(), 'was removed from the deck') # removing the card 
    print('is the deck empty?', stack.isEmpty()) #checking again, returns true 
    
    card2 = CardNode('2', 'h')
    stack.push(card2) # adding a card back into the deck 
    print('is the deck empty?', stack.isEmpty()) # not empty anymore returns false 
    ''' 

    ################################# TESTING STR() ######################################
    '''
    print(stack) # one card in the deck returns str(card)
    print(stack.pop(), 'was removed from the deck') # removing the card
    print(stack) #nothing in the deck returns -- 

    card2 = CardNode('2', 'h')
    card3 = CardNode('3', 'h')
    stack.push(card2)  
    stack.push(card3) # adding thigns back into the deck 
    print(stack) # returns card3 in string form 
    '''


def testTable():
    table = Table()
    # write tests here
    ######################### TESTING POPULATE DECK() ####################################
    '''
    table.populateDeck('startDeck.txt')
    '''

    ############################## TESTING RIGGAME() ################################
    '''
    # to test these populate and rig method i changed the "flipped" boolean in the populate from true to false and printed the decks to 
    # confirm that everything imported properly and that the sort() method sorted everything correctly
    table.rigGame()
    '''

    ################## TESTING DEALGAME() ###################################
    '''
    # cant really show how i tested becuase to show the columns you need to be in the method as everything is private. 
    # i checked every column by calling self.__columns[0] - self.__columns[6] to make sure everything was good. 
    # i deleted those tests as they were in the middle of the method and it was ugly 
    table.dealGame()
    ''' 

    ################# TESTING DRAWTHREE() ###########################################################
    '''
    # again the same problem with the private attributes, cant test out here but i printed the self.__playingPile inside the method to confirm it is working 
    table.drawThree()
    '''

    ##################### TESTING PLAYPILETOFOUNDATION() ###############################
    '''
    # i created another method in the class to actually test this method to make sure all the logic was working found under PPTF_test()
    table.playPileToFoundation()
    table.PPTF_test()
    '''

    ################### TESTING COLUMN TO FOUNDATION () #################################
    '''
    # i created another method in the class to actually test this method to make sure all the logic was working found under CTF_test()
    table.columnToFoundation(6)
    table.CTF_test(6)
    '''

    ########################## TESTING DISPLAYTABLE() ####################################
    '''
    table.displayTable()
    '''
    ############################## TESTING GAME WON() ###################################
    '''
    table.GW_test()
    '''

if __name__ == '__main__':
    # comment/uncomment tests as required.  You may add more tests in any format.
    
    #testCardNode()
    #testCardList()
    #testCardStack()
    #testTable()
    pass
	