T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_fly = 0
    di_1 = [1, 0, -1, 0]
    dj_1 = [0, 1, 0, -1] 

    di_2 = [-1, -1, 1, 1]
    dj_2 = [-1, 1, -1, +1]

    for i in range(N):
        for j in range(N):
            fly_1 = arr[i][j]
            fly_2 = arr[i][j]

            for k in range(4):
                for l in range(1, M):
                    ni = i + di_1[k]*l
                    nj = j + dj_1[k]*l

                    mi = i + di_2[k]*l
                    mj = j + dj_2[k]*l

                    if 0 <= ni < N and 0 <= nj < N:
                        fly_1 += arr[ni][nj]

                    if 0 <= mi < N and 0 <= mj < N:
                        fly_2 += arr[mi][mj]

                fly = fly_1
                if fly_1 < fly_2:
                    fly = fly_2 

            if max_fly < fly:
                max_fly = fly

    print(f'#{tc} {max_fly}')
