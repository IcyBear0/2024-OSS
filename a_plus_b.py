# a + b

while True:
    try:
        x = int(input('첫 번째 정수를 입력하세요: '))
        y = int(input('두 번째 정수를 입력하세요: '))
        print(f'{x} + {y} = {x + y}')
        print('프로그램을 종료합니다')
        break
    except ValueError:
        print("정수가 아닙니다. 정수를 넣어주세요!")