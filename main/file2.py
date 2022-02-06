import file_1
print("hi2")

def file2_me():
    print("I am file2_me")
#If you import the guardless script in another script (e.g. import my_script_without_a_name_eq_main_guard), then the second script will trigger the first to run at import time and using the second script's command line arguments. This is almost always a mistake
if __name__ == "__main__":
    file2_me()