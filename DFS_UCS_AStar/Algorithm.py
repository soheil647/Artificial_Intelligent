import numpy as np

class Algorithms:
    solved = False
    maxNodeExplored = 0
    maxNodeExpanded = 0
    answerDepth = 0

    def __init__(self, problem):
        self.problem = problem

    def copy_array(self, state):
        state_update = [[' ' for x in range(len(state[-1]))] for y in range(len(state))]
        for i in range(len(state)):
            for j in range(len(state[i])):
                state_update[i][j] = state[i][j]
        return state_update

    def DFS_Unlimited(self, state, states_array):
        # try:
            # print(state)
            if not self.solved:
                self.answerDepth += 1
                if self.problem.is_final_state(state):
                    # print(states_array)
                    print(print(np.array(state).reshape([len(states_array[-1]), 6])))
                    self.solved = True
                    self.answerDepth = len(states_array)
                    return state, states_array
                states_generated = self.problem.allowed_actions(state)
                self.maxNodeExplored += 1
                self.maxNodeExpanded += 1
                for section_state in states_generated:
                    if section_state not in states_array:
                        new_copy = self.copy_array(states_array)
                        new_copy.append(section_state)
                        self.DFS_Unlimited(section_state, new_copy)
        # except:
        #     print('DFS unlimited exceed its max recursion')
