from dice import Dice

class Hand:

    def __init__(self):
        self.hand = []
        self.keepers = []
        self.dice = Dice()


    def yahtzee_roll(self):
        """Rolls five, six sided die and prints them."""
        input('Hit enter to roll the die: ')
        self._clear_hand()
        roll = self.dice.roll_dice(5)
        self.hand.extend(roll)
        # Print current hand.
        self._print_hand()

    def new_yahtzee_roll(self):
        """Rolls five, six sided die and prints them."""
        self._clear_hand()
        roll = self.dice.roll_dice(5)
        self.hand.extend(roll)
        # Print current hand.
        self._print_hand()

    def _clear_hand(self):
        for x in self.hand.copy():
            self.hand.remove(x)
    
    def _clear_keepers(self):
        for x in self.keepers.copy():
            self.keepers.remove(x)

    def _print_hand(self):
        """Prints clean output for the users hand."""
        print('Here\'s your new hand...')
        for x in self.hand:
            print(x)
        print('________')
    
    def _count_of_remaining_dice(self, group: tuple, keepers:tuple) -> int:
        """Returns the number of dice remaining after removing <keepers> from <group>. ANY KEEPERS NOT IN THE GROUP ARE IGNORED."""
        group_list = group
        for i in keepers:
            if i in group:
                group_list.remove(i)
            else:
                pass
        return len(group_list)

    def _integers_from_comma_delimited_string(self, input: str) -> tuple:
        """Takes a comma-delimited string and creates a tuple of the values between the commas, removing whitespace from each value."""
        new_input = input.split(',')
        try:
            output = [int(x.strip()) for x in new_input]
        except ValueError:
            print('Something other than numbers snuck into your \'Keepers\'. Try again.')
        else:
            return tuple(output)

    def new_roll(self):
        """Removes any unwanted die from the players hand, rolls replacement die, and adds the newly rolled die to complete the hand."""
        # Get number of new die to roll.
        count_roll = self._count_of_remaining_dice(self.hand, self.keepers)

        # Add Keepers to the players hand.
        self._clear_hand()
        self.hand.extend(self.keepers)
        new_die = self.dice.roll_dice(count_roll)
        # Add newly rolled dice to players hand & print.
        self.hand.extend(new_die)
        # Print die.
        self._print_hand()
    
    def _validate_keepers(self, keepers: tuple):
        """Double checks that a users <keepers> are in their roll. Prevents cheating."""
        frequency_dict = self.dice.dice_frequency(self.hand)
        for num in keepers:
            try:
                if frequency_dict[num] > 0:
                    frequency_dict[num] -= 1
                elif frequency_dict[num] == 0:
                    print(f'Sorry, {num} isn\'t in your roll.')
                    return False
            except KeyError:
                print(f'Sorry, {num} isn\'t in Yahtzee.')
                return False
        return True

    def _get_keepers(self):
        """Requires users to enter the values they'd like to keep, and only returns valid keepers."""
        
        while True: 
            self._clear_keepers()
            dice = input('Please enter the dice you\'d like to keep sepearated by a comma, then hit enter to re-roll: ')
            # Break if user decides to keep all die.
            if dice != '':
                split_die = self._integers_from_comma_delimited_string(dice)
                if split_die:
                    # Return keeper die if they're in user's hand, or continues loop until all keepers are validated.
                    if self._validate_keepers(split_die):
                        self.keepers.extend(split_die) # -> tuple
                        if len(split_die) == 5:
                            return 7
                        else:
                            return True
                    else: 
                        continue
                else:
                    continue
            else:
                break

    def re_roll(self) -> tuple:
        """Gives the user an option to reroll up to three times."""
        for x in range(2): 
            keepers = self._get_keepers()
            if keepers == 7:
                break
            elif keepers: 
                if self.new_roll():
                    continue
            else:
                self.new_yahtzee_roll()