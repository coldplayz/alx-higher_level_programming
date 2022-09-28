#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
set_3 = None
set_4 = None
c_set = common_elements(set_3, set_4)
print(sorted(list(c_set)))
