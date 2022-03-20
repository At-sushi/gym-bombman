import json, subprocess, sys

import gym
import gym.spaces


PATH_SERVER = 'BombmanServer;BombmanServer\gson-2.3.1.jar;'
CLASS_SERVER = 'BombmanServer'

class BombmanEnv(gym.Env):
    def __init__(self):
        self._server = subprocess.run(['java', '-classpath', PATH_SERVER, CLASS_SERVER])

    def _reset(self):

    def _step(self, action):

    def _render(self):

