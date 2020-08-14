# 익은 토마토의 영향을 받는다. (인접의 덜익은 토마토가 익는다, 대각선은 영향 x)

M,N = map(int,input().split())
#M : 가로칸 N :세로칸

box = [[0 for _ in range(M)] for _ in range(N)]
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


while (True):
    arr.find