import sys

print(sys.version)


for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")

sys.stdout.write('Geeks')