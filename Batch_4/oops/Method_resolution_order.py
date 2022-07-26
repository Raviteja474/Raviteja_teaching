# think, eat, sleep, run, fight, walk
# object is super parent of all classes
# class A(object):
class A:
    def think(self):
        print("A think")
    def eat(self):
        print("A think")
class B(A):
    def run(self):
        print("B run")
    def eat(self):
        print("B eat")
class C(B,A):
    def fight(self):
        print("C fight")
    def walk(self):
        print("C walk")
class D(B):
    def sleep(self):
        print("D sleep")
    def walk(self):
        print("D walk")
    def about(self):
        print("D about")
a= A()
b= B()
c= C()
d= D()
c.eat()
d.think()
# d.walk()
# d.run()