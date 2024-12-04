import re
with open("input", "r") as f:
    file = f.read()
mul = 0
enabled = True
x = re.findall(r"(do\(\))|(don't\(\))|mul\(([0-9]*),([0-9]*)\)", file)
for i in x:
    if i[0] == "do()":
        enabled = True
    elif i[1] == "don't()":
        enabled = False
    elif enabled:
        mul += (int(i[2])*int(i[3]))
print(mul)