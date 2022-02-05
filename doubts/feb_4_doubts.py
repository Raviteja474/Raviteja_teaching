var_1 = ([1,2,3],)

# support modification
var_1[0].append(4)

print(var_1)

# 1. u can't add

# don't support assignment but support modification
var_1 = (1,3,4)
# TypeError: 'tuple' object does not support item assignment
var_1[1]=4