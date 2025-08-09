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
                    playing_field[i][j] = "U"

        return playing_field   
    
        
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

Test = SOLITAIRE()