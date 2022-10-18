def magic_string():
    magic_string.c = getattr(magic_string, 'c', 0) + 1
    s = "BestSchool" if magic_string.c == 1 else "BestSchool, BestSchool"
    return s + ", BestSchool" * (magic_string.c - 2)
