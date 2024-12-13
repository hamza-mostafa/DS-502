def anagram_check(string1, string2):
    return sorted(string1) == sorted(string2)

# good if no duplicate letters included
# def anagram_check2(string1, string2):
#     return set(string1).issubset(set(string2)) and len(string1) == len(string2)