from cerinta_0 import *

# function that calculates the geometric mean between
# euclidian and manhattan distances 
#
# this heuristic is admissible because the euclidian
# and manhattan distances are admissible and the
# result is lower than each of them
def my_heuristic(pos1, pos2):
    ed = euclidean_distance(pos1, pos2)
    md = manhattan_distance(pos1, pos2)
    return int(sqrt(ed * md))
