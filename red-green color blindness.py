import sys
import copy
from collections import deque

def detectSurround(map, visited, lc, T):      #주변 같은 색상 있는지 판별
    visited[lc[0]][lc[1]] = 1   #시작자리
    try:  
        if map[lc[0]+1][lc[1]] == map[lc[0]][lc[1]] and visited[lc[0]+1][lc[1]] == 0:    #확인하려는 색과 같은지 확인
            stack.append([lc[0]+1, lc[1]])
            visited[lc[0]+1][lc[1]] = 1   #위
    except:
        a = 1
    
    try:  
        if  map[lc[0]-1][lc[1]] == map[lc[0]][lc[1]] and visited[lc[0]-1][lc[1]] == 0 :
            stack.append([lc[0]-1, lc[1]])
            visited[lc[0]-1][lc[1]] = 1   #아래
    except:
        a =1

    try  :
        if map[lc[0]][lc[1]+1] == map[lc[0]][lc[1]] and visited[lc[0]][lc[1]+1] == 0 :
            stack.append([lc[0], lc[1]+1])
            visited[lc[0]][lc[1]+1]   #우
    except:
        a =1

    try :
        if map[lc[0]][lc[1]-1] == map[lc[0]][lc[1]] and visited[lc[0]][lc[1]-1] == 0 :
            stack.append([lc[0], lc[1]-1])  #좌
            visited[lc[0]][lc[1]-1] = 1
    except:
        a =1
sys.stdin = open('D:/beakjoon/beakjoon/text/redgreen.txt', 'r')
T = int(sys.stdin.readline())
map = []
sectorNum = 0
blindSectorNum = 0
stack = deque()
blindMap = copy.deepcopy(map)
visited = [[0 for i in range(T)] for i in range(T)]
cvisited = copy.deepcopy(visited)
for i in range(T):
    temp = sys.stdin.readline().replace("\n","")
    map.append(temp)
    blindMap.append(temp.replace("R", "G"))


for i in range(T):
    for j in range(T):
        print (map[i-1][j])
        if visited[i][j] == 0:
            detectSurround(map, visited, [i,j], T)
            while stack:
                detectSurround(map, visited, stack.pop(), T)
            sectorNum += 1

for i in range(T):
    for j in range(T):
        if cvisited[i][j] == 0:
            detectSurround(blindMap, cvisited, [i,j], T)
            while stack:
                detectSurround(blindMap, cvisited, stack.pop(), T)
            blindSectorNum += 1

print (sectorNum, blindSectorNum)