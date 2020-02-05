#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    cont = contains_iter(text, pattern)
    
    return cont

def contains_iter(text, pattern):
    return pattern in text


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)
    text_i = 0
    pattern_i = 0
    if pattern == "":
        return 0
    while pattern_i < len(pattern) and text_i < len(text):
        if pattern[pattern_i] == text[text_i]:
            if pattern_i == len(pattern) - 1:
                return text_i - pattern_i
            text_i += 1
            pattern_i += 1
        elif pattern[pattern_i] != text[text_i]:
            if pattern_i != 0:
                text_i -= pattern_i - 1
                pattern_i = 0
            else:
                text_i += 1


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    text_i = 0
    pattern_i = 0
    indexes = []
    if pattern == "":
        return [x for x in range(len(text))]
    elif len(pattern) == 1:
        return [i for i, x in enumerate(text) if pattern == x]
    while text_i < len(text) and pattern_i < len(pattern):
        if pattern[pattern_i] == text[text_i]:
            if pattern_i == len(pattern) - 1:
                indexes.append(text_i - pattern_i)
                text_i -= pattern_i - 1
                pattern_i = 0
            text_i += 1
            pattern_i += 1
        elif pattern[pattern_i] != text[text_i]:
            if pattern_i != 0:
                text_i -= pattern_i - 1
                pattern_i = 0
            else:
                text_i += 1
    return indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
    print(find_all_indexes('aaa', 'a'))
