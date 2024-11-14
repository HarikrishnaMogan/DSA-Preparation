https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1

# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        # code here
        
        #checking neighour node also have same color or not
        def isSafe(node,colors,adj,colorToCheck):
            for neighbour in adj[node]:
                if colors[neighbour] == colorToCheck:
                    return False
            return True
        
        
        def iscolorPossible(node,colors,adj,m,v):
            if node == v:
                return True
            
            for i in range(1,m+1):
                if isSafe(node,colors,adj,i):
                    colors[node]=i
                    if iscolorPossible(node+1,colors,adj,m,v)==True:
                        return True
                    colors[node] = 0
            return False
                    
        
    
        #creating adjacent node, this will provide neigbours or adjacent list of a vertices
        adj = [[] for i in range(v)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        colors = [0]*v
        
        return iscolorPossible(0,colors,adj,m,v)
