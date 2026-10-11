from collections import deque
queue = deque()

def bfs(visited, graph, node):
    visited.add(node)
    queue.appendleft(node)
    
    while queue:
        node = queue.pop()
        print(node, end = " ")
        
        for adjancentnodes in graph[node]:
            if adjancentnodes not in visited:
                visited.add(adjancentnodes)
                queue.appendleft(adjancentnodes)





visited = set()

graph = {
    'A': ['B', 'C', 'D'],
    'B' : ['E'],
    'C' : ['E', 'F'],
    'D' : ['F'],
    'E' : ['G'],
    'F' : ['G'],
    'G' : []
}

bfs(visited, graph, 'A')