import random
import numpy as np
class SOLITAIRE:
    def __init__(self):
        #self.name = name
        self.already_assigned_cards = []
        self.playing_field = self.generate_playingfield()
        print(self.playing_field)
    
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
    

Test = SOLITAIRE()