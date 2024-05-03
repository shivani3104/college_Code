def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbours in graph[node]:
            dfs(visited,graph,neighbours)
            
def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.appned(node)
    
    while queue:
        s=queue.pop[0]
        print(s,end=" ")
        
        for neighbours in graph[s]:
            if neighbours not in visited:
                visited.add(neighbours)
                queue.append(neighbours)

def main():
    visited1 = set()
    visited2 = set()
    queue=[]
    
    n=int(input("enter the number of nodes:"))
    graph=dict()
    
    for i in range(1,n+1):
        m =int(input("enter the number of edges for node" + i +" :"))
        graph[i] = list()
        for j in range(1,m+1):
            s=int(input("enter the egde" + j +"for node" + i))
            graph[i].append(s)
        
    print("the dfs is :")
    dfs(visited1,graph,1)
    print("the bfs is :")
    dfs(visited2,graph,1,queue)
    
if __name__ =="__main__":
    main()
    
            
    