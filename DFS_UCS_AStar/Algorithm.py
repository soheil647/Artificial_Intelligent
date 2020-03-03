import numpy as np
import copy


class Algorithms:
    solved = False
    maxNodeExplored = 0
    maxNodeExpanded = 0
    answerDepth = 0

    def __init__(self, problem):
        self.problem = problem

    def reset_factors(self):
        self.maxNodeExpanded = 0
        self.maxNodeExplored = 0
        self.answerDepth = 0
        self.solved = False
        self.problem.have_patient = False

    def state_cost(self, state_properties):
        cost = 0
        for r in range(1, 9):
            cost += r
            # i, j = self.find(state, r)
            # cost += abs(slidingPuzzle_value[r - 1]['i'] - i) + abs(slidingPuzzle_value[r - 1]['j'] - j)
        return cost

    def dfs(self, state_properties, states_array):
        try:
            if not self.solved:
                self.answerDepth += 1
                have_final_state = self.problem.is_final_state(state_properties)
                if have_final_state == "Solve":
                    self.solved = True
                    self.answerDepth = len(states_array)
                    print("Final for DFS")
                    print(np.array(state_properties['state']).reshape(
                        [len(state_properties['state']), len(state_properties['state'][-1])]))
                    return state_properties, states_array
                if have_final_state == "Patient":
                    self.problem.have_patient = True
                if have_final_state == "Hospital":
                    self.problem.have_patient = False
                # print("current")
                # print(np.array(state_properties['state']).reshape(
                #     [len(state_properties['state']), len(state_properties['state'][-1])]))
                # print("Have Patient: ", state_properties['have_patient'])
                # print("is Hospital: ", state_properties['is_hospital'])
                # print("Self have patient: ", self.problem.have_patient)
                states_generated = self.problem.allowed_actions(state_properties)
                self.maxNodeExplored += 1
                self.maxNodeExpanded += 1
                for section_state in states_generated:
                    if section_state['state'] not in states_array:
                        new_copy = copy.deepcopy(states_array)
                        new_copy.append(section_state['state'])
                        self.dfs(section_state, new_copy)
        except:
            print('DFS unlimited exceed its max recursion')

    def bfs(self, state_properties, states_array):
        try:
            if not self.solved:
                preferred_state = {}
                states_generated = self.problem.allowed_actions(state_properties)
                for section_state in states_generated:
                    self.maxNodeExplored += 1
                    have_final_state = self.problem.is_final_state(section_state)
                    if have_final_state == "Solve":
                        new_copy = copy.deepcopy(states_array)
                        new_copy.append(section_state)
                        self.solved = True
                        self.answerDepth = len(states_array)
                        print("Final for BFS")
                        print(np.array(section_state['state']).reshape(
                            [len(section_state['state']), len(section_state['state'][-1])]))
                        return section_state, states_array
                    if have_final_state == "Patient":
                        self.problem.have_patient = True
                        preferred_state = section_state
                        break
                    if have_final_state == "Hospital":
                        self.problem.have_patient = False
                        preferred_state = section_state
                        break
                # print("current")
                # print(np.array(state_properties['state']).reshape(
                #     [len(state_properties['state']), len(state_properties['state'][-1])]))
                # print("Have Patient: ", state_properties['have_patient'])
                # print("is Hospital: ", state_properties['is_hospital'])
                # print("Self have patient: ", self.problem.have_patient)
                if len(preferred_state) != 0 and preferred_state['state'] not in states_array:
                    # print(preferred_state)
                    self.maxNodeExpanded += 1
                    new_copy = copy.deepcopy(states_array)
                    new_copy.append(preferred_state)
                    self.bfs(preferred_state, new_copy)
                else:
                    for section_state in states_generated:
                        if section_state["state"] not in states_array:
                            self.maxNodeExpanded += 1
                            new_copy = copy.deepcopy(states_array)
                            new_copy.append(section_state['state'])
                            self.bfs(section_state, new_copy)
        except:
            print('BFS exceed its max recursion')

    def ids(self, state_properties, states_array, max_depth, counter):
        try:
            if not self.solved:
                self.answerDepth += 1
                have_final_state = self.problem.is_final_state(state_properties)
                if have_final_state == "Solve":
                    print("Final for DFS_Growing_Depth")
                    print(np.array(state_properties['state']).reshape(
                        [len(state_properties['state']), len(state_properties['state'][-1])]))
                    self.solved = True
                    self.answerDepth = len(states_array)
                    return state_properties, states_array
                if have_final_state == "Patient":
                    self.problem.have_patient = True
                if have_final_state == "Hospital":
                    self.problem.have_patient = False
                if counter > max_depth / 5:
                    return -1
                # if counter % 10 == 0:
                #     max_depth *= 2
                states_generated = self.problem.allowed_actions(state_properties)
                self.maxNodeExpanded += 1
                self.maxNodeExplored += 1
                # print("current")
                # print(np.array(state_properties['state']).reshape(
                #     [len(state_properties['state']), len(state_properties['state'][-1])]))
                # print("Have Patient: ", state_properties['have_patient'])
                # print("is Hospital: ", state_properties['is_hospital'])
                # print("Self have patient: ", self.problem.have_patient)
                for section_state in states_generated:
                    if section_state['state'] not in states_array:
                        new_copy = copy.deepcopy(states_array)
                        new_copy.append(section_state['state'])
                        self.ids(section_state, new_copy, max_depth, counter + 1)
        except:
            print('DFS_growing_depth exceed its max recursion')

    def a_star(self, state_properties, states_array):
        # try:
        if not self.solved:
            states_generated = self.problem.allowed_actions(state_properties)
            states_cost = []
            for section_state in states_generated:
                section_state.update({"cost": self.state_cost(section_state)})
                states_cost.append(section_state)
                # print(np.array(section_state['state']).reshape(
                #     [len(section_state['state']), len(section_state['state'][-1])]))
            sorted_states = sorted(states_cost, key=lambda kv: kv['cost'])
            for section_rating in sorted_states:
                self.maxNodeExplored += 1
                have_final_state = self.problem.is_final_state(state_properties)
                if have_final_state == "Solve":
                    self.solved = True
                    new_copy = copy.deepcopy(states_array)
                    new_copy.append(section_rating['state'])
                    print("Final for AStar")
                    print(np.array(state_properties['state']).reshape(
                        [len(state_properties['state']), len(state_properties['state'][-1])]))
                    self.answerDepth = len(states_array) + 1
                    return state_properties, states_array
                if have_final_state == "Patient":
                    self.problem.have_patient = True
                if have_final_state == "Hospital":
                    self.problem.have_patient = False
                print("current")
                print(np.array(state_properties['state']).reshape(
                    [len(state_properties['state']), len(state_properties['state'][-1])]))
                print("Have Patient: ", state_properties['have_patient'])
                print("is Hospital: ", state_properties['is_hospital'])
                print("Self have patient: ", self.problem.have_patient)
            for section_rating in sorted_states:
                new_copy = copy.deepcopy(states_array)
                new_copy.append(section_rating['state'])
                self.maxNodeExpanded += 1
                self.a_star(section_rating, new_copy)
    # except:
    #     print('A* exceed its max recursion')
