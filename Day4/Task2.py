with open("input", "r") as f:
    file = f.read()

lines = file.split("\n")
pattern = [list(line) for line in lines]
count = 0

for i in range(len(pattern[0]) - 2):
    for j in range(len(pattern) - 2):
        if (pattern[j+1][i+1] == 'A' and
                (pattern[j][i] == 'M' and pattern[j+2][i+2] == 'S' and ((pattern[j+2][i] == 'M' and pattern[j][i+2] == 'S') or (pattern[j+2][i] == 'S' and pattern[j][i+2] == 'M')) or
                (pattern[j][i] == 'S' and pattern[j+2][i+2] == 'M' and ((pattern[j+2][i] == 'S' and pattern[j][i+2] == 'M') or (pattern[j+2][i] == 'M' and pattern[j][i+2] == 'S'))))):
            count += 1
print(count)