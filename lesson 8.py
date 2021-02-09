# def test_variables(numb_1, numb_2, numb_3):
#     numb_1 = 5
#     print(a)
#     numb_2 = 2
#     return numb_1 + numb_2
#
# a = 100
# print(a)
# result = test_variables()
# print(result)
# print(a)

import random as rnd

def create_point(min_limit= -100, max_limit=100, debug_mode=False):
    point = (rnd.randint(min_limit, max_limit),
             rnd.randint(min_limit, max_limit),
             rnd.randint(min_limit, max_limit))
    if debug_mode:
        print(point)
    return point

res = create_point(debug_mode=True)