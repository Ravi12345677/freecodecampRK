import random

def player(prev_play, opponent_history=[]):
    # Store opponent moves
    if prev_play != "":
        opponent_history.append(prev_play)

    # First move
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # --- Strategy 1: Frequency counter ---
    count = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        count[move] += 1

    most_common = max(count, key=count.get)

    # Counter move
    counter = {"R": "P", "P": "S", "S": "R"}

    # --- Strategy 2: Pattern detection ---
    pattern = "".join(opponent_history[-4:])

    pattern_counts = {}

    for i in range(len(opponent_history) - 4):
        seq = "".join(opponent_history[i:i+4])
        next_move = opponent_history[i+4]

        if seq not in pattern_counts:
            pattern_counts[seq] = {"R": 0, "P": 0, "S": 0}

        pattern_counts[seq][next_move] += 1

    if pattern in pattern_counts:
        prediction = max(pattern_counts[pattern], key=pattern_counts[pattern].get)
        return counter[prediction]

    # --- Fallback ---
    return counter[most_common]