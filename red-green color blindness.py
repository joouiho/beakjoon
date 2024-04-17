import sys
from collections import deque

def trans(index, str): 
    return str[:index] + 'n' + str[index+1:]

def detectSurround(map, location, T):      #주변 같은 색상 있는지 판별
    if location[0]+1 < T  and map[location[0]+1][location[1]] == map[location[0]][location[1]] and map[location[0]+1][location[1]] != 'n':   #확인하려는 색과 같은지 확인
        stack.append([location[0]+1, location[1]])   #위
        
    if 0 <= location[0]-1 and map[location[0]-1][location[1]] == map[location[0]][location[1]] and map[location[0]-1][location[1]] != 'n' :
        stack.append([location[0]-1, location[1]])#아래
        
    if location[1]+1 < T  and map[location[0]][location[1]+1] == map[location[0]][location[1]] and map[location[0]][location[1]+1] != 'n':
        stack.append([location[0], location[1]+1])#우

    if 0 <= location[1]-1 and map[location[0]][location[1]-1] == map[location[0]][location[1]] and map[location[0]][location[1]-1] != 'n':
        stack.append([location[0], location[1]-1])  #좌
    
    map[location[0]] = trans(location[1], map[location[0]])   #map에 바로 지나간 자리 표시

def detectSurround1(map, location, T):      #주변 같은 색상 있는지 판별
    if map[location[0]+1][location[1]] == map[location[0]][location[1]] and map[location[0]+1][location[1]] != 'n':   #확인하려는 색과 같은지 확인
        stack.append([location[0]+1, location[1]])   #위
        
    if map[location[0]-1][location[1]] == map[location[0]][location[1]] and map[location[0]-1][location[1]] != 'n' :
        stack.append([location[0]-1, location[1]])#아래
        
    if  map[location[0]][location[1]+1] == map[location[0]][location[1]] and map[location[0]][location[1]+1] != 'n':
        stack.append([location[0], location[1]+1])#우

    if map[location[0]][location[1]-1] == map[location[0]][location[1]] and map[location[0]][location[1]-1] != 'n':
        stack.append([location[0], location[1]-1])  #좌
    
    map[location[0]] = trans(location[1], map[location[0]])   #map에 바로 지나간 자리 표시

sys.stdin = open("D:/beakjoon/beakjoon/redgreen.txt",'r')
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
        if map[i][j] != 'n':
            detectSurround(map, [i,j], T)
            while stack:
                if stack:
                    t = stack[-1]
                    if 0<t[0]<T-1 and 0<t[1]<T-1 :
                        detectSurround1(map, stack.pop(), T)
                    else:
                        detectSurround(map, stack.pop(), T)
            sectorNum += 1

        if blindMap[i][j] != 'n':
            detectSurround(blindMap, [i,j], T)
            while stack:
                if stack:
                    t = stack[-1]
                    if 0<t[0]<T-1 and 0<t[1]<T-1 :
                        detectSurround1(blindMap, stack.pop(), T)
                    else:
                        detectSurround(blindMap, stack.pop(), T)
            blindSectorNum += 1

print (sectorNum, blindSectorNum)
