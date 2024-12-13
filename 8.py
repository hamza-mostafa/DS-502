def intersect_dicts(dict1, dict2):
    return {k: v for k, v in dict1.items() if k in dict2 and dict2[k] == v}