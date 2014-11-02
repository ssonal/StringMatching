
def alphabet_index(c):
    return ord(c.lower()) - 97  # 'a' is ASCII character 97


def match_length(S, pos1, pos2):
    """
    Returns the length of the match of the substrings of S beginning at pos1 and pos2.
    """
    if pos1 == pos2:
        return len(S) - pos1
    match = 0
    while pos1 < len(S) and pos2 < len(S) and S[pos1] == S[pos2]:
        match += 1
        pos1 += 1
        pos2 += 1
    return match