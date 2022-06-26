"""
False	True	else	import	pass break		in
True		is	return and	continue	for
as	def	from		while
assert	del		not	 elif	if	or

return  None  in

any all
"""
import random
import time
user_name = input("Who are you?")
movies = ["kgf", "rrr", "v", "Vkram", "Major", "Minor", "kgf2"]

def copying_movie(user_name, movie):
    print(f"{user_name} copying the {movie}.")
    movie_time = random.randrange(1,10)
    start_time = time.time()
    for i in range(10):
        if time.time()-start_time>=8:
            print(f"{movie} taking more time to copy, let's fail this man.")
            return False
        if movie_time < time.time():
            time.sleep(1)
            print(f"Seconds:{i} over, remanining: {10-i} for movie: {movie}")
            return True
for movie in movies:
    print(f"movie: {movie} status: {copying_movie(user_name,movie)}")
    print("___________________________________________________________________")






