import random

num = random.randint(1,100)
uin = int(input("Enter any number btwn 1 to 100: "))
count = 1
game_over= False
while not game_over:
  
    if uin == num:
        print(f"You win and you  guess this number in {count} times!!!!")
        game_over= True
    else:
        if uin < num:
            print("Too low...! ")
        else:
            print("Too high...! ")

        count+=1
        uin= int(input("Guess again:"))


# print(num)