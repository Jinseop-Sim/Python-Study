graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def dfs(graph, start_node):
    visit = []
    stack = []

    stack.append(start_node)

    while stack:
        print(visit, stack)
        node = stack.pop() # 앞서 본 BFS는 pop(0)을 이용해 제일 앞 원소를 꺼내와서 queue처럼 이용했지만, pop()을 하여 제일 마지막 원소를 빼내 Stack처럼 만든다.
        if node not in visit: 
            visit.append(node)
            stack.extend(graph[node])
    return visit

dfs(graph, 'A')

"""
BFS는 너비 우선 탐색이라 Queue처럼 동작해야하며, DFS는 깊이 우선 탐색이라 Stack처럼 동작해야만 한다.
"""
