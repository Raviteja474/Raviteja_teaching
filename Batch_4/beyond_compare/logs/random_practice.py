import random
import time
# flip a coin
# outcome_list = ["Tail", "Head"]
# while True:
#     outcome = random.choice(outcome_list)
#     print(f"Filled a coin, You got: {outcome}")
#     time.sleep(0.4)

# x --> 16
# 0x12  -->18
#        --> 1*16^^1+2*16^^0 = 1*16+2*1 = 18
# o-->8
# 0o712 --> value*base^^postion = 1
#         --> 7*8^^2+1*8^^1+2*8^^0 = 448+8+2 = 458

# infinite loop --> 60 secs
# iterations --> 100 samples
sample_count = 0
while True:
    outcome_age = random.randrange(1, 140)
    print(f"outcome_age : {outcome_age}, sample_count: {sample_count}")
    time.sleep(0.1)
    # WRONG
    # sample_count=+1
    sample_count+=1
    if sample_count>100:
        break

# otp time.time()  105053

print(random.random())