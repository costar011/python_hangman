from random import *  # 랜덤 모드 갖고오기
vocabulary = ["cheap", "guide", "length", "progress",
              "range", "package", "monster", "screen"]  # 배열에 영단어 추가
words = choice(vocabulary)  # 단어 1개 랜덤으로 돌림
write = ""  # 사용자가 입력한 영단어 저장

# 정답 맞힐 떄까지 무한으로 반복한다
while True:
    succeed = True  # 성공하는지 확인하는 변수
    print()
    for v in words:  # 제시 단어 알파벳 단위로 한 글자씩 비교
        if v in write:  # 현재 알파벳이 플레이어가 입력한 값들 중에 있으면
            print(v, end=" ")  # 영단어 표시
        else:  # 입력한 값들중에 없으면
            print("_", end=" ")  # 밑줄을 표시해라
            succeed = False  # 밑줄이 있다면 정답이 아직 안나온 것
    print()

    if succeed:  # 만약 성공했다면 게임 종료
        print("✅")
        break

    letter = input("Input Word >>>  ")  # 사용자가 한 글자씩 입력
    if letter not in write:  # 입력값 중에 포함되어 있지 않다면
        write += letter  # 새로 입력받은 글자를 입력값에 추가

    if letter in words:  # 만약 입력한 글자가 제시된 영단어에 포함되어있으면
        print("⭕️")
    else:   # 포함되지 않았으면
        print("❌")
