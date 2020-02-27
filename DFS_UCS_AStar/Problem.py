import numpy as np
from Algorithm import copy_array


class Problem:
    def __init__(self, initial_state, states, final_state, actions):
        # index number of state is equal to indexOf state element in states array
        # actions is a 2D array which shows states you can go from a state
        self.states = states  # This is the state we are in now
        self.final_state = final_state  # This is our Final state
        self.actions = actions  # New action for our agent
        self.initial_state = initial_state  # This is our start state
        self.have_patient = False  # Whether there is patient in hospital or not
        self.ambulance_x = 0  # Ambulance x coordinate
        self.ambulance_y = 0  # Ambulance y coordinate
        self.patient_list = [[]]
        self.hospital_list = [[]]

    #  just for Hospital problem
    # To find Where is the ambulance x and y in our new state
    def find_ambulance(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 'A':
                    self.ambulance_y = i
                    self.ambulance_x = j

    def find_patient(self, state):
        self.patient_list = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 'P':
                    if [i, j] not in self.patient_list:
                        self.patient_list.append([i, j])
                        self.patient_list = list(filter(None, self.patient_list))

    def find_hospital(self, state):
        self.hospital_list = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j].isdigit():
                    self.hospital_list.append([i, j])
                    self.hospital_list = list(filter(None, self.hospital_list))

    def assign_movement(self, state, movement):
        state_update = [[' ' for x in range(len(state[-1]))] for y in range(len(state))]  # to update for a new state

        # Check how to move in correct direction
        if movement == 'up':
            state_update = self.check_movement(state, self.ambulance_x, self.ambulance_y - 1)
        if movement == 'down':
            state_update = self.check_movement(state, self.ambulance_x, self.ambulance_y + 1)
        if movement == 'right':
            state_update = self.check_movement(state, self.ambulance_x + 1, self.ambulance_y)
        if movement == 'left':
            state_update = self.check_movement(state, self.ambulance_x - 1, self.ambulance_y)
        return state_update

    # To Generate the states that agent can move in that direction
    def state_generator(self, state):
        self.find_ambulance(state)
        self.find_patient(state)
        # print(self.patient_list)
        allowed_moves = ['up', 'down', 'right', 'left']
        # To remove the direction that there is an obstacle in the way
        if self.check_obstacle(state, self.ambulance_x, self.ambulance_y - 1):
            allowed_moves.remove('up')
        if self.check_obstacle(state, self.ambulance_x, self.ambulance_y + 1):
            allowed_moves.remove('down')
        if self.check_obstacle(state, self.ambulance_x - 1, self.ambulance_y):
            allowed_moves.remove('left')
        if self.check_obstacle(state, self.ambulance_x + 1, self.ambulance_y):
            allowed_moves.remove('right')
        new_map = []  # New possible moves to iterate on
        print("Allowed_Moves: ", allowed_moves)
        for move in allowed_moves:
            new_map.append(self.assign_movement(state, move))
        # print("new_Map: ", new_map)
        return new_map

    #  To see if agent is busy or ready for a new action
    def allowed_actions(self, state):
        if self.actions is not None:
            return self.actions[state]
        else:
            return self.state_generator(state)

    # To check if we got the final state and our job is done!
    def is_final_state(self, state):
        empty_hospitals = 0
        self.lower_hospital_number(state)
        self.find_ambulance(state)
        self.find_hospital(state)
        if [self.ambulance_y, self.ambulance_x] in self.patient_list:
            self.have_patient = True
        for i in range(len(self.hospital_list)):
            if state[self.hospital_list[i][0]][self.hospital_list[i][1]] == '0':
                empty_hospitals = empty_hospitals + 1
        return empty_hospitals == len(self.hospital_list)

    # To Check what is our next move obstacle and generate the allowed_movement
    def check_obstacle(self, state, x_coordinate, y_coordinate):
        # To see if there is a WALL or Patient or Hospital
        if (state[y_coordinate][x_coordinate] == '#') or (
                state[y_coordinate][x_coordinate] == '0') or (
                self.have_patient is True and state[y_coordinate][x_coordinate] == 'P') or (
                self.have_patient is False and state[y_coordinate][x_coordinate].isdigit()):
            return True
        else:
            return False

    # Check if our new action needs changes in our agent and update for ne State
    def check_movement(self, state, x_coordinate, y_coordinate):
        state_update = copy_array(state)
        # To see if we dont have patient and our next move is patient so we should pick it up!
        if self.have_patient is False and state[y_coordinate][x_coordinate] == 'P':
            # self.have_patient = True
            state_update[y_coordinate][x_coordinate] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '

        # To see if we already have a patient and out next move is a not empty hospital so we take off the patient
        if self.have_patient is True and state[y_coordinate][x_coordinate].isdigit() and (
                int(state[y_coordinate][x_coordinate])) != "0":
            state_update[y_coordinate][x_coordinate] = \
                str(int(state[y_coordinate][x_coordinate]) - 1)
            # self.have_patient = False
            state_update[self.ambulance_y][self.ambulance_x] = 'A'

        # To see if it is just a normal move
        else:
            state_update[y_coordinate][x_coordinate] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '
        return state_update

    def lower_hospital_number(self, state):
        new_state = state
        temp_ambulance_x = self.ambulance_x
        temp_ambulance_y = self.ambulance_y
        self.find_ambulance(new_state)
        if temp_ambulance_x == self.ambulance_x and temp_ambulance_y == self.ambulance_y:
            if new_state[self.ambulance_y][self.ambulance_x - 1].isdigit():
                # new_state[self.ambulance_y][self.ambulance_x - 1] = str(
                #     int(new_state[self.ambulance_y][self.ambulance_x - 1]) - 1)
                self.have_patient = False
            if new_state[self.ambulance_y][self.ambulance_x + 1].isdigit():
                # new_state[self.ambulance_y][self.ambulance_x + 1] = str(
                #     int(new_state[self.ambulance_y][self.ambulance_x + 1]) - 1)
                self.have_patient = False
            if new_state[self.ambulance_y - 1][self.ambulance_x].isdigit():
                # new_state[self.ambulance_y - 1][self.ambulance_x] = str(
                #     int(new_state[self.ambulance_y - 1][self.ambulance_x]) - 1)
                self.have_patient = False
            if new_state[self.ambulance_y + 1][self.ambulance_x].isdigit():
                # new_state[self.ambulance_y + 1][self.ambulance_x] = str(
                #     int(new_state[self.ambulance_y + 1][self.ambulance_x]) - 1)
                self.have_patient = False
        # return new_state
