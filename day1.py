
with open("input/day1.txt") as f:
    cals = [0]
    elf = 0
    for line in f:
        if line == "\n":
            elf += 1
            cals.append(0)
        else:
            cals[elf] += int(line)

    cals.sort()

    print (cals[-1])
    print (cals[-1] + cals[-2] + cals[-3])

    