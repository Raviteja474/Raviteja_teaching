student_list=["raviteja","bharath","avinash","anjayya","mahesh","ganesh",
              "visu","sumanth", " ", " "]

# dictionary
# {"raviteja":8,"bharath": 7}

# dict[4] ="four"
# dict[4] ="four1"
try:
    student_dict = {}
    for student in student_list:
        student_dict[student] = len(student)
    print("Before",student_dict)
except:
    print("except")
finally:
    # 19@@ Ravi, address this,- dictionary pop in iteration
    # for key,value in student_dict.items():
    #     if " " in key:
    #         student_dict.pop(key)
    student_dict.pop(" ")
print("After",student_dict)


# try:
#     pass
# except:
#     pass
# finally:
#     # pass
#     # remove nulls
