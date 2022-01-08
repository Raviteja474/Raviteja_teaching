import time
class SeatNotAvailable(Exception):
    pass

def theater():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Driver code to check above generator function
# for value in generator_obj:
#     print(value)
theater_entry = theater()

persons = ["Ravi","Avinash","Bhrath","Mahesh","Visu","Sumanth"]


def seat_request(seat_no):
    print(f"person: {person} and seat: {theater_entry.__next__()}")
    
try:
    for person in persons:
        seat_request(person)
except StopIteration as error:
    raise SeatNotAvailable(f"Sorry!{person} Seat not available, please wait until show is over.")
finally:
    print(f"{persons} Thanks for your visit!!")






