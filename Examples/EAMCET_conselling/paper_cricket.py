# 0 2 4 6 8
# 10 wickets - 1 player
# 10 wickets - 2 player
import random
papers_list = [0, 2, 4,6,8]


def play_paper_cricket():
    wickets = 0
    total = 0
    while wickets<=10:
        paper_selected = random.choice(papers_list)
        print(f"paper_selected: {paper_selected}")
        total+=paper_selected
        print(f"Total: {total}, wickets: {wickets}")
        if paper_selected == 0:
            wickets+=1
            print("out!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return total


user_1 = input("Enter user name ?")
total_1 = play_paper_cricket()
print(f"{user_1} total : {total_1}")

user_2 = input("Enter user name ?")
total_2 = play_paper_cricket()
print(f"{user_2} total : {total_2}")

# ternary
# if statement output ,  condition , else else statement output
print("User 1 won!!") if total_1>total_2 else print("User 2 won!!")