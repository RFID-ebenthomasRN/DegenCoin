import random
import json
import os


def generate_random_number(lower_bound=1, upper_bound=99999):
    return random.randint(lower_bound, upper_bound)


def get_rng_based_on_probability(probs):
    cumulative_prob = list(np.cumsum(probs))
    rand_num = generate_random_number() / 100000.0
    return min([cumulative_prob.index(i) for i in cumulative_prob if i > rand_num])


def save_game(name_of_game, variables):
    if not os.path.exists('saved_games'):
        os.makedirs('saved_games')
    with open(os.path.join('saved_games', f'{name_of_game}.json'), 'w') as file:
        json.dump(variables, file)


def load_game(name_of_game):
    if os.path.exists(os.path.join('saved_games', f'{name_of_game}.json')):
        with open(os.path.join('saved_games', f'{name_of_game}.json'), 'r') as file:
            return json.load(file)
    else:
        return None