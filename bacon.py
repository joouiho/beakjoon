import sys
import copy

def serch_bacon(node, relationship , ispassed , loop_num, bacon_num):
    for repeat in range(len(node)):
        for part_friend in relationship:
            if node[0][0] in part_friend :  #찾는값 포함 확인
                part_friend = copy.deepcopy(part_friend)  #객체복사 일어남
                index = part_friend.index(node[0][0])     
                part_friend.pop(index)         #출발값 que에서 제거
                if not(ispassed[part_friend[0]-1][part_friend[0]]):    
                    ispassed[part_friend[0]-1][part_friend[0]] = True  
                    node.append([part_friend[0], loop_num])
        bacon_num += node[0][1]
        node.pop(0)

    if not(node):
        return bacon_num
    else :
        loop_num += 1
        return serch_bacon(node ,relationship, ispassed, loop_num,bacon_num)

sys.stdin = open("D:/beakjoon/beakjoon/intext.txt", 'r')
n,m = list(map(int, input().split()))
bacon_num = 0
loop_num = 1
ispassed, relationship, total_bacon, node= [],[],[],[]

for i in range(m):
    relationship.append(list(map(int, input().split())))
for i in range(1,int(n+1)):
    ispassed.append({i : False})

for i in range (1,n+1):
    copy_ispassed = copy.deepcopy(ispassed)
    copy_ispassed[i-1][i] = True            #시작 노드 설정
    node.clear()
    node.append([i,0])
    total_bacon.append(serch_bacon(node ,copy.deepcopy(relationship), copy_ispassed,copy.deepcopy(loop_num),copy.deepcopy(bacon_num)))

print (total_bacon.index(min(total_bacon))+1)