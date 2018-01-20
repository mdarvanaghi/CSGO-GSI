import map
import player

class GameStateManager:
    def __init__(self):
        self.gamestate = GameState()

class GameState:
    def __init__(self):
        self.map = map.Map()
        self.player = player.Player()
        self.round_phase = ''

    def update_round_phase(self, phase):
        self.round_phase = phase
        print('Round phase: ' + phase)

    def update_round_kills(self, kills):
        if self.player.state.round_kills != kills and kills != 0:
            self.player.state.round_kills = kills
            print(self.player.name + ' got a kill.')

        if kills == 5:
            print(self.player.name + ' got an ace!')