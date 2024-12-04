with open("input", "r") as f:
    file = f.read()
lines = file.splitlines()
i = 0
for line in lines:
    temp = list(map(int, line.split()))
    for h in range(len(temp)):
        a = False
        b = False
        templist = temp[:h] + temp[h + 1:]
        if (all(templist[k] <= templist[k + 1] for k in range(len(templist) - 1))) or (
        all(templist[l] >= templist[l + 1] for l in range(len(templist) - 1))): a = True
        mi = abs(templist[0] - templist[1])
        ma = mi
        for j in range(0, len(templist) - 1):
            akt = abs(templist[j] - templist[j + 1])
            mi = min(mi, akt)
            ma = max(ma, akt)
        if mi >= 1 and ma <= 3 and a:
            i += 1
            break
print(i)