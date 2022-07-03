import re

input_string = r"This       is pycharm ide This is 99  mobile number   6300906133 we have 9502764652 @#$%^&*!?/| This"

# pattern = re.compile("\AThis") #matched <re.Match object; span=(0, 4), match='This'>
# pattern = re.compile("\AT") #matched <re.Match object; span=(0, 1), match='T'>
# pattern = re.compile("\Ah") #not matched None
# pattern = re.compile("\Anumber") #not matched None
# pattern = re.compile("\Bis")  #matched <re.Match object; span=(3, 5), match='is'>
# pattern = re.compile("Th\b")  #23@@
# pattern = re.compile("\d") #matched <re.Match object; span=(46, 47), match='6'>
# pattern = re.compile("\d+") #matched <re.Match object; span=(46, 56), match='6300906133'>
# pattern = re.compile("\D") #matched <re.Match object; span=(0, 1), match='T'>
# pattern = re.compile("\D+") #matched <re.Match object; span=(0, 45), match='This    is pycharm ide This is mobile number '>
# pattern = re.compile("\s") #matched <re.Match object; span=(4, 5), match=' '>
# pattern = re.compile("\s+") #matched <re.Match object; span=(4, 8), match='    '>
# pattern = re.compile("\S") #matched <re.Match object; span=(0, 1), match='T'>
# pattern = re.compile("\S+") #matched <re.Match object; span=(0, 4), match='This'>
# pattern = re.compile("\w") #matched <re.Match object; span=(0, 1), match='T'>
# pattern = re.compile("\w+") #matched <re.Match object; span=(0, 4), match='This'>
# pattern = re.compile("This\Z") #matched <re.Match object; span=(87, 91), match='This'>
pattern = re.compile("s\Z") #matched <re.Match object; span=(90, 91), match='s'>
# pattern = re.compile("i\Z") #not matched None
# pattern = re.compile("number\Z") #not matched None
# pattern = re.compile("\ZThis") #not matched None

matches = pattern.search(input_string)
print(matches)

print("---------------------------------------------------")
matches_2 = pattern.findall(input_string)
print(matches_2)