class Players:

    def __init__(self):
        """ Initializes Players instance. """

        self.current_player = 0
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

    def is_playable(self):
        """ Ensures the players instance attribute is playable with a value greater than 2. """
        return self.how_many_players >= 2

    def add_player(self, player_name):
        """ Adds a player with the specified name in the argument.  Calls a helper method to construct
        the initialized player attributes. """
        self.players.append(player_name)
        self._added_player_setup(player_name)

    def _added_player_setup(self, player_name):
        """ Constructs the initialized player attributes. """
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        self._player_added_confirmation(player_name)
        return True

    def _player_added_confirmation(self, player_name):
        """ Prints out a confirmation of the player being successfully added to the game. """
        print(player_name + " was added.\n"
                            "They are player number %s" % len(self.players))

    @property
    def how_many_players(self):
        """ Property getter to retrieve number of players through class's players attribute. """
        return len(self.players)
