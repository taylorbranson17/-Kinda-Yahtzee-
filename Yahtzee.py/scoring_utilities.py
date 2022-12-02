
def dice_frequency(roll:tuple) -> dict:
    """returns a dictionary with the number as the key and the frequency as the value. This function might be helpful to use to solve some of the problems below."""
    score = {}
    for x in range(1,7):
        score[x] = roll.count(x)
    return score
    
def score_for_aces(roll:tuple) -> int:
    """returns score for the aces present in the roll"""
    
    aces = roll.count(1)
    return aces

def score_for_twos(roll:tuple) -> int:
    """returns score for the twos present in the roll"""
    
    twos = roll.count(2)*2
    return twos

def score_for_threes(roll:tuple) -> int:
    """returns score for the threes present in the roll"""

    threes = roll.count(3)*3
    return threes

def score_for_fours(roll:tuple) -> int:
    """returns score for the fours present in the roll"""
    
    fours = roll.count(4)*4
    return fours

def score_for_fives(roll:tuple) -> int:
    """returns score for the fives present in the roll"""

    fives = roll.count(5)*5
    return fives

def score_for_sixes(roll:tuple) -> int:
    """returns score for the sixes present in the roll"""

    sixes = roll.count(6)*6
    return sixes


    
#bottom part of scorecard#

def score_for_three_of_a_kind(roll:tuple) -> int:
    """returns total of dice if three or more of a kind are present, zero if not"""
    score = dice_frequency(roll)
    for i in roll:
        if score[i] >= 3:
            score = sum(roll)
            return score
        else: 
            pass

    return 0 

def score_for_four_of_a_kind(roll:tuple) -> int:
    """returns total of dice if four or more of a kind are present, zero if not"""

    score = dice_frequency(roll)
    for i in roll:
        if score[i] >= 4:
            score = sum(roll)
            return score
        else:
            pass 
    return 0

def score_for_full_house(roll:tuple) -> int:
    """returns 25 if a full house is present, 0 if not"""

    score = tuple(dice_frequency(roll).values())
    if 3 in score and 2 in score:
        return 25
    else:
        return 0
    

def  score_for_small_straight(roll:tuple) -> int:
    """returns 30 if small straight is present, 0 if not"""

    possible_sets = [{1,2,3,4},{2,3,4,5},{3,4,5,6}]

    for x in possible_sets:
        if x.issubset(roll):
            return 30
        else:
            pass
    return 0    


def score_for_large_straight(roll:tuple) -> int:
    """returns 40 if large straight is present, 0 if not"""

    possible_sets = [{1,2,3,4,5},{2,3,4,5,6}]

    for x in possible_sets:
        if x.issubset(roll):
            return 40
        else:
            pass
    return 0    


def score_for_chance(roll:tuple) -> int:
    """returns the sum of the dice roll"""
    score = sum(roll)
    return score


def score_for_yahtzee(roll:tuple) -> int:
    """returns 50 if all dice are same number, 0 if not"""
    score = dice_frequency(roll)
    for i in roll:
        if score[i] == 5:
            return 50
        else: 
            pass
    return 0

my_library = {'Aces': score_for_aces, 'Twos':score_for_twos, 'Threes': score_for_threes, 'Fours': score_for_fours, 'Fives': score_for_fives, 'Sixes': score_for_sixes, 'Three of a Kind': score_for_three_of_a_kind, 'Four of a Kind':score_for_four_of_a_kind, 'Full House': score_for_full_house, 'Small Straight': score_for_small_straight, 'Large Straight': score_for_large_straight, 'Chance': score_for_chance, 'Yahtzee': score_for_yahtzee, 'Bonus':0}

def score_for_category(category:str, hand:list) -> int:
    """uses the functions above to return the correct score for the given category using the given roll."""
    num = my_library[category](hand)
    return num

def input_positive_integer(prompt:str, warning:str, min:int, max:int) -> int:
    """Will present <prompt> for input, will not return until input is a positive integer in the given (inclusive) range of min and max.  Will present <warning> if user inputs something invalid."""

    while True:
        try:
            answer = int(input(prompt))
        except ValueError:
            print(warning)
            continue
        if answer >= min and answer <= max:
            break
        else: 
            print(warning)

    return answer

