def duplicate_encode(word):
    word_count = {}
    for c in word.lower():
        if c not in word_count:
            word_count[c] = 1
        else:
            word_count[c] += 1
    return ''.join([''.join('(') if word_count[c]== 1 else ''.join(')') for c in word.lower()])