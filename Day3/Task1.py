import re
with open("/home/simon/IdeaProjects/AoC24/Day3/input", "r") as f:
    file = f.read()
mul = 0
x = re.findall(r"mul\(([0-9]*),([0-9]*)\)",file)
for i in x:
    mul += (int(i[0])*int(i[1]))
print(mul)