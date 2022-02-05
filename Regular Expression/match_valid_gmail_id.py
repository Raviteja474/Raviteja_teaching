import re
# valid_gamil = "sumanth.@$-_K123@gmail.com"
# valid_gamil = "suma45nth.@$@-_K123@gmail.com"
#
# gmail_pattern = re.compile(r"^[A-Za-z][\w]+(\.|@|\$|-|_)*[\w+]*[@]+gmail\.com$")
# gmail_match = gmail_pattern.search(valid_gamil)
# print(gmail_match)
# if gmail_match:
#     print(gmail_match.group())
#     print("valid gmail")
# else:
#     print("Not a valid gmail")

with open("score_card.txt", "r") as f:
    data = f.read()
    lines = data.splitlines()
    for line in lines:
        gmail_pattern = re.compile(r"^[A-Za-z][\w]+(\.|@|\$|-|_|~)*[\w+]*[@]+[a-z]{1,9}\.([a-z]{1,5}\.)*[a-z]{1,5}$")
        gmail_match = gmail_pattern.search(line)
        if gmail_match:
            print(gmail_match.group())

