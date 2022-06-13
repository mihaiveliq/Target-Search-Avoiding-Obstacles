from cerinta_0 import *
from cerinta_1 import *
from cerinta_2 import *
from cerinta_3 import *
from cerinta_4 import *
import time
import sys

class Graph():

    def __init__(self, env, i):
        self.mouse_pos = env[MOUSE_POS]
        self.cheese_pos = env[CHEESE_POS]
        self.env_graph = env[ENV_GRAPH]
        self.test_nr = i + 1
    
    def cerinta1(self):

        start_time = time.time()
        (path, cost) = bucla_DFID(self.env_graph, self.mouse_pos, self.cheese_pos)
        finish_time = time.time()

        return (path, cost, finish_time - start_time)
    
    def cerinta2(self):

        start_time = time.time()
        (path, cost) = bucla_IDA_star(self.env_graph, self.mouse_pos, self.cheese_pos, euclidean_distance)
        finish_time = time.time()

        return (path, cost, finish_time - start_time)
    
    def cerinta3(self):

        start_time = time.time()
        (path, cost) = bucla_LRTA_star(self.env_graph, self.mouse_pos, self.cheese_pos, euclidean_distance)
        finish_time = time.time()

        return (path, cost, finish_time - start_time)

    def cerinta4_1(self):

        start_time = time.time()
        (path, cost) = bucla_IDA_star(self.env_graph, self.mouse_pos, self.cheese_pos, my_heuristic)
        finish_time = time.time()

        return (path, cost, finish_time - start_time)
    
    def cerinta4_2(self):

        start_time = time.time()
        (path, cost) = bucla_LRTA_star(self.env_graph, self.mouse_pos, self.cheese_pos, my_heuristic)
        finish_time = time.time()

        return (path, cost, finish_time - start_time)
    
    def print_cerinta(self, cerinta, nume):
        (path, cost, computation_time) = cerinta
        print(nume)
        print('\t-Best cost is: ' + str(cost))
        print('\n\t-Cheapest path is:\n')
        print(path)
        print("\n\t-It took %s seconds to compute it." % (computation_time))
        print('\n')

    def test(self):

        # Creating Testi output file and redirecting the output
        out_file_name = 'testul' + str(self.test_nr) + '.out'
        f = open(out_file_name,'w')
        sys.stdout = f

        print('Testul ' + str(self.test_nr) + ':\n---------\n')

        # Cerinta1()
        self.print_cerinta(self.cerinta1(), '*Cerinta 1: DFID\n')
        # Cerinta2()
        self.print_cerinta(self.cerinta2(), '*Cerinta 2: IDA_star\n')
        # Cerinta4_1()
        self.print_cerinta(self.cerinta4_1(), '*Cerinta 4: IDA_star cu euristica my_heuristic\n')
        # Cerinta3()
        self.print_cerinta(self.cerinta3(), '*Cerinta 3: LTRA_star\n')
        # Cerinta4_2()
        self.print_cerinta(self.cerinta4_2(), '*Cerinta 4: LRTA_star cu euristica my_heuristic\n')
