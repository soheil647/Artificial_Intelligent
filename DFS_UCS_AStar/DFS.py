import numpy as np
from Problem import Problem
from Algorithm import Algorithms

fobj = open("test2.txt")
initial_state = []
for line in fobj:
    new_arr = [i for i in str(line).replace('\n', '')]
    initial_state.append(new_arr)
fobj.close()

print(np.array(initial_state).reshape([len(initial_state), len(initial_state[-1])]))

fobj = open("out2.txt")
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
print("max node explored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ",
      alg.answerDepth)

# print("BFS answer :")
# alg.BFS(initial_state,initial_state)
# print("max node expored : ",alg.maxNodeExplored," max node expanded : ",alg.maxNodeExpanded," answer depth : ",alg.answerDepth)
