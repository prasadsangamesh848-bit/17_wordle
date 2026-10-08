def evaluate(target, guess):
    # Start with all letters marked gray.
    result = ["gray"] * len(guess)

    # Keep track of how many times each letter is still
    # available in the target word.
    remaining = {}

    for ch in target:
        remaining[ch] = remaining.get(ch, 0) + 1

    # First pass: identify exact matches.
    # Exact matches get priority and their letter occurrence
    # is removed from the available target letters.
    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
            remaining[ch] -= 1

    # Second pass: identify letters that exist in the target
    # but are in the wrong position.
    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue

        if remaining.get(ch, 0) > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result