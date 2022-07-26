import math
print("1@@",math.pi)

pi = 3.5

def function_2():
    pi=3.6
    def function_3():
        pi = 3.7
        def function_4():
            pi = 3.8
            def function_5():
                pi = 3.9
                print("6@@", pi)
            print("5@@", pi)
            function_5()
        print("4@@", pi)
        function_4()
    function_3()
    print("3@@", pi)
print("2@@",pi)
function_2()