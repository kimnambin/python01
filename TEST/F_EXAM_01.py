# DFS로 문제 풀기 

def dfs(graph, v, visited): # 2차원 리스트로 경로 저장
    visited[v] = 1 # 병동과 연결된 곳 (방문한 곳)은 1로 표시

    for i in graph[v]:
        if visited[i] == 0: # 그렇지 않은 곳은 0으로 표시
            dfs(graph, i, visited)

n, m = map(int, input('병동의 총 갯수와 연결된 병동의 수를 입력하세요 (공백으로 구분): ').split()) # 입력받기

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [[] for i in range(n + 1)]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [0] * (n + 1)

# 정의된 DFS 함수 호출, 시작 병동 1
for i in range(m):
    a, b = map(int, input('연결된 병동을 입력하세요 (공백으로 구분): ').split())
    graph[a].append(b)
    graph[b].append(a)  

# A씨가 위치한 1동에서 시작하여 DFS를 통해 감염된 병동의 개수 세기 (챗 지피티도움 )
dfs(graph, 1, visited)
# 감염된 병동의 개수 출력
result = sum(visited) - 1  # A씨가 위치한 1동은 감염된 병동이므로 1을 뺌 (챗 지피티 도움)
print('감염된 병동은 총 {}개 입니다.'.format(result))



