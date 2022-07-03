import re

input_string = """This is an example of regular expressions matchings This
Python 98
Mr.. Mahesh Btech
Mr. Bharath Btech
Mr.. Avinash Btech
Mr. Visweswar Btech
Mr Sumanth Btech
6300906188 87657656757
+916300906188
# 29589556556595
1548485956595599
9652841530
+919652841530
sumanth-ketharaju
$%^&**+-.><?
an
"""

# pattern = re.compile(r"^This") #matched <re.Match object; span=(0, 4), match='This'>
# pattern = re.compile(r"^T") #matched <re.Match object; span=(0, 1), match='T'>
# pattern = re.compile(r"^h")  # not matched None
# pattern = re.compile(r".") #matched # pattern = re.compile(r"..") #matched
# pattern = re.compile(r"...") #matched <re.Match object; span=(0, 2), match='Th'>
# pattern = re.compile(r"\.") #matched <re.Match object; span=(16, 17), match='.'>
# pattern = re.compile(r"[e]") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r"[Mr]") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r"[1-9]00") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r"[0-9]") #matched <re.Match object; span=(43, 53), match='6300906138'>
# pattern = re.compile(r"[0-9]+") #matched <re.Match object; span=(43, 53), match='6300906138'>
# pattern = re.compile(r"[0-9]{9,15}") #matched <re.Match object; span=(43, 53), match='6300906138'>23@@
# pattern = re.compile(r"[0-9]{19}") #matched <re.Match object; span=(43, 53), match='6300906138'>23@@
# pattern = re.compile(r"Mr") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r".+an") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r".*an") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r".?an") #matched <re.Match object; span=(2, 3), match='i'>
# pattern = re.compile(r"Avinash") #matched <re.Match object; span=(100, 107), match='Avinash'>
# pattern = re.compile(r"is|Python") #matched <re.Match object; span=(0, 4), match='This'>
# pattern = re.compile(r"\?$") #matched <re.Match object; span=(276, 277), match='?'>
# pattern = re.compile(r"an$") # not matched None
# pattern = re.compile(r"n$") # not matched None
# pattern = re.compile(r"a$") # not matched None
# Mr.. Mahesh Btech
# pattern = re.compile(r"Mr\.+\s[A-Z][a-z]+\sBtech") #matched <re.Match object; span=(59, 70), match='Mr.. Mahesh'>
# pattern = re.compile(r"Mr\.?s[A-Z][a-z]+\sBtech") #matched <re.Match object; span=(77, 94), match='Mr. Bharath Btech'>
# pattern = re.compile(r"Mr\.*\s[A-Z][a-z]+") #matched <re.Match object; span=(77, 88), match='Mr. Bharath'>
# pattern = re.compile(r"[a-zA-Z0-9]") #matched <re.Match object; span=(0, 1), match='T'>
# pattern = re.compile(r"[a-zA-Z0-9]+") #matched <re.Match object; span=(4, 5), match=' '>
# pattern = re.compile(r"[^a-zA-Z0-9]") #matched <re.Match object; span=(4, 5), match=' '>


print("-------------------search method--------------------------------")
this_pattern = r"^This"
matches = re.search(this_pattern, input_string)
print(matches)

#
# print("-------------------findall method--------------------------------")
#
# matches_2 = pattern.findall(input_string)
# print(matches_2)

