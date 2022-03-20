x=int(input())
for i in range(x):
    inp=int(input())
    s=set()
    cube_flag=True
    square_flag=True
    initial=1
    while(cube_flag==True) or (square_flag==True):
        cube=initial**2
        square=initial**3
        if square<=inp and square_flag:
            s.add(square)
        else:
            square_flag=False
        if cube<=inp and cube_flag:
            s.add(cube)
        else:
            cube_flag=False
        initial+=1
    print(len(s))
        