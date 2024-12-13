def integer_value_only(mixed_dict):
    return {k: v for k, v in mixed_dict.items() if isinstance(v, int)}