def sum_of_integers(integer_list):
    return sum(i if i > 0 else 0 for i in integer_list)
