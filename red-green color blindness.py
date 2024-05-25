import sys
import copy
from collections import deque

def detectSurround(map, visited, location, T):      #주변 같은 색상 있는지 판별
    visited[location[0]][location[1]] = 1   #시작자리
    if  0 <= location[0]+1 < T and visited[location[0]+1][location[1]] == 0 and map[location[0]+1][location[1]] == map[location[0]][location[1]] :   #확인하려는 색과 같은지 확인
        stack.append([location[0]+1, location[1]])
        visited[location[0]+1][location[1]] = 1   #위
        
    if  0 <= location[0]-1 < T and visited[location[0]-1][location[1]] == 0 and map[location[0]-1][location[1]] == map[location[0]][location[1]] :
        stack.append([location[0]-1, location[1]])
        visited[location[0]-1][location[1]] = 1   #아래

    if  0 <= location[1]+1 < T and visited[location[0]][location[1]+1] == 0 and map[location[0]][location[1]+1] == map[location[0]][location[1]] :
        stack.append([location[0], location[1]+1])
        visited[location[0]][location[1]+1]   #우
        
    if 0 <= location[1]-1 < T and visited[location[0]][location[1]-1] == 0 and map[location[0]][location[1]-1] == map[location[0]][location[1]] :
        stack.append([location[0], location[1]-1])  #좌
        visited[location[0]][location[1]-1] = 1

sys.stdin = open (r"D:\beakjoon\beakjoon\text\redgreen.txt", 'r')
T = int(sys.stdin.readline())
map = []
sectorNum = 0
blindSectorNum = 0
stack = deque()
blindMap = copy.deepcopy(map)
visited = [[0 for i in range(T)] for i in range(T)]

for i in range(T):
    temp = sys.stdin.readline().replace("\n","")
    map.append(temp)
    blindMap.append(temp.replace("R", "G"))

for i in range(T):
    for j in range(T):
        if visited[i][j] == 0:
            detectSurround(map, visited, [i,j], T)
            while stack:
                detectSurround(map, visited, stack.pop(), T)
            sectorNum += 1
visited = [[0 for i in range(T)] for i in range(T)]

for i in range(T):
    for j in range(T):
        if visited[i][j] == 0:
            detectSurround(blindMap, visited, [i,j], T)
            while stack:
                detectSurround(blindMap, visited, stack.pop(), T)
            blindSectorNum += 1

print (sectorNum, blindSectorNum)