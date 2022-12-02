from random import randint

class Dice:
    """All dice functions/methods."""

    def roll_die(self) -> int:
        """Returns a value for a random roll of a six-sided die"""
        die = randint(1,6)
        return die

    def roll_dice(self, count: int) -> tuple:
        """Returns a tuple containing the results of rolling <count> dice"""
        all_dice = []
        for i in range(count):
            all_dice.append(self.roll_die())
        return tuple(all_dice)

    def dice_frequency(self, roll:tuple) -> dict:
        """returns a dictionary with the number as the key and the frequency as the value. This function might be helpful to use to solve some of the problems below."""
        score = {}
        for x in range(1,7):
            score[x] = roll.count(x)
        return score