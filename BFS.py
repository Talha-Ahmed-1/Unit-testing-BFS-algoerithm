from typing import List


def bfs(graph, node):
    queue = []  #1
    visited = []    #2
    path = []   #3
    visited.append(node)    #4
    queue.append(node)  #5
    while queue:    #6
        s = queue.pop(0)    #7 
        path.append(s)  #8
        for neighbour in graph[s]:  #9
            if neighbour not in visited:    #10
                visited.append(neighbour)   #11
                queue.append(neighbour) #12
    return path #13

# Driver Code
def runWhole():
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': [], 'H': [], 'C': []}
    print(bfs(graph, 'A'))
    print("\nGraph is: ",graph)
# runWhole()

def path1():
    print("It is not possible to achive this path.")
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': [], 'H': [], 'C': []}
    print(bfs(graph, None))
    print("\nGraph is: ",graph)
# path1()

def path2():
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': [], 'H': [], 'C': []}
    print(bfs(graph, 'C'))
    print("\nGraph is: ",graph)
# path2()

def path3():
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': [], 'H': [], 'C': []}
    print(bfs(graph, 'G'))
    print("\nGraph is: ",graph)
# path3()

def path4():
    print("It is not possible to achive this path.")
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': ['H'], 'H': [], 'C': []}
    print(bfs(graph, 'F'))
    print("\nGraph is: ",graph)
# path4()

def variableDeclaration():
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': [], 'H': [], 'C': []}
    node = 'A'

    queue = []  #1
    visited = []    #2
    path = []   #3
    visited.append(node)    #4
    queue.append(node)  #5
    print(f"var 1 = {queue}, var2 = {visited}, var3 = {path}")
    while queue:    #6
        s = queue.pop(0)    #7 
        path.append(s)  #8
        for neighbour in graph[s]:  #9
            if neighbour not in visited:    #10
                visited.append(neighbour)   #11
                queue.append(neighbour)
# variableDeclaration()

def controlStructure():
    visited = ['A']
    neighbour = 'A'
    queue = []

    if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

    print(visited, queue)
# controlStructure()

def methodParameters():
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': [], 'H': [], 'C': []}
    print("Input: Valid graph along with valid node:")
    print(bfs(graph, 'A'))
    print("Input: Invalid graph along with invalid node:")
    print(bfs({}, 2))
    print("Input: Invalid graph along with valid node:")
    print(bfs({}, 'A'))
    print("Input: Valid graph along with invalid node:")
    print(bfs(graph, 3))
# methodParameters()

def returnType():
    print("Return type should be list of nodes:")
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': [], 'H': [], 'C': []}
    if str(type(bfs(graph, 'A'))) == '<class \'list\'>':
        print("Pass")
        return
    print("Fail")
# returnType()

def nestedLoop():
    visited = []
    s = 'C'
    queue = []
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': ['H'], 'H': [], 'C': []}

    print("Skip the loop entirely")
    for neighbour in graph[s]:  #9
        if neighbour not in visited:    #10
            visited.append(neighbour)   #11
            queue.append(neighbour)
    print(visited, queue)

    s = 'F'
    print("Only one pass through the loop")
    for neighbour in graph[s]:  #9
        if neighbour not in visited:    #10
            visited.append(neighbour)   #11
            queue.append(neighbour)
    print(visited, queue)

    s = 'A'
    print("Only two pass through the loop")
    for neighbour in graph[s]:  #9
        if neighbour not in visited:    #10
            visited.append(neighbour)   #11
            queue.append(neighbour)
    print(visited, queue)

    s = 'D'
    print("m passes through the loop m < n")
    for neighbour in graph[s]:  #9
        if neighbour not in visited:    #10
            visited.append(neighbour)   #11
            queue.append(neighbour)
    print(visited, queue)
# nestedLoop()

def loopTest():
    queue = []
    visited = []
    path = []
    graph = {'A': ['B', 'D'], 'E': ['F'], 'G': ['H'], 'B': ['C', 'E'], 'D': ['E', 'H', 'G'], 'F': ['H'], 'H': [], 'C': []}

    print("Skip the loop entirely")
    while queue: 
        s = queue.pop(0) 
        path.append(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour) 
                queue.append(neighbour)
    print(visited, queue, path)

    print("Only one pass through the loop")
    queue = ['A']
    while queue: 
        s = queue.pop(0) 
        path.append(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour) 
                queue.append(neighbour)
    print(visited, queue, path)

    print("Only two pass through the loop")
    queue = ['A', 'B']
    while queue: 
        s = queue.pop(0) 
        path.append(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour) 
                queue.append(neighbour)
    print(visited, queue, path)

    print("m passes through the loop m < n")
    queue = ['A', 'B', 'D']
    while queue: 
        s = queue.pop(0) 
        path.append(s)
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour) 
                queue.append(neighbour)
    print(visited, queue, path)
loopTest()
