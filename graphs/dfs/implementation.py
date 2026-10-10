def depthFirstTraversal(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for adjacentNodes in graph[node]:
            if adjacentNodes not in visited:
                depthFirstTraversal(visited, graph, adjacentNodes)



visited = set()

# storing the data of the graph using adjacency lists
graph = {
    '5' : ['3', '7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : [],
}

depthFirstTraversal(visited, graph, '5')