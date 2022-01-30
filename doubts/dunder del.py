import time


class Employee:

    # @classmethod
    # def get_delete(cls):
    #     del()
    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

    def delete1(self,obj_sample):
        del (obj_sample)



obj = Employee()
obj_1 = Employee()
print(dir(Employee))

print(obj)
print(obj_1)

# __del__ we can delete
# print(obj)
# del(obj)
# print(obj)

# for i in range(10):
#     time.sleep(1)
#     print("hi")
#19@@
#obj_1.delete1(obj)
print("__________________________________________________________")
print(obj)

sentence = 'I am an indian.'
final_list = dict(map(lambda x: x+1, sentence))
print(final_list)