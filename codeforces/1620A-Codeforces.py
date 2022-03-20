inp="EN"
lst=[i for i in inp]
init_E=[20,20]
init_N=[10,20]
final_lst=[]
sol=[]
def compare(x,y):
    if x==y:
        return "E"
    return "N"

def anti_value(x):
    if x==10:
        return 20
    return 10

a=[10]
b=[20]

for i in range(len(lst)):
    if lst[i]=="E":
        a.append(a[-1])
        b.append(b[-1])
    else:
        a.append(anti_value(a[-1]))
        b.append(anti_value(b[-1]))

for i in range(len(a)-1):
    if i==len(a)-1:
        sol.append(compare(a[len(a)-1],a[0]))
    else:
        sol.append(compare(a[i],a[i+1]))

for i in range(len(b)-1):
    if i==len(b)-1:
        sol.append(compare(b[len(b)-1],b[0]))
    else:
        sol.append(compare(b[i],b[i+1]))
print(a)
print(b)
print(inp)
print("".join(sol))