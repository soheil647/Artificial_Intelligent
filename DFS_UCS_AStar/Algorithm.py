import numpy as np


def copy_array(state):
    state_update = [[' ' for x in range(len(state[0]))] for y in range(len(state))]
    for i in range(len(state)):
        for j in range(len(state[i])):
            state_update[i][j] = state[i][j]
    return state_update


class Algorithms:
    solved = False
    maxNodeExplored = 0
    maxNodeExpanded = 0
    answerDepth = 0

    def __init__(self, problem):
        self.problem = problem

    def DFS_Unlimited(self, state, states_array):
        # print(count)
        if self.answerDepth < 100:
            # try:
            #     print(count)
            if not self.solved:
                self.answerDepth += 1
                if self.problem.is_final_state(state):
                    self.solved = True
                    self.answerDepth = len(states_array)
                    print("Final")
                    print(np.array(state).reshape([len(state), len(state[-1])]))
                    return state, states_array
                print("current")
                print(np.array(state).reshape([len(state), len(state[-1])]))
                # print(self.problem.have_patient)
                states_generated = self.problem.allowed_actions(state)
                self.maxNodeExplored += 1
                self.maxNodeExpanded += 1
                # print("States_Generated: ", states_generated)
                print("States_Array: ", states_array)
                for section_state in states_generated:
                    if section_state not in states_array:
                        new_copy = states_array
                        new_copy.append(section_state)
                        # print("Section_State: ")
                        # print(np.array(section_state).reshape([len(section_state), len(section_state[-1])]))
                        self.DFS_Unlimited(section_state, new_copy)
            # except:
            #     print('DFS unlimited exceed its max recursion')

    def BFS(self, state, states_array):
        try:
            if not self.solved:
                states_generated = self.problem.allowed_actions(state)
                for section_state in states_generated:
                    self.maxNodeExplored += 1
                    if self.problem.is_final_state(section_state):
                        new_copy = states_array.copy()
                        new_copy.append(section_state)
                        self.solved = True
                        self.answerDepth = len(states_array)
                        print("Final")
                        print(np.array(state).reshape([len(state), len(state[-1])]))
                        return state, states_array
                print("current")
                print(np.array(state).reshape([len(state), len(state[-1])]))
                for section_state in states_generated:
                    if section_state not in states_array:
                        self.maxNodeExpanded += 1
                        new_copy = states_array.copy()
                        new_copy.append(section_state)
                        self.BFS(section_state, new_copy)
        except:
            print('BFS exceed its max recursion')
