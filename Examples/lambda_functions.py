# use function? re-usability ,reduces repeatation


print("Ravi is son of Umamahesh.")
print("Avi is son of Ganesh.")
print("Sumanth is son of Srinivas.")
print("bharath is son of Narasimharao.")
print("Mahesh is son of Anjayya.")

def print_sun_father(son,father):
    print(f"{son} is son of {father}")

print_sun_father("Ravi","Umamahesh")
print_sun_father("Avi","Ganesh")
print_sun_father("Sumanth","Srinivas")
print_sun_father("bharath","Narasimharao")
print_sun_father("Mahesh","Anjayya")

# anonymous  function = labmda function = nameless function