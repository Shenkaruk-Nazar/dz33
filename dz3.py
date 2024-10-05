class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def list_players(self):
        return [str(player) for player in self.players]


if __name__ == "__main__":
    team = Team("Team")
    player1 = Player("Nick")
    player2 = Player("Kate")

    team.add_player(player1)


    print(f"Players {team.team_name}: {team.list_players()}")

    team.add_player(player2)

    team.remove_player(player1)

    print(f"Players {team.team_name}: {team.list_players()}")
