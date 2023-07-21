# bfs로 문제 풀기

from collections import deque # deque를 사용

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
               
                visited[i] = True

                
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
bfs(graph, 1, visited)
# 감염된 병동의 개수 출력
result = sum(visited) - 1  # A씨가 위치한 1동은 감염된 병동이므로 1을 뺌 (챗 지피티 도움)
print('감염된 병동은 총 {}개 입니다.'.format(result))




