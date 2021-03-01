import random as r
from operator import itemgetter as ig
import agent


def count(vals, num):
    return vals.count(num)


def roll(num_dice):
    dice_results = []
    for i in range(0, num_dice):
        val = r.randint(1, 6)
        dice_results.append(val)
    print(dice_results)
    return dice_results


def get_scores(vals):
    scores = []
    totals = [count(vals, 1), count(vals, 2), count(vals, 3), count(vals, 4), count(vals, 5), count(vals, 6)]
    ones = count(vals, 1)
    fives = count(vals, 5)

    base_score = count(vals, 1) * 100 + count(vals, 5) * 50

    for i in range(0, ones + 1):
        for j in range(0, fives + 1):
            scores.append((i + j, (i * 100) + (j * 50)))
    for i in [2, 3, 4, 6]:
        if count(vals, i) == 3:
            scores.append((3, i * 100))
            scores.append((3 + ones + fives, i * 100 + base_score))
    if count(vals, 5) == 3:
        scores.append((3, 500))
        scores.append((3 + ones, 500 + (ones * 100)))
    if count(totals, 1) == 6:  # straight
        scores.append((6, 1500))
    if count(totals, 2) == 3:  # three pairs
        scores.append((6, 1500))

    if count(totals, 4) == 1:  # four of one number
        num = totals.index(5) + 1
        scores.append((4, 1000))
        if num is not 1 or 5:
            scores.append(((4 + ones), 1000 + (ones * 100)))
            scores.append(((4 + fives), 1000 + (fives * 50)))
            scores.append((4 + ones + fives, 1000 + base_score))
        elif num is 1:
            scores.append((4 + fives, 1000 + (fives * 50)))
        elif num is 5:
            scores.append((4 + ones, 1000 + (ones * 100)))
    if count(totals, 4) == 1 and count(totals, 2) == 1:  # quads + pair
        scores.append((6, 1500))

    if count(totals, 5) == 1:  # five of one number
        num = totals.index(5) + 1
        scores.append((5, 2000))
        if num is not 1 or 5:
            scores.append((5 + ones, 2000 + ones * 100))
            scores.append((5 + fives, 2000 + fives * 50))
            scores.append((ones + fives + 5, 2000 + base_score))
        elif num is 1:
            scores.append((fives + 5, 2000 + (fives * 50)))
        elif num is 5:
            scores.append((ones + 5, 2000 + (ones * 100)))

    if count(totals, 3) == 2:  # two triplets
        scores.append((6, 2500))
    if count(totals, 6) == 1:  # six of one number
        scores.append((6, 3000))

    return scores


def choice_helper(scores):
    choices = []
    sorted_scores = [[score for score in scores if score[0] == 1], [score for score in scores if score[0] == 2],
                     [score for score in scores if score[0] == 3], [score for score in scores if score[0] == 4],
                     [score for score in scores if score[0] == 5], [score for score in scores if score[0] == 6]]
    for score in sorted_scores:
        if score:
            choices.append(max(score))
    return choices


def main():
    p1score = 0
    p2score = 0
    p1threshold = False
    p2threshold = False
    num_dice = 6
    while p1score < 10000:
        x = input("Press r to roll or e to end your turn.")
        if x == 'r':
            dice = roll(num_dice)
            scores = get_scores(dice)
            m = max(scores, key=ig(1))
            if m[1] == 0:
                print("Farkle!")
                num_dice = 6
            else:
                print(choice_helper(scores))
                y = input("Select the score you'd like to keep.")
                p1choice = choice_helper(scores)[int(y) - 1]
                p1score += p1choice[1]
                num_dice = 6 if num_dice - m[0] == 0 else num_dice - m[0]
            x = input("Score: " + str(p1score) + ". Dice: " + str(num_dice) + ".")


agent.curr_score = 0

if __name__ == '__main__':
    main()
