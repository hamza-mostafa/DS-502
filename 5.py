def vowel_counter(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(1 if i in vowels else 0 for i in string.join())
