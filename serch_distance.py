import sys
import copy

노드관계 = []
숫자보관 = []
구할노드 = []
지나갔나 = []
순서 = []
숫자개수 = 0
거리 = 0
sys.stdin = open("D:/beakjoon/beakjoon/serch_distance.txt", 'r')
첫줄 = list(map(int, sys.stdin.readline().split()))

while (1):
    임시보관 = list(map(int, sys.stdin.readline().split()))
    if max(임시보관) > 숫자개수:
        숫자개수 = max(임시보관)
    if len(임시보관) ==3:
        숫자보관.append(임시보관)
    else:
        구할노드.append(임시보관)
        break

for i in range(1,숫자개수+1):
    지나갔나.append({i : False})

for i in range(첫줄[1]-1):
    구할노드.append(list(map(int, sys.stdin.readline().split())))

순서 = copy.deepcopy(구할노드[0])
def 거리구하기(노드관계, 구할노드, 지나갔나, 순서):     #구할노드 1리스트
    지나갔나[구할노드[0]][구할노드[0]+1] = True
    for 관계 in 노드관계:
        if 구할노드[0] in 관계:
            일부관계 = copy.deepcopy(관계).remove(구할노드[0])
            순서.append(일부관계)
            if 지나갔나[일부관계[0]][[일부관계[0]+1]] == True:
                지나갔나[일부관계[0]][[일부관계[0]+1]] =False
                순서.append(일부관계)
    
    if 1:
        거리구하기(노드관계, 구할노드, 지나갔나, 순서)
    
