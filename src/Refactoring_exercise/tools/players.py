class Players:

    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

    def is_playable(self):
        return self.how_many_players >= 2

    def add_player(self, player_name):
        self.players.append(player_name)
        self._added_player_setup(player_name)

    def _added_player_setup(self, player_name):
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        self._player_added_confirmation(player_name)

        return True

    def _player_added_confirmation(self, player_name):
        print(player_name + " was added.\n"
                            "They are player number %s" % len(self.players))

    @property
    def how_many_players(self):
        return len(self.players)