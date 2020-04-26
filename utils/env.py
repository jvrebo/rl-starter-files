import gym
from gym_minigrid.wrappers import *

def make_env(env_key, seed=None):
    env = gym.make(env_key)
    # env = ImgObsWrapper(env)
    env = DirectionObsWrapper(env, 'angle') # Provides the angular direction to the goal 
    env = DirectionBonus(env) # Add a bonus if the step was towards the goal.
    # env.seed(seed)
    return env
    