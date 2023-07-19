from random import randint

print("chọn kéo, búa, bao: ")

player = input()
computer = randint(0,2)

if computer == 0:
    computer = "kéo"
if computer == 1:
    computer = "bao"
if computer == 2:
    computer = "búa"

print("---") 
print("người chơi chọn: " + player )
print("máy chọn: " + computer)
print("---")

if player == computer:
    print("hòa")
else:
    if player == "kéo":
        if computer == "bao":
            print("thắng")
        else:
            print("thua")

    elif player == "búa":
        if computer == "bao":
            print("thua")
        else:
            print("thắng")
            
    elif player == "bao":
        if computer == "búa":
            print("thắng")
        else:
            print("thua")
    else:
        print("chọn không đúng yêu cầu chọn lại!!!")