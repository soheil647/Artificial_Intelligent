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
        #     print(print(np.array(state).reshape([7, 6])))
        if not self.solved:
            self.answerDepth += 1
            if self.problem.is_final_state(state):
                # print(states_array)
                # print(print(np.array(state).reshape([len(states_array[-1]), 6])))
                self.solved = True
                self.answerDepth = len(states_array)
                return state, states_array

            print(state)
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

    def Astar(self, state, states_array):
        # try:
            if not self.solved:
                states_generated = self.problem.allowed_actions(state)
                states_cost = []
                for section_state in states_generated:
                    states_cost.append({'state': section_state, 'cost': self.state_cost(section_state)})
                sorted_states = sorted(states_cost, key=lambda kv: kv['cost'])
                for section_rating in sorted_states:
                    self.maxNodeExplored += 1
                    if self.problem.is_final_state(section_rating['state']):
                        self.solved = True
                        new_copy = self.copy_array(states_array)
                        new_copy.append(section_rating['state'])
                        print(new_copy)
                        self.answerDepth = len(states_array) + 1
                        return state, states_array
                for section_rating in sorted_states:
                    new_copy = self.copy_array(states_array)
                    new_copy.append(section_rating['state'])
                    self.maxNodeExpanded += 1
                    self.Astar(section_rating['state'], new_copy)
        # except:
            # print('A* exceed its max recursion')
