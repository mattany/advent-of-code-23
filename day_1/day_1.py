with open("day_1.txt", "r") as f:
    total = 0
    for l in f.readlines():
        for c in l:
            if c.isnumeric():
                total += 10 * int(c)
                break
        for c in l[::-1]:
            if c.isnumeric():
                total += int(c)
                break
    print(total)