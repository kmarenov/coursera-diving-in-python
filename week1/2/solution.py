import sys

steps = int(sys.argv[1])

for step in range(1, steps + 1):
    line = ''

    for i in range(1, steps + 1):
        line += '#' if i > steps - step else ' '

    print(line)
