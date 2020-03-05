import numpy as np
import time
from Problem import Problem
from Algorithm import Algorithms

fobj = open("test3.txt")
initial_state = []
for line in fobj:
    new_arr = [i for i in str(line).replace('\n', '')]
    initial_state.append(new_arr)
fobj.close()

# print(np.array(initial_state).reshape([len(initial_state), len(initial_state[-1])]))

p = Problem(initial_state, None, None, None)
alg = Algorithms(p)
initial_state_properties = {'state': initial_state, 'have_patient': False, 'is_hospital': False,
                            'object_position': None, 'ambulance_x': None,
                            'ambulance_y': None}

start_time = time.time()
print("DFS unlimited :")
alg.dfs(initial_state_properties, initial_state)
print("max node explored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ",
      alg.answerDepth)
print("Elapsed Time is: ", time.time() - start_time)
alg.reset_factors()


start_time = time.time()
print("BFS answer :")
alg.bfs(initial_state_properties, initial_state)
print("max node explored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ",
      alg.answerDepth)
print("Elapsed Time is: ", time.time() - start_time)
alg.reset_factors()


start_time = time.time()
print("DFS growing depth answer :")
alg.ids(initial_state_properties, initial_state, 60)
print("max node explored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ",
      alg.answerDepth)
print("Elapsed Time is: ", time.time() - start_time)
alg.reset_factors()


start_time = time.time()
print("A* answer with admissible heuristic:")
alg.a_star(initial_state_properties, initial_state, True)
print("max node explored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ",
      alg.answerDepth)
print("Elapsed Time is: ", time.time() - start_time)
alg.reset_factors()

start_time = time.time()
print("A* answer second heuristic:")
alg.a_star(initial_state_properties, initial_state, False)
print("max node explored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ",
      alg.answerDepth)
print("Elapsed Time is: ", time.time() - start_time)
alg.reset_factors()