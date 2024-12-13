def vowel_counter(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join(i if i not in vowels else '' for i in string)