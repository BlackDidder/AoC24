with open("/home/simon/IdeaProjects/AoC24/Day2/input", "r") as f:
    file = f.read()
allMul = []
k=0

for i in range(1000):
    for j in range(1000):
        allMul.append("mul("+str(i)+","+str(j)+")")
