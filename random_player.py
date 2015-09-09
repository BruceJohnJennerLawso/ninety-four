## random_player.py ############################################################
## random player generation to fill in the gaps in rosters #####################
################################################################################
from player import *


#Skaters:
#	Jersey Number
#	Overall rating
#	Weight value (not understood, 0-9 ABC upwards is higher weights?)
#	Agility 1,2,3,4,5,6 (Gretzky 6)
#	Speed 1,2,3,4,5,6 (Bure 6)
#	Offense Awareness (Gretzky 5)
#	Defense Awareness (Bourque 6)
#	Shot Power (Bourque 5)
#	Checking (Bourque 6)
#	Handed/Fighting (Dont understand, maybe dual handedness and fighting ability?)
#	Stick Handling (Gretzky 6)
#	Shot Accuracy (Gretzky 2? similar scale to others)
#	Endurance (Gretzky 6)
#	Roughness (Gretzky 0)
#	Pass Accuracy (Gretzky 0)
#	Aggression (Stevens 3, Probert, Kypreos 5)	
#	def __init__(self, first_name, last_name, jersey_number,\
#				agility, speed, offense, defense, shot_power, checking,\
#				right_handed, fighting, stick_handling, shot_accuracy, endurance,\
#				roughness, pass_accuracy, aggression, position, overall_rating=-1):
#		super(Skater, self).__init__(first_name, last_name, jersey_number)

def createScoringWinger(first_name, last_name):
	if(randomBoolean() == True):
		position = "lw"
	else:
		position = "rw"
	newPlayer = Skater(first_name, last_name, \
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(3,5), randomIntegerValue(3,4),\
			randomIntegerValue(3,5), randomIntegerValue(2,4),\
			randomIntegerValue(3,6), randomIntegerValue(2,4),\
			randomBoolean(), randomIntegerValue(1,4),\
			randomIntegerValue(2,5), randomIntegerValue(3,6),\
			randomIntegerValue(2,4), randomIntegerValue(2,4),\
			randomIntegerValue(3,4), randomIntegerValue(2,4),\
			position )
	return newPlayer		

def createCheckingWinger(first_name, last_name):
	if(randomBoolean() == True):
		position = "lw"
	else:
		position = "rw"
	## this should probably be skewed a bit at some point since the actual
	## distribution of wingers is weighted away from wingers playing their off
	## wings
	newPlayer = Skater(first_name, last_name, \
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,4), randomIntegerValue(2,4),\
			randomIntegerValue(2,4), randomIntegerValue(2,5),\
			randomIntegerValue(2,4), randomIntegerValue(3,5),\
			randomBoolean(), randomIntegerValue(3,5),\
			randomIntegerValue(2,4), randomIntegerValue(1,4),\
			randomIntegerValue(2,5), randomIntegerValue(2,5),\
			randomIntegerValue(2,5), randomIntegerValue(2,5),\
			position )	
	return newPlayer
			
def createOffensiveCenter(first_name, last_name):
	position = "c"
	newPlayer = Skater(first_name, last_name, \
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,5), randomIntegerValue(2,5),\
			randomIntegerValue(2,6), randomIntegerValue(1,3),\
			randomIntegerValue(2,5), randomIntegerValue(1,4),\
			randomBoolean(), randomIntegerValue(3,4),\
			randomIntegerValue(3,5), randomIntegerValue(2,5),\
			randomIntegerValue(3,6), randomIntegerValue(2,4),\
			randomIntegerValue(3,6), randomIntegerValue(2,4),\
			position )				
	return newPlayer

def createDefensiveCenter(first_name, last_name):
	position = "c"
	newPlayer = Skater(first_name, last_name, \
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,4), randomIntegerValue(3,5),\
			randomIntegerValue(1,4), randomIntegerValue(2,5),\
			randomIntegerValue(2,4), randomIntegerValue(3,6),\
			randomBoolean(), randomIntegerValue(3,4),\
			randomIntegerValue(2,5), randomIntegerValue(1,4),\
			randomIntegerValue(3,6), randomIntegerValue(2,5),\
			randomIntegerValue(2,5), randomIntegerValue(3,5),\
			position )	
	return newPlayer
			
def createDefensiveDefenseman(first_name, last_name):
	if(randomBoolean() == True):
		position = "ld"
	else:
		position = "rd"
	newPlayer = Skater(first_name, last_name, \
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,4), randomIntegerValue(2,4),\
			randomIntegerValue(1,3), randomIntegerValue(2,6),\
			randomIntegerValue(1,6), randomIntegerValue(3,6),\
			randomBoolean(), randomIntegerValue(3,6),\
			randomIntegerValue(1,4), randomIntegerValue(1,3),\
			randomIntegerValue(3,6), randomIntegerValue(2,6),\
			randomIntegerValue(1,4), randomIntegerValue(3,6),\
			position )	
	return newPlayer
			
def createOffensiveDefenseman(first_name, last_name):
	if(randomBoolean() == True):
		position = "ld"
	else:
		position = "rd"
	newPlayer = Skater(first_name, last_name, \
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,6), randomIntegerValue(3,5),\
			randomIntegerValue(2,6), randomIntegerValue(1,4),\
			randomIntegerValue(3,5), randomIntegerValue(1,4),\
			randomBoolean(), randomIntegerValue(2,4),\
			randomIntegerValue(2,5), randomIntegerValue(2,5),\
			randomIntegerValue(3,6), randomIntegerValue(2,5),\
			randomIntegerValue(3,5), randomIntegerValue(2,5),\
			position )		
	return newPlayer
	
## agility, speed	
## offense, defense		
## shot_power, checking	
## right handed, fighting
## stick handling, shot accuracy
## endurance, roughness
## pass accuracy, aggression


def createGoaltender(first_name, last_name):
	newPlayer = Goaltender(first_name, last_name, \
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,6), randomIntegerValue(1,4),\
			randomIntegerValue(1,4), randomIntegerValue(1,5),\
			randomIntegerValue(1,5), randomBoolean(),\
			randomIntegerValue(1,5), randomIntegerValue(1,5),\
			randomIntegerValue(1,5), randomIntegerValue(1,5))
	return newPlayer


## agility, speed
## offense, defense
## puck control, right handed
## stick right, stick left
## glove right, glove left	


def createRandomPlayer(first_name, last_name):
	rand = randomIntegerValue(1, 7)
	if(rand == 1):
		newPlayer = createScoringWinger(first_name, last_name)
	elif(rand == 2):
		newPlayer = createCheckingWinger(first_name, last_name)
	elif(rand == 3):
		newPlayer = createDefensiveCenter(first_name, last_name)
	elif(rand == 4):
		newPlayer = createOffensiveCenter(first_name, last_name)
	elif(rand == 5):
		newPlayer = createDefensiveDefenseman(first_name, last_name)
	elif(rand == 6):
		newPlayer = createOffensiveDefenseman(first_name, last_name)
	elif(rand == 7):
		newPlayer = createGoaltender(first_name, last_name)
	return newPlayer
	
	
	
	
	
	
	
	
	
	
	
	
	
	
