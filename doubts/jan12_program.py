
name = "I am Sumanth"

def house():

    global name
    name = "I am Sasi"
    def room():

        global name
        name = "I am Sunil"
        print(f"Local: {name}")

    room()
    print(f"Enclosing: {name}")


house()
print(f"Global: {name}")


