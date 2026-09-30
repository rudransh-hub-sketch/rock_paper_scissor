import random
choices = ["rock","paper","scissor"]
real_player_score = 0
computer_score = 0
print("===welcome to rock, paper, scissor===")

# player can play again and again with computer using while loop
while True:
    real_player_choice = input("\nEnter rock, paper, or scissor(or 'exit' to stop): ").lower().strip()
    
    #if player wants to quit the game he/she write exit
    if real_player_choice == "exit":
        print("Thanks for playing!")
        print("your score:" , real_player_score)
        print("computer score:" , computer_score)
        break
    
    #if player write wrong input
    if real_player_choice not in choices:
        print("invalid choice! please select rock, paper, or scissor.")
        continue
    
    #by using random, computer show rock, paper, scissor randomly means i will also get chance to win
    computer_choice = random.choice(choices)
    print(f"computer chose: {computer_choice}")
    
    if real_player_choice == computer_choice:
        print("result: it's a tie!")

    #or is used because there can be three conditions and i want to write in same elif    
    elif (real_player_choice == "rock" and computer_choice == "scissor") or \
         (real_player_choice == "paper" and computer_choice == "rock") or \
         (real_player_choice == "scissor" and computer_choice == "paper"):
         print("result: you win!")
         
         #player score will increase by one point everytime
         real_player_score += 1
             
    else:
        print("result: you lose!")
        
        #computer score will increase
        computer_score += 1
        
    #it will show real_player score and computer_score    
    print("your score:" , real_player_score)
    print("computer score:" , computer_score)
