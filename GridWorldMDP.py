"""
3 4
0 0 0 0
0 1 0 0
0 0 0 0
"""

import numpy as np


# List actions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def split_line(line):
    return [int(a) for a in line.strip().split(' ')]


class GridWorldMDP:

    def __init__(self, config, seed=2020):

        # Try to control the randomness
        self.rng = np.random.RandomState(seed)
        
        # Read input file
        self.input_file = config.get("input_file",
                                     "input.txt")

        self.M = 0
        self.N = 0
        self.A = None
        
        self.init_map()

        # Use dictionary to store rewards
        rewards = config.get("rewards", [])
        self.end_rewards = dict([((r[0], r[1]), r[2]) for r in rewards])

        self.noise = config.get("noise", 0.)
        self.living_cost = config.get("living_cost", 0.)
        self.actions = config.get("actions", [])

        self.start = config.get("start", None)

        # Parameters for each roll out of agent
        self.agent_position = None
        
    def init_map(self):
        with open(self.input_file, "r") as f:
            line1 = f.readline()
            a1 = split_line(line1)
            self.M = a1[0]
            self.N = a1[1]

            a = []
            for i in range(self.M):
                tmp = split_line(f.readline())
                a += [tmp]

        self.A = a
        # Debug
        print(a)
            

    def init(self):
        self.agent_position = self.start

    def get_number_of_actions(self):
        return len(self.actions)

    def step(self, action_index):
        assert 0<=action_index and action_index < self.get_number_of_actions()
        p_max = 1 - self.noise

        p = self.rng.rand()
        if p <= p_max:
            action = self.actions[action_index]
        else:
            # generating noise actions
            if self.rng.randint(10000) % 2 == 0:
                action_index += 1
            else:
                action_index -= 1

            action_index = (action_index + len(self.actions)) % len(self.actions)
            action = self.actions[action_index]

        agent_x = self.agent_position[0] + action[0]
        agent_y = self.agent_position[1] + action[1]

        if self.check_valid_state(agent_x, agent_y):
           self.agent_position = (agent_x, agent_y)

        reward = self.living_cost
        done = False

        if self.agent_position in self.end_rewards:
            done = True
            reward += self.end_rewards.get(self.agent_position, 0.)

        self.observation = self.get_observation()

        return self.observation,\
                reward,\
                done,\
                {}

    
    def get_observation(self):

        # Set default observation = self.position
        return self.agent_position

    def check_valid_state(self, x, y):
        if x < 0: return False
        if y < 0: return False
        if x >= self.M: return False
        if y >= self.N: return False

        if self.A[x][y] == 1:
            return False

        return True
               
    def generate_map(self, x, y):
        a = [list(tmp) for tmp in self.A]
        a[x][y] = 2

        return a


    #TODO: write transition function, T(s, a, s') and reward function
    def transition(self, state, action_index):
        n = len(self.actions)
        p = [0.0 for _ in range(n)]
        p[action_index] = 1 - self.noise
        p[(action_index + 1 + n)%n] = self.noise/2
        p[(action_index - 1 + n)%n] = self.noise/2

        list_states = []
        list_rewards = []

        for i in range(n):
            # TODO: write self.go generated new state rewards
            s1, r1 = self.go(state, i)
            list_state += [s1]
            list_rewards += [r1]

        return p, list_state, list_rewards




if __name__ == "__main__":
    print("Grid World MDP")
    cfg = {'input_file': 'input_file.txt',
           'rewards': [(0, 3, +1), (2, 3, -1)],
           'noise': 0.2,
           'living_cost': 0.,
           'actions': [UP, RIGHT, LEFT, DOWN],
           'start': (2, 0)}
    
    env = GridWorldMDP(cfg)
    env.init()

    start = env.get_observation()
    print("Start = ", start)

    np.random.seed(10)
    for i in range(10):
        action = np.random.randint(10000)%4
        s, r, d, _ = env.step(action)
        print("i = ", i)
        print("action = ", action)
        print(s, r, d)

        a = env.generate_map(s[0], s[1])
        for j in range(env.M):
            print(a[j])

