import numpy as np
from Problem import Problem
from Algorithm import Algorithms

fobj = open("test1.txt")
initial_state = []
for line in fobj:
    new_arr = [i for i in str(line).replace('\n', '')]
    initial_state.append(new_arr)
fobj.close()

fobj = open("out1.txt")
final_state = []
for line in fobj:
    new_arr = [i for i in str(line).replace('\n', '')]
    final_state.append(new_arr)
fobj.close()
# patients = []
#          print(print(np.array(state).reshape([7, 6])))

p = Problem(initial_state, None, final_state, None)
alg = Algorithms(p)


print("DFS unlimited :")
alg.DFS_Unlimited(initial_state, initial_state)
print("max node expored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ", alg.answerDepth)



# i, j = Problem.find_ambulance(p, initial_state)
# initial_state[i][j] = ' '
# initial_state[i + 1][j] = 'A'
# print(np.array(initial_state).reshape([7, 6]))
# initial_state[i + 1][j] = ' '
# initial_state[i + 2][j] = 'A'
# print(np.array(initial_state).reshape([7, 6]))
# initial_state[i + 2][j] = ' '
# initial_state[i + 3][j] = 'A'
# print(np.array(initial_state).reshape([7, 6]))

