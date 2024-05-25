#https://www.acmicpc.net/problem/16724
from collections import deque
import sys
def search( lc, map, visited, pathNum):
    dict = {'U':-1, "D":1, "L":-1, "R":1}
    state = map[lc[0]][lc[1]]
    visited[lc[0]][lc[1]] = pathNum
    if state == "U" or state == "D":
        move = [lc[0]+dict[state],lc[1]]
    else :
        move = [lc[0],lc[1]+dict[state]]
    if visited[move[0]][move[1]] == 0:
        stack.append([move[0],move[1]])
    elif visited[move[0]][move[1]] == pathNum:
        return 1
    elif visited[move[0]][move[1]] != pathNum:
        return 0

# sys.stdin = open (r"D:\beakjoon\beakjoon\text\pipeman.txt",'r')

# info = list(map(int, sys.stdin.readline().split()))
info = list(map(int,input().split()))
map = [[x for x in sys.stdin.readline().strip()] for _ in range(info[0])]
visited = [[0]*info[1] for _ in range(info[0])]
stack = deque()
loopNum = 0
pathNum = 1
for i in range(info[0]):
    for j in range(info[1]):
        if visited[i][j] == 0:
            stack.append([i,j])
            while (stack):
                loop = search(stack.pop(), map, visited, pathNum)
            loopNum+=loop
            pathNum+=1
print (loopNum)
