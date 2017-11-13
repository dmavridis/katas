def title_case(title, *args):
    minor_words = args[0].lower().split() if args else ''
    if title == '': return ''
    result = title.split()[0].capitalize()
    if len(title.split()) > 1:
        result += ' '
        result += ' '.join(word.capitalize() if word.lower() not in minor_words
                           else word.lower() for word in title.split()[1:])
    return result
