import numpy as np


class Problem:
    def __init__(self, initial_state, states, final_state, actions):
        # index number of state is equal to indexOf state element in states array
        # actions is a 2D array which shows states you can go from a state
        self.states = states
        self.final_state = final_state
        self.actions = actions
        self.initial_state = initial_state
        self.have_patient = False
        self.ambulance_x = 0
        self.ambulance_y = 0
        self.patient_list = []
        self.hospital_list = []
        self.hospital_caps = []
        self.wall_list = []

    #  just for Hospital problem
    def find_ambulance(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 'A':
                    self.ambulance_y = i
                    self.ambulance_x = j

    # For finding the patient in Hospital Map
    def find_patient(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 'P':
                    self.patient_list.append([i, j])

    # For Finding Hospitals in map
    def find_hospitals(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j].isdigit():
                    self.hospital_list.append([i, j])
                    self.hospital_caps.append(int(state[i][j]))

    def find_walls(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == '#':
                    self.wall_list.append([i, j])


    def assign_movement(self, state, movement):
        state_update = [[' ' for x in range(len(state[1]))] for y in range(len(state))]
        for i in range(len(state)):
            for j in range(len(state[i])):
                state_update[i][j] = state[i][j]
        # ambulance_y, ambulance_x = self.find_ambulance(state_update)
        # patient_list = self.find_patient(state)
        # hospital_list, hospital_cap = self.find_hospitals(state)

        # Check if Moving Top
        if movement == 'up':
            # if self.have_patient is False and state[ambulance_y - 1][ambulance_x] == 'P':
            #     self.have_patient = True
            # if self.have_patient is True and hospital_list.__contains__(state[ambulance_y - 1][ambulance_x]) and hospital_cap != "0":
            #     self.have_patient = False
            #     state_update
            state_update[self.ambulance_y - 1][self.ambulance_x] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '
        if movement == 'down':
            state_update[self.ambulance_y + 1][self.ambulance_x] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '
        if movement == 'right':
            state_update[self.ambulance_y][self.ambulance_x + 1] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '
        if movement == 'left':
            state_update[self.ambulance_y][self.ambulance_x - 1] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '
        return state_update,

    def state_generator(self, state):
        self.find_ambulance(state)
        allowed_moves = ['down', 'up', 'right', 'left']
        if self.check_obstacle(state, self.ambulance_x, self.ambulance_y - 1):
            allowed_moves.remove('up')
        if self.check_obstacle(state, self.ambulance_x, self.ambulance_y + 1):
            allowed_moves.remove('down')
        if self.check_obstacle(state, self.ambulance_x - 1, self.ambulance_y):
            allowed_moves.remove('left')
        if self.check_obstacle(state, self.ambulance_x + 1, self.ambulance_y):
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

    def check_obstacle(self, state, x_coordinate, y_coordinate):
        if (self.wall_list.__contains__([y_coordinate, x_coordinate]) == '#') or (
                self.have_patient is True and state[y_coordinate][x_coordinate] == 'P') or (
                self.have_patient is False and self.hospital_list.__contains__(
                [y_coordinate, x_coordinate]) and self.hospital_caps != "0"):
            return True
        else:
            return False
