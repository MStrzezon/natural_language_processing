with open("../resources/voynich.txt", "r") as f:
    lines = f.readlines()
with open("../resources/voynich.txt", "w") as f:
    for line in lines:
        if line[0] != '':
            f.write(line)