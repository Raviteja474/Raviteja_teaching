# Is there pattern
# is there count variable
# Is there flag
# can we make it or break it
# prints for more understanding
# multiple for loops?
# Do I need to store intermediate values in list/dictionary
# identify error code by putting print statements or adding irrelavent elements as a separator



exemption_count = 0

salary_list = [2,3,4,5,6,3,9,10,10, 10, 10, 11,12,9,8,7,6]
month = 0
same_salary = 0

for index in range(len(salary_list)):
    if salary_list[index] <= salary_list[index + 1] :
        if salary_list[index] == salary_list[index + 1]:
            same_salary+=1
            if same_salary>2:
                break
        print(salary_list[index],salary_list[index+1])
        month+=1
    else:
        exemption_count+=1
        if exemption_count>1:
            break
print(month)