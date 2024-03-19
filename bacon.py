import sys

sys.stdin = open("input.txt", 'r')
info = list(map(int, sys.stdin.readline().split()))

friendship = []

for i in range(info[1]):
    friendship.append(list(map(int, sys.stdin.readline().split())))

def scaning(cabin, target, lists):
    print(1)