

for number in range(10):
    try:
        print(f"Try block called for {number}")
        reminder = 100/number
    # e is a alias operand for exception
    except Exception as e:
        # This reachable for any exception.
        print(f"We have issues for {number} and error is {e}")
    finally:
        print(f"validation for {number} closed.")

try:
    value =100/0
except:
    print("wrong!!")

print("***********************************************")
for number in range(10):
    print(100/number)