# Given a target string, generate a random string with the same length
# Compare and score the generated string vs the target string and repeatedly
#   re-make the generated string at the incorrect indexes
# Finally show the number of iterations
# Observation: without re-making the generated string, the score seems
#   to stuck at 0.25 for a fairly significant number of iterations
#   (not sure as to why)

import string
import random
from typing import Tuple, List


TARGET_STRING = "methinks it is like a weasel"
GENERATE_SOURCE_STRING = string.ascii_lowercase + " "
GENERATE_STRING_LENGTH = 28

def generate_string() -> str:
    '''Generates a string of length 28;
    containing the alphabet letters plus the space
    '''
    return "".join(
        random.choice(GENERATE_SOURCE_STRING)
        for _ in range(GENERATE_STRING_LENGTH)
    )

def score_string(generated_str: str) -> Tuple[float, list]:
    '''Gives a score to a generated string
    by comparing it to the target string;
    given that the two strings have same length

    Naive comparison: for each index, if the
    characters at that index of the generated string
    and the target string are the same, add 1 to the 
    overall score; then we divide this overall score
    by the length of the generated string
    '''
    if len(generated_str) != len(TARGET_STRING):
        raise ValueError
    print(f"Giving score for {generated_str} VS. {TARGET_STRING}")
    score = 0
    incorrect_indexes: List[int] = []
    for i in range(len(generated_str)):
        if generated_str[i] == TARGET_STRING[i]:
            score += 1
        else:
            incorrect_indexes.append(i)
    return score/len(TARGET_STRING), incorrect_indexes

def remake_string(generated_str: str, incorrect_indexes: List[int]) -> str:
    '''Remakes a generated string by
    re-randomizing the characters at the incorrect indexes
    '''
    remade_str = ""
    for i in range(len(generated_str)):
        if i in incorrect_indexes:
            remade_str += random.choice(GENERATE_SOURCE_STRING)
        else:
            remade_str += generated_str[i]
    return remade_str

def run_tries():
    iterations_count = 1
    gen = generate_string()
    gen_score, incorrect_indexes = score_string(gen)
    best_score = gen_score
    while best_score < 1:
        print(f"Current generated string: {gen}")
        print(f"Best score so far: {best_score}")
        gen = remake_string(gen, incorrect_indexes) # Remake string
        gen_score, incorrect_indexes = score_string(gen)
        best_score = max(gen_score, best_score)
        iterations_count += 1
    print(
        f"Program terminated at best score of {best_score}, after {iterations_count} iterations"
    )

# print(remake_string("abcd", [0,1]))
run_tries()
