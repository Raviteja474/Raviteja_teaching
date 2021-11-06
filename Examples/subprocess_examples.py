# GUI(Graphical User Interface) operations with mouse/keyboard
# command/shell operations will be performed from terminal/command prompt

# write a python code to display your IP address.
# is google accessible

import subprocess
import time


# Popen method where we will give command and we will get outpou
# stdout : standard output
# stdin : standard input
# stderr: standard error
# return code : Tells it is failed or passed.

# we have run method in subprocess , first argument is command
# second argument is output of the command
# third argument is encoding (byte stream to string)
# check, shell(asl python program to execute this command on command prompt) 19@@

starting_time = time.time()

while True:
    if time.time()-starting_time > 180:
        break
    output = subprocess.run("ping www.google.com", stdout=subprocess.PIPE, encoding="utf-8", shell=True)
    # output contains stdout stderr return code
    # convert output to string
    output_string = output.stdout
    # checking whether is is string or not
    print(type(output.stdout))
    print(output.stderr)
    # return always should a non zero for successful command execution.
    print(output.returncode)

    print("_________________________________________________________________________________________________________________")

    # divides output based on line.
    lines = output.stdout.split("\n")

    for line in lines:
        if "Lost =" in line:
            words = line.split(" ")
            print(words)
            print(f"data packets lost is {words[13]}")




# _______________________________________________________________________________________________________
# b'\r\nPinging www.google.com [142.250.77.68] with 32 bytes of data:\r\nReply from 142.250.77.68: bytes=32 time=44ms TTL=120\r\nReply from 142.250.77.68: bytes=32 time=41ms TTL=120\r\nReply from 142.250.77.68: bytes=32 time=41ms TTL=120\r\nReply from 142.250.77.68: bytes=32 time=41ms TTL=120\r\n\r\nPing statistics for 142.250.77.68:\r\n    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\r\nApproximate round trip times in milli-seconds:\r\n    Minimum = 41ms, Maximum = 44ms, Average = 41ms\r\n'
# None


# b'Ping request could not find host www.google.com. Please check the name and try again.\r\n'
# None

# <class 'str'>
# None
# 1


