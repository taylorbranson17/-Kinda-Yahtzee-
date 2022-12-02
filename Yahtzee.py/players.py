from scorecard import Scorecard
from hand import Hand

class Player:

    def __init__(self, name: str):
        self.name = name 
        self.h = Hand()
        self.hand = self.h.hand
        self.s = Scorecard()
        self.scorecard = self.s.scorecard
        self.score = 0

    def _take_score(self, score:tuple):
        """Takes a dicitonary of chosen scoring option, and adds it to the player's scorecard."""
        self.scorecard[score[0]] = score[1]
        print(f'You\'ve chosen to take {score[1]} in the category {score[0]}.')
    
    def take_turn(self):
        """Simulates one full turn in the game of Yahtzee."""
        print(f'\n{self.name}\'s Turn!')
        self.display_current_scorecard()
        self.h.yahtzee_roll()
        self.h.re_roll()
        score = self.s.choose_score(self.hand)
        self._take_score(score)
        print('Your turn is complete, pass me along to the next player!')
    
    def display_current_scorecard(self):
        print('Here\'s your current scorecard...')
        temp_scorecard = self.scorecard.copy()
        temp_score = self._p_adjust_scorecard(temp_scorecard)
        self.s.display_scorecard(temp_score)

    def _p_adjust_scorecard(self, scorecard: dict):
        temp_scorecard = scorecard.copy()
        for k,v in scorecard.items():
            if v == '':
                temp_scorecard[k] = 0
            else:
                temp_scorecard[k] = v
        return temp_scorecard

    def display_final(self):
        self.score = self.s.display_final_scorecard(self.name)

    def __str__(self):
        return self.name