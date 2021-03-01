
def win_tree(curr_score, num_dice):
    if curr_score > 10000:
        return float("inf")
    else:







def farkle_prob(num_dice):
    probs = [0.66667, 0.44444, 0.27778, 0.15741, 0.07716, 0.02315]
    return probs[num_dice - 1]