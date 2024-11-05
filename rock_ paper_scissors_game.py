import random

choice_to_emoji = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'    
}
my_choices = ('r','p','s')

while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in my_choices:
        print("Invalid Choice!")
        continue
        
    computer_choice = random.choice(my_choices)

    print(f'You chose {choice_to_emoji[user_choice]}')
    print(f'Computer chose {choice_to_emoji[computer_choice]}')
    if user_choice == computer_choice:
        print("Tie")
        
    elif ((user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or (user_choice == "p" and computer_choice == "r")):
        print("You win")
    else:
        print("you lose")

    user_continue = input("Do you want to continue (y/n):").lower()
    if user_continue == "n":
        break
    

   
       
            
  
