from cerinta_0 import *

#
# ITERATIVE DEEPENING A* implementation with COST
#

# iterative function that constantly updates the cost limits in order to find
# the minimum path to the cheese by calling a recursive function
def bucla_IDA_star(env_graph, mouse_pos, cheese_pos, heuristic_func):
    # initialize the global cost limit and the eventual path to cheese
    h = heuristic_func(mouse_pos, cheese_pos)
    global_limit = h
    best_path = []

    # search the cheapest path until the cheese is found 
    # and as long as the graph allows it
    while best_path == [] and global_limit != INF:
        local_limit = global_limit
        global_limit = INF
        visited = {}

        # call the function that builds the path
        (best_path, best_cost, local_limit, global_limit) \
            = IDA_star(
                env_graph,
                mouse_pos,
                cheese_pos,
                0,
                local_limit,
                global_limit,
                best_path,
                visited,
                heuristic_func,
                h
                )
    
    return (best_path, best_cost)

# recursive function that searches the path of minimum cost from mouse
# to cheese within a cost limit
def IDA_star(
    env_graph,
    mouse_pos,
    cheese_pos,
    path_to_mouse_cost,
    local_limit,
    global_limit,
    best_path,
    visited,
    heuristic_func,
    old_h
    ):
    # if mouse reached cheese's position return the updated best path to it
    if mouse_pos.id == cheese_pos.id:
        best_path.insert(0, cheese_pos.id)
        best_cost = path_to_mouse_cost
        return (best_path, best_cost, local_limit, global_limit)
    
    # visit the current position
    visited[mouse_pos.id] = path_to_mouse_cost + old_h
    
    # generate the next accessible positions
    mouse_neigh = get_next_states(mouse_pos, env_graph)

    # check the cost of moving to each of the next accessible positions
    for i in mouse_neigh:
        # estimate the remaining cost to cheese from position i
        h = heuristic_func(env_graph[i], cheese_pos)
        # calculate the cost to reach the position i
        cost_to_reach_i = path_to_mouse_cost + mouse_pos.neigh[i]

        # if the position i has already been explored through this path
        # and the cost to reach it now is greater then ignore it
        if i in visited.keys() and visited[i] <= cost_to_reach_i + h:
            continue

        # if the estimated cost is not greater than the best one estimated 
        # so far then move to the position i
        if cost_to_reach_i + h <= local_limit:
            (best_path, best_cost, local_limit, global_limit) \
                = IDA_star(
                    env_graph, 
                    env_graph[i], 
                    cheese_pos, 
                    cost_to_reach_i, 
                    local_limit, 
                    global_limit, 
                    best_path, 
                    visited,
                    heuristic_func,
                    h
                    )

            # if the cheese was found then update the path to it
            if best_path != []:
                best_path.insert(0, mouse_pos.id)
                return (best_path, best_cost, local_limit, global_limit)
        
        # if the estimated cost to reach the cheese from position i is greater
        # than the best one estimated so far then check if the result is lower
        # than the global limit. if so then reset the global limit
        else:
            if cost_to_reach_i + h < global_limit:
                global_limit = cost_to_reach_i + h

    # if the current path is not efficient to follow then 
    # return the empty path to cheese and the cost limits  
    return ([], 0, local_limit, global_limit)
