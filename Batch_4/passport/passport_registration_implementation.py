import time
import random

MALE_PAYMENT = 1000
FEMALE_PAYMENT = 500
OTHERS_PAYMENT = 200

# name = 'Ramyasree'
# for character in name:
#     print(ord(character))
def is_qualified(name,gender,age,application_id):
    for character in name:
        if 65<=ord(character)<=90 or 97<=ord(character)<=122:
            pass
        else:
            print(f"Invalid  name {name}.")
            return False
    if gender in ["male", "female", "others"]:
        print("Valid gender.")
    else:
        print(f"Invalid gender {gender}.")
        return False
    if 0<age<160:
        print("Valid age.")
    else:
        print(f"Invalid age {age}.")
        return False
    if 10000<application_id<20000:
        print("Valid application_id.")
    else:
        print(f"Invalid application_id {application_id}.")
        return False
    return True

def process_payment(name):
    time.sleep(3)
    print("Your payment processing.")
    print(f"{name} Your payment done. Your application ID {application_id}")

start_time = time.time()
print(f"Passport office opened at :{start_time}")
while time.time()-start_time<80:
    print("_"*100)
    # Taking input
    # sowjanya  valid
    # sowjanya12 invalid
    name = input("Please enter your name?")
    # male, female, others
    # lkflklk!!  invalid
    gender = input("Please enter your gender?")
    # 1-160 valid
    # -1 invalid
    # 787389 invalid
    age = int(input("Please enter your age?"))
    # 10000< application_id <20000
    application_id = random.randrange(10000,20000)
    qualify = is_qualified(name,gender,age,application_id)
    if qualify:
        if gender == "male":
            print(f"male: Please pay {MALE_PAYMENT}")
            process_payment(name)
        elif gender == "female":
            print(f"female: Please pay {FEMALE_PAYMENT}")
            process_payment(name)
        elif gender == "others":
            print(f"others :Please pay {OTHERS_PAYMENT}")
            process_payment(name)
    else:
        print("You are not qualified.")
else:
    print("Sorry! Please visit us again.")
