n = int(input())
# 가로 세로 길이가 될 n을 입력받는다
x , y = 1, 1
# x y 출발 지점을 지정
plans = input().split()
# L R U D 중 하나의 알파벳을 입력받는다.

# L R U D 순서이다.
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이런 식으로 range안의 값이 숫자가 아닌 문자인 경우 plans 리스트의 [0]에 들어간
    # 알파벳이 plan에 대입되게 된다. 그렇기 때문에 plan은 문자형이 되는 것이다.
    # 보통의 숫자 범위인 in range가 아닌 그냥 in 뒤에 문자형 변수가 붙는다.
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # move_types는 L R U D의 문자가 들어있는 리스트이다.
    # [0, -1, 1, 0]과 같이 표현하는 것은 4개의 값을 각각 리스트 0번 인덱스부터
    # 차례대로 삽입해 주는 것과 같다. 그렇기에 move_types에도 [0]에 L [1]에 R 이 들어가는 형식이다.
    # plan과 move_types의 알파벳을 비교후 같은 알파벳을 바탕으로 다음 이동하는 좌표의 값을 만든다.
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue   
    
    # 이동할 좌표가 범위 밖인지 비교후 밖이라면 이동하지 않는다. 
    nx, ny = dx, ny

print(nx, ny)