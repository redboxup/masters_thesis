import gym
import numpy as np
import sys
from gym.envs.toy_text import discrete

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
#adding 4 more possible steps
UP_RIGHT = 4
DOWN_RIGHT = 5
DOWN_LEFT = 6
UP_LEFT = 7

class WindyGridworldEnv(discrete.DiscreteEnv):

    metadata = {'render.modes': ['human', 'ansi']}

    def _limit_coordinates(self, coord):
        coord[0] = min(coord[0], self.shape[0] - 1)
        coord[0] = max(coord[0], 0)
        coord[1] = min(coord[1], self.shape[1] - 1)
        coord[1] = max(coord[1], 0)
        return coord
   
    #write a different function to calculate transistion probabilities
    def _calculate_transition_prob(self,current,delta,winds):
        return_list = []
        prob = [0.3333333333333,0.3333333333334,0.3333333333333]
        w_str = [-1,0,1]
        if winds[tuple(current)] == 0:
            new_position = np.array(current) + np.array(delta) 
            new_position = self._limit_coordinates(new_position).astype(int)
            new_state = np.ravel_multi_index(tuple(new_position), self.shape)
            is_done = tuple(new_position) == (3,7)
            return_list.append((1.0,new_state,-1.0,is_done))
        else:
            new_state = np.zeros(3)
            for i in range(3):
                new_position = np.array(current) + np.array(delta) + np.array([-1, 0]) * (winds[tuple(current)]+w_str[i])  
                new_position = self._limit_coordinates(new_position).astype(int)
                new_state = np.ravel_multi_index(tuple(new_position), self.shape)
                is_done = tuple(new_position) ==(3,7)
                return_list.append((prob[i],new_state,-1.0,is_done))
        return return_list
                
                
                
    def __init__(self):
        self.shape = (7, 10)

        nS = np.prod(self.shape)
        nA = 8

        # Wind strength
        winds = np.zeros(self.shape)
        winds[:,[3,4,5,8]] = 1
        winds[:,[6,7]] = 2

        # Calculate transition probabilities
        P = {}
        for s in range(nS):
            position = np.unravel_index(s, self.shape)
            P[s] = { a : [] for a in range(nA) }
            P[s][UP] = self._calculate_transition_prob(position, [-1, 0], winds)
            P[s][RIGHT] = self._calculate_transition_prob(position, [0, 1], winds)
            P[s][DOWN] = self._calculate_transition_prob(position, [1, 0], winds)
            P[s][LEFT] = self._calculate_transition_prob(position, [0, -1], winds)
            P[s][UP_RIGHT] = self._calculate_transition_prob(position, [-1, 1], winds)
            P[s][DOWN_RIGHT] = self._calculate_transition_prob(position, [1, 1], winds)
            P[s][DOWN_LEFT] = self._calculate_transition_prob(position, [1, -1], winds)
            P[s][UP_LEFT] = self._calculate_transition_prob(position, [-1, -1], winds)

        # We always start in state (3, 0)
        isd = np.zeros(nS)
        isd[np.ravel_multi_index((3,0), self.shape)] = 1.0

        super(WindyGridworldEnv, self).__init__(nS, nA, P, isd)

    def render(self, mode='human', close=False):
        self._render(mode, close)

    def _render(self, mode='human', close=False):
        if close:
            return

        outfile = StringIO() if mode == 'ansi' else sys.stdout

        for s in range(self.nS):
            position = np.unravel_index(s, self.shape)
            # print(self.s)
            if self.s == s:
                output = " x "
            elif position == (3,7):
                output = " T "
            else:
                output = " o "

            if position[1] == 0:
                output = output.lstrip()
            if position[1] == self.shape[1] - 1:
                output = output.rstrip()
                output += "\n"

            outfile.write(output)
        outfile.write("\n")
