# AI needs to know the opponent's score, its own score, and the number of dice it has to roll.
import game

curr_score = 0

def ev(curr_score, num_dice, opp_score, own_score):
    farkleprobs = [0.67, 0.44, 0.28, 0.16, 0.08, 0.02]
    if num_dice == 1:
        expected = (1/6) * 100 + (1/6) * 50 + (2/3) * (-curr_score)
        return


def getaction(actions, opp_score, own_score, curr_score, num_dice):
    best_move = None
    for action in actions:
        return
def take_turn(own_score, opp_score):
    game.roll(6)
