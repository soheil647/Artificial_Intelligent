import numpy as np


class Problem:
    def __init__(self, initial_state, states, final_state, actions):
        # index number of state is equal to indexOf state element in states array
        # actions is a 2D array which shows states you can go from a state
        self.states = states
        self.final_state = final_state
        self.actions = actions
        self.initial_state = initial_state

    #  just for Hospital problem
    def find_ambulance(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 'A':
                    return i, j

    def find_walls(self, initial_state):
        walls = []
        for i in range(len(initial_state)):
            for j in range(len(initial_state[i])):
                if initial_state[i][j] == '#':
                    walls.append([i, j])
        return walls

    def assign_movement(self, state, movement):
        state_update = [[' ' for x in range(len(state[1]))] for y in range(len(state))]
        for i in range(len(state)):
            for j in range(len(state[i])):
                state_update[i][j] = state[i][j]
        ambY, ambX = self.find_ambulance(state_update)
        if movement == 'up':
            state_update[ambY - 1][ambX] = 'A'
            state_update[ambY][ambX] = ' '
        if movement == 'down':
            state_update[ambY + 1][ambX] = 'A'
            state_update[ambY][ambX] = ' '
        if movement == 'right':
            state_update[ambY][ambX + 1] = 'A'
            state_update[ambY][ambX] = ' '
        if movement == 'left':
            state_update[ambY][ambX - 1] = 'A'
            state_update[ambY][ambX] = ' '
        return state_update

    def state_generator(self, state):
        ambY, ambX = self.find_ambulance(state)
        allowed_moves = ['down', 'up', 'right', 'left']
        if state[ambY - 1][ambX] == '#':
            allowed_moves.remove('up')
        if state[ambY + 1][ambX] == '#':
            allowed_moves.remove('down')
        if state[ambY][ambX - 1] == '#':
            allowed_moves.remove('left')
        if state[ambY][ambX + 1] == '#':
            allowed_moves.remove('right')
        new_map = []
        for move in allowed_moves:
            new_map.append(self.assign_movement(state, move))
        return new_map

    #  just for sliding puzzle
    def allowed_actions(self, state):
        if self.actions is not None:
            return self.actions[state]
        else:
            return self.state_generator(state)

    def is_final_state(self, state):
        return np.array_equal(state, self.final_state)
