try:
    a= 10
    #print(b); NameError
    c = "Ravi"+2 #TypeError
    b = 10/0 # ZeroDivisionError:

except NameError as n:
    print("NameError")
    print(n)
except ZeroDivisionError as e:
    print(f"Error is {e}")

except TypeError as e2:
    print(e2)

except Exception as e1:
    print(f"Parent error is {e1}")
else:
    print("When no exception called else will be called.")
