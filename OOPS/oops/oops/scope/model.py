class Model:

    def __init__(self, m1=1, m2=2, m3=3):
        self.m1 = m1
        self._m2 = m2
        self.__m3 = m3
        print("Model constructor called..")


