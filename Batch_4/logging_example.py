import logging

# Create and configure logger
# 1. logname
# logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',
#                     filemode='w')
#
# # Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.WARNING)

# Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")

print("_____________________________________________________________________")
student_list=["raviteja","bharath","avinash","anjayya","mahesh","ganesh",
              "visu","sumanth", " ", " "]

student_dict = {}
for student in student_list:
    #student_dict[student] = len(student)
    total_letters = 0
    for letter in student:
        logger.debug(f"[LOG_DEBUG]: For {letter}, I am incrementing count.")
        total_letters = total_letters+1
    student_dict[student] = total_letters
    logger.info(f"[LOG_INFO] For {student}, I have created an item with "
                f"letters: {total_letters} ")
logger.warning(f"[LOG_WARNINGS] final dictionary: {student_dict}")

