import time
# coverability(reachability)
# maintainability
# scalability(extensible)
age =3
class Theater():
    def sound_system(self):
        print("Normal sound_system")
    def picture_quality(self):
        print("Normal picture_quality")
        if age:
            return True
        else:
            # unreachable code
            return False

# Mainitainable, when you have requirement change we should develope a  script with least statements.

print("Enter into theater")
time.sleep(1)
print("Sanitize hands")
time.sleep(1)
print("Follow queue line")
time.sleep(1)
print("Occupy your seat")
time.sleep(1)
print("Enjoy movie")
time.sleep(1)

actions = ["Enter into theater", "Sanitize hands", "Follow queue line", "Occupy your seat", "Enjoy movie"]
for action in actions:
    print(action)
    time.sleep(1)



