from gym.envs.registration import register

register(
    id='bombman-v0'
    entry_point='gym-bombman/environment:BombmanEnv'
)

