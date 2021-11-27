class Class_1:

    def len(self, list_):
        return 1

    def sum(self, a, b):
        return f"{a} adds {b} is equal to {a+b}"

    # overriding
    def sum(self, c, d):
        return f"{c} adds {d} is equal(s) to {c+d}"


class1 = Class_1()

print(len([1,2]))
print(class1.len([1,2,3,4,5]))
print(class1.len([1,2]))
print(sum([1,2]))
print(class1.sum(1,2))
