
# 배경 준비
background = [
    [0 for cols in range(10)]
    for widths in range(10)
]

# 배경 input
for i in range(10):
    num = input().split()
    background[i] = list(map(int, num))


# 개미 집
startPoint = (1, 1)

# 현재 좌표
point = [0, 0]
point[0] = startPoint[0]
point[1] = startPoint[1]

# 현재 상태
status = 0

while status != 2:
    # print('현재 좌표 x = ', point[0], 'y=', point[1])
    # print('현재 값 = ', background[point[0]][point[1]], '\n')

    # 확인
    if background[point[0]][point[1]] == 2:
        status = 2
        background[point[0]][point[1]] = 9
    else:
        # 경로 표시
        background[point[0]][point[1]] = 9

        # 경로 이동
        if background[point[0]][point[1]+1] != 1:
            point[1] = point[1]+1
            # print(point[1])
        else:
            point[0] = point[0] + 1
            # print(point[0])

        # 유효성
        if point[0] > 8:
            point[0] = 8
            break;
        if point[1] > 8:
            point = 8
            break;


# 배경 출력 output
for i in range(10):
    for j in range(10):
        print(background[i][j], end=' ')
    print()
