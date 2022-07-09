import re

"""
It should have 12 digits
It should not start with 0 and 1
It should not contain alphabets and special characters
It should have white space after every digits
Ex --> 2345 4567 7891
"""

sample_adhar = "2345 4567 7891" # 2345 4567 7891 is a valid adhar number
# sample_adhar = "2345 4567 789" # Not a valid adhar number
# sample_adhar = "2345 4567 78945" # Not a valid adhar number
# sample_adhar = "2345456778945" # Not a valid adhar number
# sample_adhar = "0345 4567 78945" # Not a valid adhar number
# sample_adhar = "1345 4567 78945" # Not a valid adhar number
# sample_adhar = "5A45 45b7 7894" # Not a valid adhar number
# sample_adhar = "8345 4567 7891" # 8345 4567 7891 is a valid adhar number
# sample_adhar = "9345 4567 7891" # 9345 4567 7891 is a valid adhar number
# sample_adhar = " 9345 4567 7891  " # Not a valid adhar number
# sample_adhar = " 9345  4567  7891 " # Not a valid adhar number
# sample_adhar = "93 45 4567 7891" # Not a valid adhar number

# adhar_pattern = "^[2-9]{4} [0-9]{4} [0-9]{4}$"
# adhar_pattern = "^[2-9]{4}\s[0-9]{4}\s[0-9]{4}$"

# adhar_pattern = "^[2-9]{4} \d{4} \d{4}$"
adhar_pattern = "^[2-9]{4}\s\d{4}\s\d{4}$"

adhar_match = re.search(adhar_pattern, sample_adhar)

if adhar_match:
    print(f"{adhar_match.group()} is a valid adhar number")
else:
    print("Not a valid adhar number")

