import random
options = ["Rock","Papers","Scissors"]
computer_choice = random.choice(options)
user_choice = input("choose from Rock,Papers,Scissors : ")
print("you choose:", user_choice)
print("Computer choose:", computer_choice)

if user_choice == computer_choice :
    print("it's a tie")
elif user_choice == "Papers" and computer_choice == "Rock" :
    print("Papers covers rock ! you win !")
elif user_choice == "Rock" and computer_choice == "Scissors" :
    print("Rock smashes Scissors ! you win !")
elif user_choice == "Scissors" and computer_choice == "Papers" :
    print("Scissors cuts paper ! you win !")

else :
    print("you lose !")
