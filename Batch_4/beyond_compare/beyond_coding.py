# folder 1, 2, 3
# folder a,b,c

# log 1.txt  --> log_10:21:17.txt
# log 2.txt  --> log_10:22:16.txt
# log 3.txt  --> log_10:23:16.txt

import logging
import random
import time

student_list= ["Raviteja","Bharath","Avinash","Ramya","Mahesh","Ganesh",
              "Visu","Sumanth"]
# 100 samples= 98 similar, 2 not similar

# Application : AP202U140[0-7]
# Name : Raviteja
# District : Nellore
# Disclaimer for EAMCET Exam:
# "Applicants must have cleared their 12th level exam from an AP/ Telangana accredited board or institution.
# Students applying must be at least 17 years old as of December 31, 2022. As of December 31, 2022, the upper age limit for all applicants is 22 years (25 years for SC/ ST).
# Students must have passed/appeared in Intermediate (12th) with PCM as an optional subject or an equivalent recognised by BIE Andhra Pradesh/ Telangana to be eligible for Pharma D. OR
# Students must have passed or be enrolled in the final year of a pharmacy diploma exam administered by SBTET in Andhra Pradesh or Telangana.
# Candidates must have received a grade of 45 per cent or above (40 per cent for reserved category candidates).
# Candidates must be 17 years old as of December 31, 2022, to be considered"
# Maths-1: random
# Maths-2:
# Physics:
# Chemistry:
# Rank:

APPLICATION = "AP202U140"
INFO = r'Disclaimer for EAMCET Exam:Applicants must have cleared their 12th level ' \
       r'exam from an AP/ Telangana accredited board or institution. Students applying' \
       r' must be at least 17 years old as of December 31, 2022. As of December 31, ' \
       r'2022, the upper age limit for all applicants is 22 years (25 years for SC/ ST).' \
       r' Students must have passed/appeared in Intermediate (12th) with PCM as an ' \
       r'optional subject or an equivalent recognised by BIE Andhra Pradesh/ Telangana ' \
       r'to be eligible for Pharma D. OR Students must have passed or be enrolled in the' \
       r' final year of a pharmacy diploma exam administered by SBTET in Andhra Pradesh ' \
       r'or Telangana. Candidates must have received a grade of 45 per cent or ' \
       r'above (40 per cent for reserved category candidates).Candidates must be ' \
       r'17 years old as of December 31, 2022, to be considered'

student_count = 0
for student in student_list:
    filename = r'D:\Raviteja_teaching\Batch_4\beyond_compare\logs\\'+student+'_rankcard.txt'
    print(f"Student: {student}, filename generated: {filename}")

    logging.basicConfig(filename=filename, format='%(message)s',
                        filemode='w+')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info(f"*" * 80)
    logger.info(f"Application : AP202U140{str(student_count)}")
    logger.info(f"Name : {student}")
    logger.info(f"District : Nellore")
    logger.info(INFO)

    maths_1 = random.randrange(10,40)
    logger.info(f"Maths-1: {maths_1}")
    maths_2 = random.randrange(10, 40)
    logger.info(f"Maths-2: {maths_2}")
    physics = random.randrange(10, 40)
    logger.info(f"Physics: {physics}")
    chemistry = random.randrange(10, 40)
    logger.info(f"Chemistry: {chemistry}")
    logger.info(f"{student} Total: {maths_1+maths_2+physics+chemistry}")
    time.sleep(0.5)
    student_count+=1

    # closing the handler
    handlers = logger.handlers[:]
    for handler in handlers:
        logger.removeHandler(handler)
        handler.close()
    logger.info(f"*" * 80)