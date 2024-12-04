with open("input", "r") as f:
    file = f.read()

lines = file.split("\n")
pattern = [list(line) for line in lines]
count = 0

for line in pattern:
    for i in range(len(line) - 3):
        if (line[i] == 'X' and line[i+1] == 'M' and line[i+2] == 'A' and line[i+3] == 'S') or \
                (line[i] == 'S' and line[i+1] == 'A' and line[i+2] == 'M' and line[i+3] == 'X'):
            count += 1

for i in range(len(pattern[0])):
    for j in range(len(pattern) - 3):
        if (pattern[j][i] == 'X' and pattern[j+1][i] == 'M' and pattern[j+2][i] == 'A' and pattern[j+3][i] == 'S') or \
                (pattern[j][i] == 'S' and pattern[j+1][i] == 'A' and pattern[j+2][i] == 'M' and pattern[j+3][i] == 'X'):
            count += 1

for i in range(len(pattern[0]) - 3):
    for j in range(len(pattern) - 3):
        if (pattern[j][i] == 'X' and pattern[j+1][i+1] == 'M' and pattern[j+2][i+2] == 'A' and pattern[j+3][i+3] == 'S') or \
                (pattern[j][i] == 'S' and pattern[j+1][i+1] == 'A' and pattern[j+2][i+2] == 'M' and pattern[j+3][i+3] == 'X'):
            count += 1

        if (pattern[j+3][i] == 'X' and pattern[j+2][i+1] == 'M' and pattern[j+1][i+2] == 'A' and pattern[j][i+3] == 'S') or \
                (pattern[j+3][i] == 'S' and pattern[j+2][i+1] == 'A' and pattern[j+1][i+2] == 'M' and pattern[j][i+3] == 'X'):
            count += 1

print(count)
