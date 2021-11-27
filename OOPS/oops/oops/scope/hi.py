class A(object):
    __private_number =2
    def __new__(cls, a):
        print("Creating instance")
        return super(A, cls).__new__(cls)

    def __init__(self, a):
        self.a = a
        print("Initialse the values")

    def __call__(self, *args, **kwargs):
        print("@@@@@@@@@@called")

    def display_values(self):
        print(self.a)


a=A(2)
a()
a.display_values()
