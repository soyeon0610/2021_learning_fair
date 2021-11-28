front="""
           *****
        **       **.
       **         **
       *   front   *
       **         **
        **       **
           *****
"""
back="""
           *****
        **       **.
       **         **
       *   back    *
       **         **
        **       **
           *****
"""


import random
print("*"*35)
print("동전 던지기 게임을 시작합니다.")
print("*"*35)
print()

keep_playing="yes"

while keep_playing=="yes":
    computer=random.randint(0,1)
    choice=int(input("앞면일까요? 뒷면일까요? (0:앞면, 1: 뒷면) >>> "))

    print("동전 결과:")
    if computer ==0:
        print(front)
    else:
        print(back)

    print("나의 선택: ")
    if choice==0:
        print(front)

    else:
        print(back)

    print("게임 결과 : ")
    if computer == choice:
        print("성공")
    else:
        print("실패")


    keep_playing=input("동전던지기 게임을 계속 하시겠습니까? 31게임으로 넘어가시겠습니까? \n(yes:동전던지기 / 그 외:31게임) >>> ").lower()
    print("=" *35)

print("       동전던지기 게임 종료")
print("="*35)
print("\n")


import random
import operator

game_point = {"Player":0, "computer1":0, "computer2":0}

while True:
    print("*"*20)
    print("    31 숫자게임")
    print("*"*20)

    game_log = []

    current_number =1

    randnum = random.randint(0, 2)
    if randnum == 0:
        current_player = "Player"
    elif randnum == 1:
        current_player = "computer1"
    else:
        current_player = "computer2"

    while current_number <= 31:
        print("현재 숫자는 " + str(current_number) + " 입니다.")

        if current_player == "Player":
            print("1, 2, 또는 3을 입력하세요. 더해서 31 이상이 되면 게임에서 지는 것입니다.")

            player_choice = ""
            while player_choice not in ["1", "2", "3"]:
                player_choice = input("어떤 값을 더할까요?")

            player_choice = int(player_choice)
            current_number = current_number + player_choice

            if current_number >=31:
                print("\n현재 숫자는 "+str(current_number) + " 입니다.")
                print()
                print("Player가 졌습니다.")
                break
            
            game_log.append("Player")
            current_player = "computer1"

        elif current_player == "computer1":
            computer_choice = random.randint(1,3)
            current_number = current_number +computer_choice
            print("computer1 순서입니다. computer1는 "+ str(computer_choice) + " 을 선택했습니다.")
                     
            if current_number >= 31:
                print("현재 숫자는 "+str(current_number) + " 입니다.")
                print()
                print("computer1이 졌습니다.")
                break

            game_log.append("computer1")
            current_player = "computer2"

        else:
            computer_choice = random.randint(1,3)
            current_number = current_number + computer_choice
            print("computer2 순서입니다. computer2는 "+ str(computer_choice) + " 을 선택했습니다.")

            if current_number >= 31:
                print("현재 숫자는 "+str(current_number) + " 입니다.")
                print()
                print("computer2이 졌습니다.")
                break

            game_log.append("computer2")
            current_player = "Player"


    player = game_log.pop()
    game_point[player] = game_point[player] + 2

    player = game_log.pop()
    game_point[player] = game_point[player] + 1

    print("점수")
    print(game_point)            

    play_again = input("게임을 다시 진행하겠습니까? (계속진행 = yes) >>> ")
    if play_again.lower().startswith("yes"):
        continue
    else:
        print("31게임 종료")
        break

print("")
print("[31게임 점수 순위]")
sort_list = sorted(game_point.items(), key=operator.itemgetter(1), reverse=True)
for i in range(len(sort_list)):
    print("{}위 : {}".format(i+1, sort_list[i][0]))

            
