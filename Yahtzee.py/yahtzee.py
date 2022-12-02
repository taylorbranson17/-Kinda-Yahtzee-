from scorecard import Scorecard
from settings import Settings
from dice import Dice
from players import Player

class YahtzeeGame:

    def __init__(self):
        self.settings = Settings()
        self.players = []
        self.final_scores = {}

    def establish_players(self):
        """Prints welcome message, collects names of players, and creates scorecards for each."""
        print('\nHello! Welcome to your digital Yahtzee Game!')
        p_list = tuple(self._values_from_comma_delimited_string(self._input_non_empty_string('Please enter the name of all players, separated by commas. Hit enter when done: ','You must enter at least 1 player.'))) # -> tuple w/names
        for player in p_list:
            self.players.append(Player(player.title()))
    
    def print_rules(self):
        decision = input('Press (R) to read game rules, or enter to continue: ')
        with open('rules.txt', 'r') as f:
            rules = f.read()
        if decision in ['R', 'r']:
            print(f'\n{rules}')
            input('(Hit enter to continue:)')
            self.settings.clear()

    def _input_non_empty_string(self, prompt:str, warning:str) -> str:	
        """Will present <prompt> for input, will not return until input is a non-empty string. Will present <warning> if user inputs something invalid."""
        while True:
            answer = input(prompt)
            if answer in ['', ' ']:
                print(warning)
                continue
            break
        return answer

    def _values_from_comma_delimited_string(self, input: str) -> tuple:
        """Takes a comma-delimited string and creates a tuple of the values between the commas.  Makes sure to handle the removal of any spaces the user may or may not have entered"""
        new_input = input.split(',')
        output = [x.strip() for x in new_input]
        return output

    def end_display(self):
        print('The game has concluded, I\'m calculating scores now...')
        self.settings.sleep(5)
        for player in self.players:
            player.display_final()
            self.final_scores[player.name] = player.score
        winner = self._compare_scores(self.final_scores)
        print(f'\n\t\tCongrats, {winner}, You Won!\n')

    def _compare_scores(self, scores:dict):
        winning_score = max(scores.values())
        winner = ''
        for i in scores:
            if scores[i] == winning_score:
                return i

    def run_game(self):
        self.establish_players()
        self.print_rules()
        count = 1
        while self.settings.rounds > 0:
            print(f'Round {count}')
            for player in self.players:
                player.take_turn()
                self.settings.sleep(3)
                self.settings.clear()
            self.settings.rounds -= 1
            count +=1
        self.end_display()