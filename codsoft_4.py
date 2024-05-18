import random

your_name = input("Enter your Name:")

print('\n\n\t\t\tWelcome to ROCK PAPER SCISSORS Game {}\t\t\t\n\n'.format(your_name))
print("The Game choice are \n \t\t\t1 - Rock \n \t\t\t2 - Paper \n \t\t\t3 - Scissors \n")

print('\n\nThe Game Rules are :\n'
      + "\t\t\tPaper wins Rock \n"
      + "\t\t\tRock wins Scissors \n"
      + "\t\t\tScissor wins Paper \n")
print('\n\n\t\t\t Lets Start the Game {}\t\t\t\n\n'.format(your_name))

while True:
    try:
        your_choice = int(input("Enter your Choice:"))
        if your_choice > 3 or your_choice < 1:
        	print("\nplease enter valid number between 1 and 3")
        	continue
    except:
        print("\n {} Your Choice is invalid, please enter valid number".format(your_name))
        continue
    else:
	    if your_choice == 1:
	        your_choice_name = 'Rock'
	    elif your_choice == 2:
	        your_choice_name = 'Paper'
	    else:
		    your_choice_name = 'Scissors'



	    my_choice = random.randint(1,3)

	    if my_choice == 1:
	        my_choice_name = 'Rock'
	    elif my_choice == 2:
	        my_choice_name = 'Paper'
	    else:
	        my_choice_name = 'Scissors'

	    print("\nYour Choice is:{} \t\t\t\t My Choice is:{} ".format(your_choice_name.upper(),my_choice_name.upper()))   
	    

	    if your_choice == my_choice:
	        result = 'draw'
	    elif your_choice == 1 and  my_choice == 2:
	    	result = 'computer'
	    elif your_choice == 2 and  my_choice == 1:
	    	result = your_name

	    elif your_choice == 2 and  my_choice == 3:
	    	result = 'computer'
	    elif your_choice == 3 and  my_choice == 2:
	    	result = your_name

	    elif your_choice == 1 and  my_choice == 3:
	    	result = your_name
	    elif your_choice == 3 and  my_choice == 1:
	    	result = 'computer'



	    if result == your_name:
	        print("\n\n\t\t\tYou WON the GAME {}!!!!\t\t\t\n\n".format(your_name))
	    elif result == 'computer':
	    	print("\n\n\t\t\tI WON the GAME {}!!!!\t\t\t\n\n".format(your_name))
	    elif result == 'draw':
	    	print("\n\n\t\t\tThe Match is DRAW {}!!!!\t\t\t\n\n".format(your_name))

	    print("Do you want to play again? (Y/N)")
	    ans = input().lower()
	    if ans == 'y':
	        continue
	    else:
	    	break

print("\n Thanks for playing {}... See you Next Time!!!!!".format(your_name))
