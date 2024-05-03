def print_menu():
    print("main menu")
    print("1.selection sort")
    print("2.prims")
    print("3.exit")

def print_list(arr):
    for i in arr:
        print(i,end=" ")
    print()

def print_2d(arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
    print()
    
def selection_sort(list):
    for i in range(len(list)):
        t=i
        for j in range(i+1,len(list)):
            if list[t]>list[j]:
                t=j
        temp=list[i]
        list[i]=list[t]
        list[t]=temp
    return list
    
def prims():
    n=int(input("enter the number of node:"))
    mat=[[0]*n for _ in range(n)]
    m=int(input("enter the number of edge"))
    for i in range(m):
        print("enter the value of edge in start end weight format")
        start, end,weight=map(int,input().split())
        mat[start][end]=weight
        mat[end][start]=weight
    print_2d(mat)
    
    visited=[0]*n
    visited[0]=1
    tree=[]
    while len(tree)<n-1:
        min=float('inf')
        x=0
        y=0
        
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if((not visited[j]) and mat[i][j]):
                        if(min> mat[i][j]):
                            min=mat[i][j]
                            x=i
                            y=j
        tree.append((x,y,min))
        visited[y]=1
    for edge in tree:
        print(edge)
        
while True:
    print_menu()
    ch=int(input("enter your choice:"))
    if ch==1:
        n=int(input("enter the number of elements:"))
        m=list(map(int,input("enter the number ").split()))
        print("original list: ",end=" ")
        print(m)
        print("sorted list: ",end=" ")
        new1=selection_sort(m)
        print(new1)
    elif ch==2:
        prims()
    elif ch==3:
        print("thank you")
        break
    else:
        print("enter the valid option")
    
    
    
