# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y): # 가로, 세로
    # 얼음틀에서 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0: # 처음엔 0, 0
        # 해당 노드 방문 처리, 얼음 표시
        graph[x][y] = 1 # 방문 이후 1, 1
        # 상, 좌, 하, 우의 위치 재귀 호출(모든 방향 탐색)
        dfs(x - 1, y) 
        dfs(x, y - 1) 
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True # 방문 끝나면 참 리턴
    return False # 재귀 탈출 조건

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력