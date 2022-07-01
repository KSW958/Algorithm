# 공백으로 구분하여 입력받는다
n, m, k = map(int, input().split())
# map 함수란? : 각 요소들에 특정한 함수를 적용시킬 떄 쓰는 함수이다. 파이썬 표준에 포함 되어있는 내장함수이다.

# map을 사용하는 이유 : 1개가 아닌 여러개가 입력된 경우 각각의 요소들에 대해 특정한 함수를 적용시키고 싶을 때 위는 int를 적용시키는 것이다.
data = list(map(int, input().split()))
# 위의 문장은 list화를 하되 그 인자들을 먼저 int형으로 변환시킨 케이스이다.

data.sort()
# 이렇게 sort를 사용해 정렬을 시킬 수 있다. default 값은 오름차순이기 때문에 마지막 인덱스의 값이 가장 크다
# 나는 for문을 이중으로 겹쳐 버블정렬을 사용해 배열을 만들었다.
first  = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이 되면 반복문 탈출
            break

        result += first # 가장 큰 값 더하기

        m -= 1 # 횟수를 차감한다
    
    if m == 0:
        break

    result += second

    m -= 1
    # 이 답안은 내가 생각한 m만큼 반복하는 것이 아닌 k를 반복해서 처리하고 나머지에 second값을 더해주고 오히려 M을 차감해 0이 되었을 때 탈출하는 방식이다.

print(result)
# 마지막에 출력
# 2022.07.01


