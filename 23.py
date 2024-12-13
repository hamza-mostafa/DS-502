def check_if_pangram(string):
    alphabet = set(string.ascii_lowercase)
    input_set = set(string.lower())
    return alphabet.issubset(input_set)
