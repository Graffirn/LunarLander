import numpy as np

class ValueAgent:

    def __init__(self, env):

        self.env = env

        # Note the gamma factor
        self.gamma = 0.9

        self.M = env.M
        self.N = env.N

        self.optimalValue = [[0. for _ in range(self.N)] for _ in range(self.M)]

    def value_iteration_1step(self):
        oldValue = self.optimalValue
        newValue = [[0. for _ in range(self.N)] for _ in range(self.M)]
        n = self.env.get_number_of_actions()

        for i in range(self.M):
            for j in range(self.N):
                maxValue = -1
                # TODO: for each action 0..n-1
                # call into enviroment to get T and R
                # compute and get the maxV
    
    # TODO: value iteration
    def value_iteration(self):
        
        for k in range(100):
            print(k)
            # Run value iteration until convergence
    
    
    # TODO: extract policy from optimalValue
    def extract_policy(self):
        policy = np.zeros((self.M, self.N), dtype = np.uint8)

        for i in range(self.M):
            for j in range(self.N):
                # TODO:
                #policy[i][j] = max stand at i, j, do action a 
                policy[i][j] = 0

class ValueAgent:

    def __init__(self, env):

        self.env = env

        # Note the gamma factor
        self.gamma = 0.9

        self.M = env.M
        self.N = env.N

        self.optimalValue = [[0. for _ in range(self.N)] for _ in range(self.M)]
        self.policy = np.zeros((self.M, self.N))

    def value_iteration_1step(self):
        oldValue = self.optimalValue
        newValue = [[0. for _ in range(self.N)] for _ in range(self.M)]
        n = self.env.get_number_of_actions()

        for i in range(self.M):
            for j in range(self.N):
                maxValue = -1
                # TODO: for action = self.policy[i][j]
                # call into enviroment to get T and R
                # compute and get the new V

    # TODO: value iteration
    def value_iteration(self):
        
        for k in range(100):
            print(k)
            # Run value iteration until convergence
    
    
    # TODO: extract policy from optimalValue
    def extract_policy(self):
        policy = np.zeros((self.M, self.N), dtype = np.uint8)

        for i in range(self.M):
            for j in range(self.N):
                # TODO:
                #policy[i][j] = max stand at i, j, do action a 
                policy[i][j] = 0


if __name__=="__main__":

    from GridWorldMDP import *
    print("Grid World MDP")
    cfg = {'input_file': 'input_file.txt',
           'rewards': [(0, 3, +1), (2, 3, -1)],
           'noise': 0.2,
           'living_cost': 0.,
           'actions': [UP, RIGHT, LEFT, DOWN],
           'start': (2, 0)}
    
    env = GridWorldMDP(cfg)
    env.init()

    agent = ValueAgent(env)

