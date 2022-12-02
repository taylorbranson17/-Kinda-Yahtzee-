import scoring_utilities as su

class Scorecard:
    """A class for all things scorecard."""

    def __init__(self):
        self.scorecard = {}
        self.keys_in_order = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Three of a Kind', 'Four of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Chance', 'Yahtzee', 'Bonus']
        self.scoring_keys = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Three of a Kind', 'Four of a Kind', 'Full House', 'Small Straight', 'Large Straight', 'Chance', 'Yahtzee']
        for key in self.scoring_keys:
            self.scorecard.setdefault(key, '')
        self.scorecard['Bonus'] = 0
    
    def _check_bonus(self, poss_scores: list):
        """Takes a dict of scoring options, and evaluates them against the users scorecard for a bonus Yahtzee."""
        # If 'yahtzee' is in score options.
        for item in poss_scores:
            if item[0] == 'Yahtzee' and item[1] != 0:
                # If 'yahtzee' already has a score in user's scorecard.
                if self.scorecard['Yahtzee'] == 50:
                    self.scorecard['Bonus'] += 100
                    print('Bonus Yahtzee! Your points have been saved, please choose another category to score.')
            
    def _check_score(self, hand: list):
        """Takes a user's hand, and returns a dictionary of possible scoring options."""
        poss_scores = []
        for category in self.scoring_keys:
            poss_scores.append((category,su.score_for_category(category, hand)))
        return poss_scores
    
    def choose_score(self, hand: list):
        """Shows user list of possible scoring options from <hand>, and asks them to choose one to add to their scorecard."""
        # Returns dict with all possible scoring options in {category:score, ...} format.
        poss_scores = self._check_score(hand) #--> List
        
        # Presents options to user.
        print('Here are the categories in which you can score....')
        self._check_bonus(poss_scores)

        # Remove any previously scored options from the available ones.
        for item in poss_scores.copy():
            if self.scorecard[item[0]] != '':
                poss_scores.remove(item)

        count = 1
        for item in poss_scores:
            # Makes sure user's score is default in scorecard. Will only print if no score's been taken previously.
            if self.scorecard[item[0]]  == '':
                print(f'{count:2}) {item[0]:20} {item[1]:>10}')
            else:
                pass
            count += 1

        # Asks user to choose score they'd like to take.
        decision = su.input_positive_integer('Please enter the number for the scoring option you\'d like to take: ', 'Invalid option.', 1,len(poss_scores))
        decision -= 1
        # Takes chosen score, creates dictionary, and returns it.
        choice = poss_scores[decision]
        return choice


# End-game scoring methods.


    def display_scorecard(self, scorecard: dict):
        """Given a player dictionary, fish out the scorecard and print the contents to the screen in a pleasing manner consistent with the real life scorecard"""
        for k,v in scorecard.items():
            print(f'{k:20}{v:>10}')
    
    def score_for_top(self) ->int:
        """Takes a player's dictionary and calculates the total top section score for their scorecard. Outputs the integer without adding the bonus."""
        top_categories = self.keys_in_order[0:6]
        score = []

        for category in top_categories:
            value = self.scorecard[category]
            score.append(value)
        return sum(score)


    def score_for_bottom(self) ->int:
        """Takes a player's dictionary and calculates the total top section score for their scorecard. Outputs the integer without adding the bonus."""
        categories = self.keys_in_order[6:]
        score = []

        for category in categories:
            value = self.scorecard[category]
            score.append(value)
        return sum(score)

    def _adjust_scorecard(self):
        for k,v in self.scorecard.items():
            if v == '':
                self.scorecard[k] = 0

    def display_final_scorecard(self, name:str):
        """Given a player dictionary, fish out the scorecard and print the contents to the screen in a pleasing manner consistent with the real life scorecard.  This function should also calculate the final score, including the use of the bonuses and fields not used during game play."""
        print(f'\n{name}\'s final scorecard:')
        self._adjust_scorecard()
        self.display_scorecard(self.scorecard)
        top = self.score_for_top()
        bottom = self.score_for_bottom()

        if top >= 63:
            top += 35
            print('You got a top score bonus of 35!')

        total = top + bottom

        print(f'\nYour total top section score is: {top}')
        print(f'Your total bottom section score is: {bottom}')
        print(f"{name}\'s total score is: {total}")
        print('___________')
        return total


    def __str__(self):
        for k,v in self.scorecard.items():
            print(f'{k:20} {v:>10}')
