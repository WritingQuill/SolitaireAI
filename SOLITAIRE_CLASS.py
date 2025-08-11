import random
import numpy as np
class SOLITAIRE:
    def __init__(self):
        #self.name = name
        self.already_assigned_cards = []
        self.playing_field = self.generate_playingfield()
        self.hidden_pile = self.generate_hidden_pile() #Ziehstapel
        self.draw_pile_with_assigned_cards = [] #Ablagestapel
        self.drawn_card= 0
        self.foundation = {} #Endstapel
        self.cards = self.generate_cards()
        #print(self.cards)
    
    def generate_playingfield(self):
        playing_field = np.zeros((13, 7), dtype=object)
        for j in range(7):
            random_number = random.randint(1, 52)
            while random_number in self.already_assigned_cards:
                random_number = random.randint(1, 52)
            playing_field[j][j] = random_number
            self.already_assigned_cards.append(random_number)
    
        for i in range(13):
            for j in range(7):
                if j> i:
                    playing_field[i][j] = "x"

        return playing_field   
    
    def generate_cards(self):   
        cards = {}
        for i in range(1,14):
            cards[i] = ["Hearts",i]
        for i in range(14,27):
            cards[i] = ["Diamonds",i-13]
        for i in range(27,40):
            cards[i] = ["Clubs",i-26]
        for i in range(40,53):
            cards[i] = ["Spades",i-39]
        return cards

    def generate_hidden_pile(self):
        hidden_pile = []
        for i in range(24):   
            random_number = random.randint(1,52)
            while random_number in self.already_assigned_cards:
                random_number = random.randint(1, 52)
            self.already_assigned_cards.append(random_number)   
            hidden_pile.append(random_number)
        return hidden_pile
    
    def click_on_draw_pile(self):
        if self.drawn_card == 0:
            drawn_card = self.hidden_pile[0]
        else: 
            index_hidden_pile = self.hidden_pile.index(self.drawn_card)
            try:
                drawn_card = self.hidden_pile[index_hidden_pile + 1]
            except IndexError:
                drawn_card = self.hidden_pile[0]
        self.drawn_card = drawn_card
        return 

    def move_drawn_card_to_position(self,j):
        previous_card = 0
        index = 0
        for i in range(13):
            if self.playing_field[i][j] != "x" and self.playing_field[i][j]!= 0:
                previous_card  = self.playing_field[i][j]
                index = i
        #CHECK FUNCTION!!!!!
        self.playing_field[index+1][j] = self.drawn_card
        self.drawn_card = 0
        return

    def select_cards_from_playing_field(self,i, j):   
        selected_cards = []
        while i in range(13-i):
            if self.playing_field[i][j] != 0:
                selected_cards.append(self.playing_field[i][j])
                if self.playing_field[i][j] != "x":
                    self.playing_field[i][j] = 0
        selected_cards = [item for item in selected_cards if item != "x"]
        return selected_cards
    
    def move_selected_cards_on_playing_field(self,selected_cards, j):
        index = 0
        for i in range(13):
            if self.playing_field[i][j] != 0:
                index = i
                #CHECK FUNCTION!!!!!
        previous_card = self.playing_field[index-1][j]
        selected_card = selected_cards[0]
        if self.check_move(previous_card, selected_card):
            for card in selected_cards:
                self.playing_field[index][j] = card
                index += 1
        else:
            print("Invalid move")
        return




    def check_move(self, previous_card, drawn_card):
        

        return
        
Test = SOLITAIRE()