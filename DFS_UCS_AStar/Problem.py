import copy


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
        self.hospital_list = [[]]

    #  just for Hospital problem
    # To find Where is the ambulance x and y in our new state
    def find_ambulance(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 'A':
                    self.ambulance_y = i
                    self.ambulance_x = j

    def find_hospital(self, state):
        self.hospital_list = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j].isdigit():
                    self.hospital_list.append([i, j])
                    self.hospital_list = list(filter(None, self.hospital_list))

    def assign_movement(self, state_properties, movement):
        state_update_properties = copy.deepcopy(state_properties)  # to update for a new state

        # Check how to move in correct direction
        if movement == 'up':
            state_update_properties = self.check_movement(state_properties, self.ambulance_x, self.ambulance_y - 1,
                                                          movement)
        if movement == 'down':
            state_update_properties = self.check_movement(state_properties, self.ambulance_x, self.ambulance_y + 1,
                                                          movement)
        if movement == 'right':
            state_update_properties = self.check_movement(state_properties, self.ambulance_x + 1, self.ambulance_y,
                                                          movement)
        if movement == 'left':
            state_update_properties = self.check_movement(state_properties, self.ambulance_x - 1, self.ambulance_y,
                                                          movement)
        return state_update_properties

    # To Generate the states that agent can move in that direction
    def state_generator(self, state_properties):
        # To find where is the ambulance!
        self.find_ambulance(state_properties['state'])
        allowed_moves = ['up', 'down', 'right', 'left']
        # To remove the direction that there is an obstacle in the way
        if self.check_obstacle(state_properties, self.ambulance_x, self.ambulance_y - 1):
            allowed_moves.remove('up')
        if self.check_obstacle(state_properties, self.ambulance_x, self.ambulance_y + 1):
            allowed_moves.remove('down')
        if self.check_obstacle(state_properties, self.ambulance_x - 1, self.ambulance_y):
            allowed_moves.remove('left')
        if self.check_obstacle(state_properties, self.ambulance_x + 1, self.ambulance_y):
            allowed_moves.remove('right')
        new_map_properties = []  # New possible moves to iterate on
        for move in allowed_moves:
            new_map_properties.append(self.assign_movement(state_properties, move))
        return new_map_properties

    #  To see if agent is busy or ready for a new action
    def allowed_actions(self, state_properties):
        if self.actions is not None:
            return self.actions[state_properties]
        else:
            return self.state_generator(state_properties)

    # To check if we got the final state and our job is done!
    def is_final_state(self, state_properties):
        empty_hospitals = 0
        self.find_hospital(state_properties['state'])
        for i in range(len(self.hospital_list)):
            if state_properties['state'][self.hospital_list[i][0]][self.hospital_list[i][1]] == '0':
                empty_hospitals = empty_hospitals + 1
                if empty_hospitals == len(self.hospital_list):
                    return "Solve"
        if state_properties['have_patient'] is True:
            return "Patient"
        if state_properties['is_hospital'] is True:
            return "Hospital"
        return "Default"

    # To Check what is our next move obstacle and generate the allowed_movement
    def check_obstacle(self, state_properties, x_coordinate, y_coordinate):
        # To see if there is a WALL or Patient or Hospital
        if (state_properties['state'][y_coordinate][x_coordinate] == '#') or (
                state_properties['state'][y_coordinate][x_coordinate] == '0') or (
                self.have_patient is True and state_properties['state'][y_coordinate][
            x_coordinate] == 'P') or (
                self.have_patient is False and state_properties['state'][y_coordinate][
            x_coordinate].isdigit()):
            return True
        else:
            return False

    # Check if our new action needs changes in our agent and update for ne State
    def check_movement(self, state_properties, x_coordinate, y_coordinate, movement):
        state_update = copy.deepcopy(state_properties['state'])
        state_properties = {'state': state_update, 'have_patient': False, 'is_hospital': False,
                            'object_position': movement, 'ambulance_x': self.ambulance_x,
                            'ambulance_y': self.ambulance_y
                            }
        # To see if we dont have patient and our next move is patient so we should pick it up!
        if self.have_patient is False and state_properties['state'][y_coordinate][x_coordinate] == 'P':
            # self.have_patient = True
            state_update[y_coordinate][x_coordinate] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '
            state_properties.update({'state': state_update, 'have_patient': True, 'is_hospital': False,
                                     'object_position': movement, 'ambulance_x': x_coordinate,
                                     'ambulance_y': y_coordinate})

        # To see if we already have a patient and out next move is a not empty hospital so we take off the patient
        elif self.have_patient is True and state_properties['state'][y_coordinate][
            x_coordinate].isdigit() and (
                int(state_properties['state'][y_coordinate][x_coordinate])) != "0":
            state_update[y_coordinate][x_coordinate] = \
                str(int(state_properties['state'][y_coordinate][x_coordinate]) - 1)
            # self.have_patient = False
            state_update[self.ambulance_y][self.ambulance_x] = 'A'
            state_properties.update({'state': state_update, 'have_patient': False, 'is_hospital': True,
                                     'object_position': movement, 'ambulance_x': self.ambulance_x,
                                     'ambulance_y': self.ambulance_y})

        # To see if it is just a normal move
        else:
            state_update[y_coordinate][x_coordinate] = 'A'
            state_update[self.ambulance_y][self.ambulance_x] = ' '
            state_properties.update({'state': state_update, 'ambulance_x': x_coordinate,
                                     'ambulance_y': y_coordinate})
        return state_properties
