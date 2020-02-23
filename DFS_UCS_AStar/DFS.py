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
print(p.find_ambulance(initial_state))
print(p.ambulance_y, p.ambulance_x)
p.find_hospitals(initial_state)
p.find_patient(initial_state)
p.find_walls(initial_state)

print("DFS unlimited :")
alg.DFS_Unlimited(initial_state, initial_state)
print("max node expored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ", alg.answerDepth)


# print("A* answer :")
# alg.Astar(initial_state, initial_state)
# print("max node expored : ", alg.maxNodeExplored, " max node expanded : ", alg.maxNodeExpanded, " answer depth : ", alg.answerDepth)



