"""
BFS는 너비 우선 탐색.
가장 먼저 방문한 지점을 확인할 visit 리스트와, 앞으로 방문 할 지점들을 저장할 queue 리스트를 만든다.
"""
def bfs(graph, start_node):
  visit = []
  queue = []
  
  queue.append(start_node)
  
  while queue:
    node = queue.pop(0) # Queue의 첫 번째 항목을 node로 가져오는 것
    print(visit, queue) # BFS의 동작 과정을 보기 위해 visit과 queue를 print 해본다.
    if node not in visit: # Node가 visit에 없으면, 즉 방문한 적이 없는 지점이면 visit에 추가하고 해당 노드의 인접 노드들을 queue에 추가한다.
      visit.append(node)
      queue.extend(graph[node])
  return visit

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

bfs(graph, 'A')
