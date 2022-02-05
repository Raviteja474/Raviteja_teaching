import re

input_string = r"This sai is pycharm .ide This is mobile number 6300906138 we have 9502764952 @#$%^&*!?/| This 1"


# pattern = re.compile(r"^This") #matched <re.Match object; span=(0, 4), match='This'>
# pattern = re.compile(r"^T") #matched <re.Match object; span=(0, 1), match='T'>
# pattern = re.compile(r"^h") # not matched None
# pattern = re.compile(r".") #matched # pattern = re.compile(r"..") #matched
# pattern = re.compile(r"...") #matched <re.Match object; span=(0, 2), match='Th'>
# pattern = re.compile(r"\.") #matched <re.Match object; span=(16, 17), match='.'>
# pattern = re.compile(r"is+") #matched <re.Match object; span=(2, 4), match='is'>
# pattern = re.compile(r"is*") #matched <re.Match object; span=(2, 4), match='is'>23@@
# pattern = re.compile(r"is?") #matched <re.Match object; span=(2, 4), match='is'>
# pattern = re.compile(r"is") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r"[ise]") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r"[a-zA-Z0-9]") #matched <re.Match object; span=(0, 1), match='T'>
# pattern = re.compile(r"[^a-zA-Z0-9]") #matched <re.Match object; span=(4, 5), match=' '>
# pattern = re.compile(r"63+") #matched <re.Match object; span=(43, 45), match='63'>
# pattern = re.compile(r"[0-9]+") #matched <re.Match object; span=(43, 53), match='6300906138'>
# pattern = re.compile(r"^[0-9]{10}$") #matched <re.Match object; span=(43, 53), match='6300906138'>23@@
# pattern = re.compile(r"is|This") #matched <re.Match object; span=(0, 4), match='This'>
# pattern = re.compile(r"([a-zA-Z]+|[0-9]{10})") #matched <re.Match object; span=(0, 4), match='This'>
# pattern = re.compile(r"1$") #matched <re.Match object; span=(90, 91), match='1'>
# pattern = re.compile(r"1$") # not matched None


print("--------------------------------------search method----------------------------------------")
matches = pattern.search(input_string)
print(matches)


print("--------------------------------------finditer method----------------------------------------")
matches = pattern.finditer(input_string)
for match in matches:
    print(match)




# matches = pattern.finditer(input_string)
# for match in matches:
#     print(match)
# if match it returns address like
# <callable_iterator object at 0x000002638EC24400>
# <re.Match object; span=(90, 91), match='1'>

# else it returns address
# <callable_iterator object at 0x000002548F4F4400>

# ---------------------------------------------------------------------------------------------
# matches = pattern.findall(input_string)
# print(matches)
# if match it returns matched elements within a list
# ['is', 'is', 'is', 'is', 'is']

# else returns empty list like
# []

# ---------------------------------------------------------------------------------------------

# matches = pattern.search(input_string)
# print(matches)
# if match it returns span,matched elements like as
# <re.Match object; span=(2, 4), match='is'>
#
# else returns None
# None
# ---------------------------------------------------------------------------------------------

# matches = pattern.match(input_string) #23@@
# if match it returns
# None
#
# else returns None
# None
# ---------------------------------------------------------------------------------------------

# matches = pattern.split(input_string)
# print(matches)
# if match it splits the string where match occurs at the same time matched element is not in that list  like as
# ['Th', ' ', ' pycharm .ide Th', ' ', ' mobile number 6300906138 we have 9502764952 @#$%^&*!?/| Th', ' 1']
#
# else returns original string within a list
# ['This is pycharm .ide This is mobile number 6300906138 we have 9502764952 @#$%^&*!?/| This 1']
# ---------------------------------------------------------------------------------------------

# matches = pattern.sub("as", input_string)
# print(matches)
# if match it returns the string with replaced element like
# Thas as pycharm .ide Thas as mobile number 6300906138 we have 9502764952 @#$%^&*!?/| Thas 1
#
# else returns original string
# This is pycharm .ide This is mobile number 6300906138 we have 9502764952 @#$%^&*!?/| This 1

# matches = pattern.sub("as", input_string, count=1)
# print(matches)
# if match it returns the string with only 2 replaced element like
# Thas as pycharm .ide This is mobile number 6300906138 we have 9502764952 @#$%^&*!?/| This 1
# ---------------------------------------------------------------------------------------------

# matches = pattern.subn("as", input_string)
# print(matches)
# if match it returns tuple containing string with replaced element and count of how many times the element is replaced
# ('Thas as pycharm .ide Thas as mobile number 6300906138 we have 9502764952 @#$%^&*!?/| Thas 1', 5)
#
# else returns tuple containing original string and count as 0
# ('This is pycharm .ide This is mobile number 6300906138 we have 9502764952 @#$%^&*!?/| This 1', 0)

# matches = pattern.subn("as", input_string, count=2)
# print(matches)
# if match it returns tuple containing string with 2replaced element and count of how many times the element is replaced
# ('Thas as pycharm .ide This is mobile number 6300906138 we have 9502764952 @#$%^&*!?/| This 1', 2)
# ---------------------------------------------------------------------------------------------


