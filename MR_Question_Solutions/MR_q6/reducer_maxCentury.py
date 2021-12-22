import sys

players = {}

for line in sys.stdin:
    line = line.strip()
    player, runs = line.split("\t")
    runs = int(runs)
    if player in players.keys():
        if runs>=100:
            players[player] += 1
    else:
        if runs>=100:
            players[player] = 1

player_max = ""
player_maxCenturies = 0
for player in players.keys():
    if players[player] > player_maxCenturies:
        player_max = player
        player_maxCenturies = players[player]
print("{}\t{}".format(player_max, player_maxCenturies))