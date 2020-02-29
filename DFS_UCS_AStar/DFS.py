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

print(p.states)
start_time = time.time()
print("BFS answer :")
alg.bfs(initial_state_properties, initial_state)
print("max node expored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ",
      alg.answerDepth)
print("Elapsed Time is: ", time.time() - start_time)
alg.reset_factors()
