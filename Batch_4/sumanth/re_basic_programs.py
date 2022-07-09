import re

# ^[]*+?()./|$

# input_string = "Ts is Pychram .IDE to write python code"
# print(input_string.split())
# starting_word = "This"
# if input_string.startswith(starting_word):
#     print(f"Yes given string starting with 'This' like ---> {input_string}")
# else:
#     print(f"given string not starting with 'This', this is starting with {input_string.split()[0]} like ---> {input_string}")

# -----------------------------------------------------------------------------------------------------------------------------
# input_string = "Ts is Pychram .IDE to write python code"
# starting_word_pattern = "^This"
# this_word_match = re.search(starting_word_pattern, input_string)
#
# if this_word_match:
#     print("Matched --> ", this_word_match)
#     print(f"Our string pattern was '{starting_word_pattern}', yes given starting with '{this_word_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{starting_word_pattern}', Not matched")

# -----------------------------------------------------------------------------------------------------------------------------

# input_string = "This is Pychram .IDE to write python code"
# is_pattern = "[is]"
# is_match = re.search(is_pattern, input_string)
#
# if is_match:
#     print("Matched --> ", is_match)
#     print(f"Our string pattern was '{is_pattern}', yes given string having '{is_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{is_pattern}', Not matched")

# -----------------------------------------------------------------------------------------------------------------------------

# input_string = "This is Pychram .IDE to write python code"
# is_pattern = "(is)"
# is_match = re.search(is_pattern, input_string)
# if is_match:
#     print("Matched --> ", is_match)
#     print(f"Our string pattern was '{is_pattern}', yes given string having '{is_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{is_pattern}', Not matched")

# -----------------------------------------------------------------------------------------------------------------------------

# input_string = "This is Pychram .IDE to write python code"
# s_is_p_pattern = "s is P"
# s_is_p_match = re.search(s_is_p_pattern, input_string)
# if s_is_p_match:
#     print("Matched --> ", s_is_p_match)
#     print(f"Our string pattern was '{s_is_p_pattern}', yes given string having '{s_is_p_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{s_is_p_pattern}', Not matched")

# -----------------------------------------------------------------------------------------------------------------------------
#
# input_string = "This s Pychram .IDE to write python code"
# s_is_p_pattern = "s [is] P"
# s_is_p_match = re.search(s_is_p_pattern, input_string)
# if s_is_p_match:
#     print("Matched --> ", s_is_p_match)
#     print(f"Our string pattern was '{s_is_p_pattern}', yes given string having '{s_is_p_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{s_is_p_pattern}', Not matched")

# # -----------------------------------------------------------------------------------------------------------------------------
#
# input_string = "This is Pychram .IDE to write python code"
# s_is_p_pattern = "s [is]+ P"
# s_is_p_match = re.search(s_is_p_pattern, input_string)
# if s_is_p_match:
#     print("Matched --> ", s_is_p_match)
#     print(f"Our string pattern was '{s_is_p_pattern}', yes given string having '{s_is_p_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{s_is_p_pattern}', Not matched")

# # -----------------------------------------------------------------------------------------------------------------------------
#
# input_string = "This is Pychram .IDE to write python code"
# s_is_p_pattern = "s [is]* P"
# s_is_p_match = re.search(s_is_p_pattern, input_string)
# if s_is_p_match:
#     print("Matched --> ", s_is_p_match)
#     print(f"Our string pattern was '{s_is_p_pattern}', yes given string having '{s_is_p_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{s_is_p_pattern}', Not matched")


# # -----------------------------------------------------------------------------------------------------------------------------
#
# input_string = "This is Pychram .IDE to write python code"
# s_is_p_pattern = "s i[s]? P"
# s_is_p_match = re.search(s_is_p_pattern, input_string)
# if s_is_p_match:
#     print("Matched --> ", s_is_p_match)
#     print(f"Our string pattern was '{s_is_p_pattern}', yes given string having '{s_is_p_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{s_is_p_pattern}', Not matched")

# -----------------------------------------------------------------------------------------------------------------------------
#
# input_string = "This is Pychram .IDE to write python code"
# p_to_m_patten = "P.....m"
# p_to_m_match = re.search(p_to_m_patten, input_string)
# if p_to_m_match:
#     print("Matched --> ", p_to_m_match)
#     print(f"Our string pattern was '{p_to_m_patten}', yes given string having '{p_to_m_match.group()}', like --> {input_string}")
# else:
#     print(f"Our string pattern was '{p_to_m_patten}', Not matched")

# -----------------------------------------------------------------------------------------------------------------------------


# input_string = "This is Pychram .IDE to write python code"
# print(input_string.split())
# ending_word = "code"
# if input_string.endswith(ending_word):
#     print(f"Yes given string endswith 'code' like ---> {input_string}")
# else:
#     print(f"given string not ending with 'code', this is ending with '{input_string.split()[-1]}' like ---> {input_string}")

# -----------------------------------------------------------------------------------------------------------------------------
input_string = "Ts is Pychram .IDE to write python code"
ending_word_pattern = "code$"
ending_word_match = re.search(ending_word_pattern, input_string)

if ending_word_match:
    print("Matched --> ", ending_word_match)
    print(f"Our string pattern was '{ending_word_pattern}', yes given starting with '{ending_word_match.group()}', like --> {input_string}")
else:
    print(f"Our string pattern was '{ending_word_pattern}', Not matched")
