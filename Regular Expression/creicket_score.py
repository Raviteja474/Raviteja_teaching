import re

max_boundaries_player = "x"
max_sixes_player = "x"
max_sixes = 0
max_boundaries = 0

with open("score_card.txt", "r") as f:
    data = f.read()
    # print(data)
    lines = data.splitlines()
    # print(lines)
    for line in lines:
        player_pattern = re.compile(r".* \(")
        player_match = player_pattern.search(line)
        sixes_pattern = re.compile(r" \d+-6")
        sixes_match = sixes_pattern.search(line)
        boundaries_pattern = re.compile(r" \d+ ")
        boundaries_match = boundaries_pattern.search(line)
        if player_match:
            # print(player_match)
            # print(player_match.group()).
            player = player_match.group()
            currrent_player = player[:-2]
            # print(currrent_player)
            sixes = int(sixes_match.group()[:-2])
            # print(sixes)
            boundaries = int(boundaries_match.group()[1:-1])
            # print(boundaries)
            if sixes > max_sixes:
                max_sixes = sixes
                max_sixes_player = currrent_player

            if boundaries > max_boundaries:
                max_boundaries = boundaries
                max_boundaries_player = currrent_player

print(max_sixes_player, max_sixes)
print(max_boundaries_player, max_boundaries)

