#https://www.acmicpc.net/problem/28309
import sys
from collections import deque

sys.stdin = open(r'D:\beakjoon\beakjoon\text\cooki.txt', 'r')

T = int(sys.stdin.readline())

def serch_cokii (loc_coki, size):
    
    

for i in range(T):
    info = list(map(int, sys.stdin.readline().split()))
    loc_coki = [list(map(int, sys.stdin.readline().split())) for _ in range(info[2])]
    serch_cokii(loc_coki, info[0:2])