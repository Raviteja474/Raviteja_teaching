print("Hello world!")

# for i in range(10):
#     if i==5:
#         person = input("Who born?")
#         # run time
#         print(f"Hey!! Special person {person} born.")
#     else:
#         print("This is normal month.")


gender = input("Enter the gender")
age = int(input("Enter the age"))

if gender == "male":
    if age >60:
        print("You are elgible for pension")
    else:
        print("You are not elgible for pension")
elif gender == "female":
    if age >50:
        print("You are elgible for pension")
    else:
        print("You are not elgible for pension")
else:
    if age >45:
        print("You are elgible for pension")
    else:
        print("You are not elgible for pension")
