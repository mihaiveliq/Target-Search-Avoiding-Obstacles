from math import sqrt
from heapq import heappop, heappush

# constants
INF = 999999999
X = 0
Y = 1
POS1_ID = 0
POS2_ID = 1
COST = 2
ID_POS = 0
X_POS = 1
Y_POS = 2
MOUSE_POS = 0
CHEESE_POS = 1
ENV_GRAPH = 2

# class that represent a position
class Position():
    def __init__(self, id, pos_x, pos_y):
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.neigh = {}

# function that builds the environment described by an input file
def init_env(input_file):
    # declare the environment components:

    # mouse's position on map as a list of coordonates
    mouse_pos = Position(-1, -1, -1)
    # cheese's position on map as a list of coordonates
    cheese_pos = Position(-1, -1, -1)
    # map as a "position_id<->Position" dictionary
    env_graph = {}
    # environment as a list of 
    # mouse's position on map 
    # cheese's position on map
    # map
    env = [mouse_pos, cheese_pos, env_graph]
    # obstacles as a list
    obstacles = []

    # open the input file
    fd = open(input_file, 'r')

    # parse mouse position
    mouse_pos_x, mouse_pos_y = tuple(fd.readline().split(', '))
    mouse_pos.pos_x = int(mouse_pos_x)
    mouse_pos.pos_y = int(mouse_pos_y)

    # parse cheese position
    cheese_pos_x, cheese_pos_y = tuple(fd.readline().split(', '))
    cheese_pos.pos_x = int(cheese_pos_x)
    cheese_pos.pos_y = int(cheese_pos_y)

    # parse the total number of positions
    positions_no = int(fd.readline())

    # parse each position into a new position in the positions graph
    for i in range(positions_no):
        position = fd.readline().strip('\n').split(', ')

        id_pos = int(position[ID_POS])

        if len(position) > 3:
            obstacles.append(id_pos)
            continue
        
        x_pos = int(position[X_POS])
        y_pos = int(position[Y_POS])

        if x_pos == mouse_pos.pos_x and y_pos == mouse_pos.pos_y:
            mouse_pos.id = id_pos
            env_graph[id_pos] = mouse_pos

        elif x_pos == cheese_pos.pos_x and y_pos == cheese_pos.pos_y:
            cheese_pos.id = id_pos
            env_graph[id_pos] = cheese_pos

        else:
            env_graph[id_pos] = Position(id_pos, x_pos, y_pos)

    # parse the total number of edges
    edges_no = int(fd.readline())

    # parse each edge by placing the positions in the corespondant 
    # neighbours list
    for i in range(edges_no):
        edge = fd.readline().strip('\n').split(', ')

        pos1_id = int(edge[POS1_ID])
        pos2_id = int(edge[POS2_ID])

        if pos1_id in obstacles or pos2_id in obstacles:
            continue

        cost = int(edge[COST])

        env_graph[pos1_id].neigh[pos2_id] = cost
        env_graph[pos2_id].neigh[pos1_id] = cost

    # return environment
    return env

# function that generates all the next states from a current state
def get_next_states(curr_state, env_graph):
    
    return list(env_graph[curr_state.id].neigh)

# function that creates the next state from a state after aplying an action
def apply_action(curr_state, action, env):
    next_state = []

    return next_state

# function that calculates the euclidian distance between 2 positions
def euclidean_distance(pos1, pos2):
    x1, y1 = pos1.pos_x, pos1.pos_y
    x2, y2 = pos2.pos_x, pos2.pos_y

    return int(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))

# function that calculates the manhattan distance between 2 positions
def manhattan_distance(pos1, pos2):

    x1, y1 = pos1.pos_x, pos1.pos_y
    x2, y2 = pos2.pos_x, pos2.pos_y

    return int(abs(x1 - x2) + abs(y1 - y2))
    