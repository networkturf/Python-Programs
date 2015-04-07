def name_to_number(name):
    if name == 'rock': 
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print 'Try again'
        quit()
#print name_to_number('rock')



def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return "This is not a valid choice"
#print number_to_name(4)


def rpsls(player_choice): 
    
    player_choice = raw_input("Enter your choice: ")
    print "Player chooses %s"  %player_choice
    return name_to_number(player_choice)
    

player_number = rpsls("player_choice")
#print "Player's number is: %s" %player_number


import random
comp_number = random.randrange(0,5)
#print "Computer's number is: %s" %comp_number
def rpsls():
    
    return number_to_name(comp_number)
    
    
print "Computer chooses %s" %rpsls()

final = (comp_number - player_number)%5
def rpsls():
    if final >= 3:
        return "Player wins!"
    elif final >= 1:
        return "Computer wins!"
    else:
        return "Its a tie"
print rpsls()



