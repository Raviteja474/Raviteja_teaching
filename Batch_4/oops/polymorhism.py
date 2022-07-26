print(sum([55,22]))
list_3 = [65,66,67,68,69,70,"Ravi"]

# DO I need to implement Meta class? 19@@
class Sample(type):
    def __sum__(self,list):
        list_2 = []
        for element in list:
            if type(element)==int:
                list_2.append(chr(element))
            else:
                list_2.append(element)
        return ''.join(list_2)



# sample = Sample()

print(sum(Sample()))

