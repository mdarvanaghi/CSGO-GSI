class PayloadParser:
    def __init__(self, gamestate_manager):
        self.gamestate_manager = gamestate_manager
        self.gamestate_changes = None

    def parse_payload(self, payload):
        self.gamestate_changes = {}

        # Parse round information from payload
        if 'round' in payload:
            self.parse_round_info(payload['round'])

        # Parse map information
        if 'map' in payload:
            self.parse_map_info(payload['map'])

        # Parse player informations

        # Pass game state changes to game state manager, if any
        if self.gamestate_changes:
            self.gamestate_manager.update_gamestate(self.gamestate_changes)

    def parse_round_info(self, round_info):
        # Parse bomb information
        # bomb                  ; "planted", "exploded", or "defused"
        if 'bomb' in round_info:
            if self.gamestate_manager.gamestate.round.bomb != round_info['bomb']:
                self.gamestate_changes['bomb'] = round_info['bomb']
        else:
            self.gamestate_manager.gamestate.round.bomb = ''
        
        # Parse win information
        # win_team              ; "CT" or "T"
        if 'win_team' in round_info:
            if not self.gamestate_manager.gamestate.round.win_team:
                self.gamestate_changes['win_team'] = round_info['win_team']
        else:
            self.gamestate_manager.gamestate.round.win_team = ''

        # Parse phase information
        # phase                 ; "live", "freezetime", "over" (maybe "warmup", others?)
        if 'phase' in round_info:
            if round_info['phase'] != self.gamestate_manager.gamestate.round.phase:
                self.gamestate_changes['round_phase'] = round_info['phase']

    def parse_map_info(self, map_info):
        # Parse team scores
        # - team_ct
        #         - score         ; int, current team score
        if 'team_ct' in map_info:
            if 'score' in map_info['team_ct']:
                self.gamestate_manager.gamestate.map.team_ct_score = map_info['team_ct']['score']
        # - team_t
        #         - score         ; int, current team score
        if 'team_t' in map_info:
            if 'score' in map_info['team_t']:
                self.gamestate_manager.gamestate.map.team_t_score = map_info['team_t']['score']

        # Parse round number
        # round                 ; int, current round number
        if 'round' in map_info:
            self.gamestate_manager.gamestate.map.round = map_info['round']