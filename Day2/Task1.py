with open("/home/user/IdeaProjects/AoC24/Day2/input", "r") as f:
    file=f.read()
lines=file.splitlines()
i=0
for line in lines:
    temp=list(map(int,line.split()))
    if (all(temp[k] <= temp[k+1] for k in range(len(temp) - 1))) or (all(temp[l] >= temp[l+1] for l in range(len(temp) - 1))):
        mi=5
        ma=0
        for j in range(len(temp)-1):
            akt=abs(temp[j] - temp[j+1])
            mi=min(mi,akt)
            ma=max(ma,akt)
        if mi>=1 and ma<=3: i+=1
print(i)