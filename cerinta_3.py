from cerinta_0 import *

def bucla_LRTA_star(env_graph, mouse_pos, cheese_pos, heuristic_func):
    visited = {}

    (less_trained_best_path, less_trained_best_cost, visited) = LRTA_star(env_graph, mouse_pos, cheese_pos, [], 0, visited, heuristic_func)
    (better_trained_best_path, better_trained_best_cost, visited) = LRTA_star(env_graph, mouse_pos, cheese_pos, [], 0, visited, heuristic_func)

    while less_trained_best_path != better_trained_best_path :

        less_trained_best_path = better_trained_best_path
        less_trained_best_cost = better_trained_best_cost
        (better_trained_best_path, better_trained_best_cost, visited) = LRTA_star(env_graph, mouse_pos, cheese_pos, [], 0, visited, heuristic_func)
    
    return (better_trained_best_path, better_trained_best_cost)

 
def LRTA_star(env_graph, mouse_pos, cheese_pos, best_path, best_cost, visited, heuristic_func):
    while mouse_pos.id != cheese_pos.id:
        
        next_states = get_next_states(mouse_pos, env_graph)

        min_f_i = INF
        best_next = next_states[0]
        for i in next_states:
            cost_mouse_i = mouse_pos.neigh[i]

            if i in visited.keys():
                h_i = visited[i]
            else:
                h_i = heuristic_func(env_graph[i], cheese_pos)
            f_i = cost_mouse_i + h_i

            if f_i < min_f_i:
                min_f_i = f_i
                best_next = i
        
        visited[mouse_pos.id] = min_f_i
        best_path.append(mouse_pos.id)
        best_cost += mouse_pos.neigh[best_next]
        mouse_pos = env_graph[best_next]

    best_path.append(mouse_pos.id)
    return (best_path, best_cost, visited)
