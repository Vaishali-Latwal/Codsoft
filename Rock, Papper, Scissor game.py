import random 

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type rock, paper, scissors or Q to quit:"). lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock: 0, paper: 1, scissor:2
    computer_chose = options[random_number]
    print("Computer chosed", computer_chose + ".")


    if user_input =="rock" and computer_chose =="scissors":
        print("You win!")
        user_wins +=1

    elif user_input == "paper" and computer_chose =="rock":
        print("You win!")
        user_wins += 1

    elif user_input =="scissors" and computer_chose == "paper":
            print("You win")
            user_wins += 1

    elif user_input and computer_chose == "both chose same input":
         print("its a tie")        

    else:
         print("You lose!")
         computer_wins += 1

print("You win", user_wins, "times.")
print("The computer win", computer_wins, "times")
print("Thanks for playing")                 
           
