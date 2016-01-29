#Catarina Soeiro
#January 28, 2016
#rps.py

#prompt user to choose
print 'Rock, Paper, Scissors?'
p1 = raw_input('Player 1? ')
p2 = raw_input('Player 2? ')

#some print variables
p1win = "Player 1 wins."
p2win = "Player 2 wins."
error = "You can't do that!"

#conditionals for options
if (p1 == p2 and (p1 == "rock" or p1 == "paper" or p1 == "scissors")):
	print 'Tie.'
#it's important to specify the p1 options
#otherwise the user can just input whatever 
#and not get an error screen
	
elif (p1== 'rock'):
	if (p2== 'scissors'):
		print p1win
	elif (p2== 'paper'):
		print p2win
	else: 
		print error
elif (p1 == 'paper'):
	if (p2 == 'rock'):
		print p1win
	elif (p2== 'scissors'):
		print p2win
	else: 
		print error
elif (p1== 'scissors'):
	if (p2 == 'rock'):
		print p2win
	elif (p2== 'paper'):
		print p1win
	else:
		print error
else: 
	print error
#every elif statement needs an else statement
#otherwise error message won't display