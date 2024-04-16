import sys
from collections import deque

def detectSurround(map, location, T):      #주변 같은 색상 있는지 판별
    map[location[0]][location[1]] = 0   #map에 바로 지나간 자리 표시
    if map[location[0]+1][location[1]] == map[location[0]][location[1]] and 0 <= location[0]+1 < T and map[location[0]+1][location[1]] == 0 :   #확인하려는 색과 같은지 확인
        stack.append([location[0]+1, location[1]])
        map[location[0]+1][location[1]] = 0   #위
        
    if  map[location[0]-1][location[1]] == map[location[0]][location[1]] and 0 <= location[0]-1 < T and map[location[0]-1][location[1]] == 0 :
        stack.append([location[0]-1, location[1]])
        map[location[0]-1][location[1]] = 0   #아래

    if map[location[0]][location[1]+1] == map[location[0]][location[1]] and 0 <= location[1]+1 < T and map[location[0]][location[1]+1] == 0  :
        stack.append([location[0], location[1]+1])
        map[location[0]][location[1]+1] = 0   #우
        
    if map[location[0]][location[1]-1] == map[location[0]][location[1]] and 0 <= location[1]-1 < T and map[location[0]][location[1]-1] == 0  :
        stack.append([location[0], location[1]-1])  #좌
        map[location[0]][location[1]-1] = 0

T = int(sys.stdin.readline())
map = []
blindMap = []
sectorNum = 0
blindSectorNum = 0
stack = deque()

for i in range(T):
    temp = sys.stdin.readline().replace("\n","")
    map.append(temp)
    blindMap.append(temp.replace("R", "G"))

for i in range(T):
    for j in range(T):
        if map[i][j] == 0:
            detectSurround(map, [i,j], T)
            while stack:
                detectSurround(map, stack.pop(), T)
            sectorNum += 1
map = [[0 for i in range(T)] for i in range(T)]

for i in range(T):
    for j in range(T):
        if map[i][j] == 0:
            detectSurround(blindMap, map, [i,j], T)
            while stack:
                detectSurround(blindMap, map, stack.pop(), T)
            blindSectorNum += 1

print (sectorNum, blindSectorNum)
