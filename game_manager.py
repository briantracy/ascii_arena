
import shared

class Player:

    def __init__(self, userid, username):
        self.userid   = userid
        self.username = username
        self.x = 0
        self.y = 0

    def reset():
        self.kills  = 0
        self.deaths = 0

class GameManager:

    def player_joined(self, userid):
        pass

    def player_left(self, userid):
        pass

    def player_attempt_action(self, userid, action, direction):
        pass
