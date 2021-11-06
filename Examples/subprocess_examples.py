# GUI(Graphical User Interface) operations with mouse/keyboard
# command/shell operations will be performed from terminal/command prompt

# write a python code to display your IP address.
# is google accessible

import subprocess
import time

# subprocess module used to execute a command locally on your machine and gets the result of the command.

# Popen method where we will give command and we will get output
# stdout : standard output
# stdin : standard input
# stderr: standard error
# return code : Tells it is failed or passed.

# we have run method in subprocess , first argument is command
# second argument is output of the command
# third argument is encoding (byte stream to string)
# check, shell(asl python program to execute this command on command prompt) 19@@

starting_time = time.time()

# Find out internet stability of your net for 180 seconds.
while True:
    if time.time()-starting_time > 180:
        break
    # run method have 4 parameters
    # ping www.google.com --> pings google send 4 packets and count how many packets received and how many lost.
    # stdout simply takes output after command execution in byte array form
    # encoding utf-8 will convert byte array to string
    # shell= True says that this command will be executed from command prompt from python
    output = subprocess.run("ping www.google.com", stdout=subprocess.PIPE, encoding="utf-8", shell=True)
    # output object contains 3 values i.e. stdout stderr return code
    # convert output to string
    output_string = output.stdout
    # checking whether is is string or not
    print(type(output.stdout))
    print(output.stderr)
    # return always should a non zero for successful command execution.
    print(output.returncode)

    print("_________________________________________________________________________________________________________________")

    # divides output based on new line.
    lines = output.stdout.split("\n")
    # iterating over lines
    for line in lines:
        # Looking for a string "Lost" to know how many packets lost
        if "Lost =" in line:
            # splitting into word based on space from a line.
            words = line.split(" ")
            print(words)
            # We have lost packet info at 14 th word(index 13)
            print(f"data packets lost is {words[13]}")

# _______________________________________________________________________________________________________
# b'\r\nPinging www.google.com [142.250.77.68] with 32 bytes of data:\r\nReply from 142.250.77.68: bytes=32 time=44ms TTL=120\r\nReply from 142.250.77.68: bytes=32 time=41ms TTL=120\r\nReply from 142.250.77.68: bytes=32 time=41ms TTL=120\r\nReply from 142.250.77.68: bytes=32 time=41ms TTL=120\r\n\r\nPing statistics for 142.250.77.68:\r\n    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\r\nApproximate round trip times in milli-seconds:\r\n    Minimum = 41ms, Maximum = 44ms, Average = 41ms\r\n'
# None


# b'Ping request could not find host www.google.com. Please check the name and try again.\r\n'
# None

# <class 'str'>
# None
# 1


