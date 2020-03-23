def scan(input):
    words = input.split()
    result = []
    for word in words:
        if word.isdigit():
            result.append(('number', _convert_number(word)))
        else:
            word_type = _get_type(word)
            if word_type:
                result.append(word_type)
            else:
                result.append(('error', word))
    return result


def _get_type(word):
    allowable_words = {
        'direction': ['north', 'south', 'east', 'west',
                      'down', 'up', 'lef', 'right', 'back'],
        'verb': ['go', 'stop', 'kill', 'eat'],
        'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
        'noun': ['door', 'bear', 'princess', 'cabinet'],
    }

    result = ()
    for key, value in allowable_words.items():
        if word in value:
            result = (key, word)
            break
    return result


def _convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
