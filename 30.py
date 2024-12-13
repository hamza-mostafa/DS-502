# like 25
def only_palindrome(l):
    return [i for i in l if i == i[::-1]]
