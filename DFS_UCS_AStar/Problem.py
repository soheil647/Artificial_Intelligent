import numpy as np
from Algorithm import copy_array

class Problem:
    def __init__(self, initial_state, states, final_state, actions):
        # index number of state is equal to indexOf state element in states array
        # actions is a 2D array which shows states you can go from a state
        self.states = states                    # This is the state we are in now
        self.final_state = final_state          # This is our Final state
        self.actions = actions                  # New action for our agent
        self.initial_state = initial_state      # This is our start state
        self.have_patient = False               # Whether there is patient in hospital or not
        self.ambulance_x = 0                    # Ambulance x coordinate
        self.ambulance_y = 0                    # Ambulance y coordinate

    #  just for Hospital problem
    # To find Where is the ambulance x and y in our new state
    def find_ambulance(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 'A':
                    self.ambulance_y = i
                    self.ambulance_x = j

    def assign_movement(self, state, movement):
        state_update = [[' ' for x in range(len(state[-1]))] for y in range(len(state))]     # to update for a new state

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
        allowed_moves = ['down', 'up', 'right', 'left']
        # To remove the direction that there is an obstacle in the way
        if self.check_obstacle(state, self.ambulance_x, self.ambulance_y - 1):
            allowed_moves.remove('up')
        if self.check_obstacle(state, self.ambulance_x, self.ambulance_y + 1):
            allowed_moves.remove('down')
        if self.check_obstacle(state, self.ambulance_x - 1, self.ambulance_y):
            allowed_moves.remove('left')
        if self.check_obstacle(state, self.ambulance_x + 1, self.ambulance_y):
            allowed_moves.remove('right')
        new_map = []    # New possible moves to iterate on
        for move in allowed_moves:
            new_map.append(self.assign_movement(state, move))
        return new_map

    #  To see if agent is busy or ready for a new action
    def allowed_actions(self, state):
        if self.actions is not None:
            return self.actions[state]
        else:
            return self.state_generator(state)

    # To check if we got the final state and our job is done!
    def is_final_state(self, state):
        return np.array_equal(state, self.final_state)

    # To Check what is our next move obstacle and generate the allowed_movement
    def check_obstacle(self, state, x_coordinate, y_coordinate):
        # To see if there is a WALL or Patient or Hospital
        if (state[y_coordinate][x_coordinate] == '#') or (
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
            self.have_patient = True
            state_update[y_coordinate][x_coordinate] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '

        # To see if we already have a patient and out next move is a not empty hospital so we take off the patient
        if self.have_patient is True and state[y_coordinate][x_coordinate].isdigit() and (
                int(state[y_coordinate][x_coordinate])) != "0":
            state_update[y_coordinate][x_coordinate] = \
                str(int(state[y_coordinate][x_coordinate]) - 1)
            self.have_patient = False
            state_update[self.ambulance_y][self.ambulance_x] = 'A'

        # To see if it is just a normal move
        else:
            state_update[y_coordinate][x_coordinate] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '
        return state_update
