from enum import Enum
from random import choice


class Variants(Enum):
    SCISSORS = 'scissors'
    ROCK = 'rock'
    PAPER = 'paper'
    random_choice = choice([SCISSORS, ROCK, PAPER])
