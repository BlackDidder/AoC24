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
n=0
for num in leftN:
    n+=num*rightN.count(num)
print(n)