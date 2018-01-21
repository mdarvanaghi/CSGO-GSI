import round
import map
import player
import time

class GameStateManager():
    def __init__(self):
        self.gamestate = GameState()

    def update_gamestate(self, gamestate_changes):
        if 'bomb' in gamestate_changes:
            self.gamestate.round.bomb = gamestate_changes['bomb']
            self.bomb_event(gamestate_changes['bomb'])

        if 'round_phase' in gamestate_changes:
            self.gamestate.round.phase = gamestate_changes['round_phase']
            if self.gamestate.round.phase == 'live':
                self.round_goes_live()
            elif self.gamestate.round.phase == 'over':
                self.round_over()

        if 'win_team' in gamestate_changes:
            self.gamestate.round.win_team = gamestate_changes['win_team']
            self.team_wins(gamestate_changes['win_team'])

    # Override these functions with cool audio-visual effects
    def round_goes_live(self):
        print(time.asctime())
        print('ROUND IS LIVE')

    def round_over(self):
        print('ROUND HAS ENDED')

    def bomb_event(self, event):
        print('BOMB' + (' ' if event == 'exploded' else ' HAS BEEN ') + str(event).upper() + '!')

    def team_wins(self, team):
        print(('Terrorists' if team == 'T' else 'Counter-Terrorists') + ' win!\n')

class GameState:
    def __init__(self):
        self.round = round.Round()
        self.map = map.Map()
        self.player = player.Player()

    def update_round_phase(self, phase):
        self.round_phase = phase
        print('Round phase: ' + phase)

    def update_round_kills(self, kills):
        if self.player.state.round_kills != kills and kills != 0:
            self.player.state.round_kills = kills
            print(self.player.name + ' got a kill.')

        if kills == 5:
            print(self.player.name + ' got an ace!')