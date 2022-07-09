# def sample_func():
#     print("I am sample_func")
#     # it's logical to return some thing, in this case we are returning Nine
#     # return [1,2,3]
#
# a = sample_func()
# print(a[0])

#
# try:
#     print("I am try")
#     a = 1
#     b= 1000/a
# # except [Exception class] [as] [e]
# # except:
# except Exception as e:
#     # print(f"I am except")
#     print(f"I am except: {e}")
#     # I am except: division by zero
# else:
#     print(f"I am else")
# finally:
#     print("finally")
#     del a

try:
    a = 0
    print(100/a)
# child exception will get priority when compared to parent
except TypeError as e:
    print(f"Expecting ZeroDivisionError is: {e}")
except ZeroDivisionError as e:
    print(f"Expecting ZeroDivisionError is: {e}")
except Exception as e:
    print(f"Exception is: {e}")





