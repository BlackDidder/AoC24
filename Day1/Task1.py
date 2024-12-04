with open("input", "r") as f:
    file=f.read()
lines=file.splitlines()
leftN = []
rightN = []
for line in lines:
    left, right = map(int, line.split())
    leftN.append(left)
    rightN.append(right)
leftN.sort()
rightN.sort()
d=0
for left, right in zip(leftN, rightN):
    d+=abs(left-right)
print(d)