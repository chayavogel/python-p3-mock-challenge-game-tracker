#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


chess = Game("chess")
chaya = Player("chaya")
result = Result(chaya, chess, 5)

variable = chaya.games_played()
print(variable)

ipdb.set_trace()
