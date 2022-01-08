import time

class SeatNotAvailable(Exception):
    pass

seat_number =0
cinema_done = False

persons = ["Ravi", "Avinash", "Bhrath", "Mahesh", "Visu", "Sumanth"]
persons_iter = iter(persons)


def seat_request(present_person):
    global seat_number
    seat_number= seat_number+1
    if seat_number<=5:
        print(f"person: {present_person} and seat: {seat_number}")
    else:
        print(f"For person: {present_person}, the seat not available.")

while True:
    try:
        starting_time= time.time()
        present_person = next(persons_iter)
        seat_request(present_person)
    except StopIteration as error:
        time.sleep(5)
        raise SeatNotAvailable(f"Sorry!{present_person} Seat not available, please wait until show is over.")
    finally:
        if time.time()-starting_time>5:
            print(f"{persons} Thanks for your visit!!")