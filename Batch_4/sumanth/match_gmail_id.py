import re

"""
It should start with lower case or uppercase characters
It should have alphanumeric characters and special characters
It must have @ symbol after above lines
It must ends with gmail.com

"""

# sample_gmail = "python.2022batch@gmail.com" # python.2022batch@gmail.com is a valid gmail
# sample_gmail = "python-2022batch@gmail.com" # python-2022batch@gmail.com is a valid gmail
# sample_gmail = "python_2022batch@gmail.com" # python_2022batch@gmail.com is a valid gmail
sample_gmail = "pyt34hon*2022batch@gmail.com"
# sample_gmail = "pyt34hon*2022batch@hotmail.com"

sample_string = "Python"

# gmail_pattern = "^[A-Za-z]+(\.|-|_|#)*[0-9a-zA-Z]+[@]+gmail\.com$"

# gmail_pattern = "^[A-Za-z][\w]+(\.|-|_|~|#|\*)*[\w+]*[@]+gmail\.com$"

# gmail_pattern = "^[A-Za-z][\w]+(\.|-|_|~|#|\*)*[\w+]*[@]+([a-z]{7}|[a-z]{5})\.com$"

gmail_pattern = "^[A-Za-z][\w]+(\.|-|_|~|#|\*)*[\w+]*[@]+(gmail\.com|hotmail\.com)$"
gmail_match = re.search(gmail_pattern, sample_gmail)

if gmail_match:
    print(f"{gmail_match.group()} is a valid gmail")
else:
    print("Not a valid gmail")


