import subprocess
import time
starting_time = time.time()
while True:
    if time.time()-starting_time > 180:
        break
    output = subprocess.run("ping www.google.com", stdout=subprocess.PIPE, encoding="utf-8", shell=True)
    output_string = output.stdout
    print(type(output.stdout))
    print(output.stderr)
    print(output.returncode)
    lines = output.stdout.split("\n")
    for line in lines:
        if "Lost =" in line:
            words = line.split(" ")
            print(words)
            print(f"data packets lost is {words[13]}")
