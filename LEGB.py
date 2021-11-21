# Scope
# Local, Enclosed, Global, Builtin

# indentation 0 global variable
var_1 = "I am ISRO scientist."

def village():
    # non local variable defined within function
    var_1 ="I am classmate."
    def function_2():
        # local variable
        var_1 = "I am Brother."
        print(var_1)
    function_2()

village()

print("______________________________________")

var_1 = "I am ISRO scientist."
# overwriting/overriding the global variable
var_1 = "I am ISRO doctor."
print(var_1)

def function_3():
    # your change scope is local. If you want to change global variable normally, once it leaves function , values will not change.
    var_1 = "I am ISRO clerk."
    print(var_1)

function_3()
print(var_1)

print("___________________changing global variable value___________________")

var_1 = "I am ISRO scientist."
# overwriting/overriding the global variable
var_1 = "I am ISRO doctor."
print(var_1)

def function_3():
    # your change scope is local. If you want to change global variable normally, once it leaves function , values will not change.
    # indicating that I am going to change global variable
    global var_1
    var_1 = "I am ISRO clerk."
    print(var_1)

function_3()
print(var_1)


print("___________________not changing enclosed variable value___________________")


def function_4():
    var_3 = "I am Bank clerk."
    def function_5():
        print("______________I am called_____________________")
        var_3 = "I am Bank PO."
        print(var_3)
    function_5()
    print(var_3)

function_4()

print("___________________changing nonlocal variable value___________________")


def function_4():
    var_3 = "I am Bank clerk."
    print(var_3)
    def function_5():
        print("______________I am called_____________________")
        nonlocal var_3
        var_3 = "I am Bank PO."
        print(var_3)
    function_5()
    print(var_3)

function_4()

# 19@@ built in scope