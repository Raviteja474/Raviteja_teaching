import random

total_players = ["bharath","avinash","mahesh","visu","sumanth","ravi"]
dict_1={}

input_rounds= int(input("Enter number of rounds needed:"))

for round in range(1,input_rounds+1):
    print(f"____________round: {round} started____________________________")
    for player in range(len(total_players)):
        rolling_dice=random.randint(1,6)
        print(f"player: {total_players[player]} got value: {rolling_dice} in round {round}")
        if total_players[player] in dict_1.keys():
            dict_1[total_players[player]] += rolling_dice
        else:
            dict_1[total_players[player]]=rolling_dice
    print(f"____________round: {round} over____________________________\n")

print(dict_1)

max_value = max(dict_1.values())
print(f"max_value: {max_value}")

for key,value in dict_1.items():
    if max_value == dict_1[key]:
        print(f"{key} won the match.")