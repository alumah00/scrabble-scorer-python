# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = 0

    for char in word:

        for point_value in OLD_POINT_STRUCTURE:

            if char in OLD_POINT_STRUCTURE[point_value]:
                letterPoints += point_value

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   choice = input("Let's play some Scrabble!\n\nEnter a word to score:")
   return choice

def simple_scorer(word):
    word = word.lower()
    points = 0
    for char in word:
        points += 1
    return points

def vowel_bonus_scorer(word):
    word = word.lower()
    points = 0
    for char in word:
        if char in ["a", "e", "i", "o", "u"]:
            points += 3
        else: points += 1
    return points 

def scrabble_scorer(word):
    word = word.lower()
    points = 0
    for letter in word:
        if letter in new_point_structure:
            points += new_point_structure[letter]
    return points

scoring_algorithms = ()

def scorer_prompt():
    print('Which scoring algorithm would you like to use?')
    
    for index, algorithm in enumerate(scoring_algorithms):
        print(f'{index} - {algorithm["name"]}: {algorithm["description"]}')

    selection = int(input('Enter 0, 1, or 2:'))

    selected_score_algorithm_dict = scoring_algorithms[selection]

    return selected_score_algorithm_dict


def transform(provided_dict):
    new_dict = {}

    new_dict["' '"] = 0

    for (key, value) in provided_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict


new_point_structure = transform(OLD_POINT_STRUCTURE)

simple_scorer_dict = {
    'name': 'Simple',
    'description': 'scores each letter provided is worth 1 point.',
    'score_function': simple_scorer
}

vowel_bonus_scorer_dict = {
    'name': 'Bonus Vowels',
    'description': 'gives 3 point per vowels and 1 point per consonants',
    'score_function': vowel_bonus_scorer
}

old_scrabble_scorer_dict = {
    'name': 'Scrabble',
    'description': 'uses the original Scrabble game point system',
    'score_function': scrabble_scorer
}

scoring_algorithms = (
    simple_scorer_dict,
    vowel_bonus_scorer_dict,
    old_scrabble_scorer_dict
)


def run_program():
    word = initial_prompt()

    selected_score_algorithm_dict = scorer_prompt()

    points = selected_score_algorithm_dict['score_function'](word)

    print(
        f'''
The word you entered was "{word}".
You selected the "{selected_score_algorithm_dict["name"]}" scoring algorithm which {selected_score_algorithm_dict["description"]}.
Your word is worth {points} points!'''
    )

