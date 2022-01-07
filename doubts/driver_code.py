# actual code, driver code
# __name__ 19@@ inheritance
# Driver code will call actual code
#actual code
import driver_code_import

def method_1():
    print("method_1")
    print(__name__)

if __name__ == "__main__":
    method_1()