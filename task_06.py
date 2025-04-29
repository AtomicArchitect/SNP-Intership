class WrongNumberOfPlayersError(Exception):
    def __init__(self, message = None):
        if message is None: self.message = "Wrong number of players"
        else: self.message = message

    def __str__(self):
        return self.message

class NoSuchStrategyError(Exception):
    def __init__(self, message = None):
        if message is None: self.message = "No such strategy"
        else: self.message = message

    def __str__(self):
        return self.message

def rps_game_winner(players):
    if len(players) != 2: raise WrongNumberOfPlayersError
    for player in players:
        if (len(player) != 2 or
                (player[1] != 'P' and
                player[1] != 'R' and
                player[1] != 'S')): raise NoSuchStrategyError("cheat player -> {}".format(player))
    return players[check_winning_hand(players[0][1], players[1][1]) - 1]

def check_winning_hand(first_player, second_player):
    if first_player == second_player: return 1
    if first_player == 'P':
        if second_player == 'S': return 2
        elif second_player == 'R': return 1
    elif first_player == 'R':
        if second_player == 'S': return 1
        elif second_player == 'P': return 2
    elif first_player == 'S':
        if second_player == 'R': return 2
        elif second_player == 'P': return 1
    return 1

print(rps_game_winner([['player1', 'S'], ['player2', 'P']]))
print(rps_game_winner([['player1', 'R'], ['player2', 'P']]))
print(rps_game_winner([['player1', 'S'], ['player2', 'R']]))
print(rps_game_winner([['player1', 'R'], ['player2', 'R']]))
# print(rps_game_winner([['player1', 'P'], ['player2', 'A']])) # NoSuchStrategyError: No such strategy
# print(rps_game_winner([['player1', 'P', 'S'], ['player2', 'A']])) # NoSuchStrategyError: No such strategy
# print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) # WrongNumberOfPlayersError: Wrong number of players