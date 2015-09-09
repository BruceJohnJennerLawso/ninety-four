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
			randomIntegerValue(1,4), randomIntegerValue(2,4),\ ## agility, speed
			randomIntegerValue(2,4), randomIntegerValue(2,5),\ ## offense, defense
			randomIntegerValue(2,4), randomIntegerValue(3,5),\ ## shot_power, checking
			randomBoolean(), randomIntegerValue(3,5),\		   ## right handed, fighting
			randomIntegerValue(2,4), randomIntegerValue(1,4),\ ## stick handling, shot accuracy
			randomIntegerValue(2,5), randomIntegerValue(2,5),\ ## endurance, roughness
			randomIntegerValue(2,5), randomIntegerValue(2,5),\ ## pass accuracy, aggression
			position )	
			
def createOffensiveCenter(first_name, last_name):
	position = "c"
	## this should probably be skewed a bit at some point since the actual
	## distribution of wingers is weighted away from wingers playing their off
	## wings
	newPlayer = Skater(first_name, last_name, \ 
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,5), randomIntegerValue(2,5),\ ## agility, speed
			randomIntegerValue(2,6), randomIntegerValue(1,3),\ ## offense, defense
			randomIntegerValue(2,5), randomIntegerValue(1,4),\ ## shot_power, checking
			randomBoolean(), randomIntegerValue(3,4),\		   ## right handed, fighting
			randomIntegerValue(3,5), randomIntegerValue(2,5),\ ## stick handling, shot accuracy
			randomIntegerValue(3,6), randomIntegerValue(2,4),\ ## endurance, roughness
			randomIntegerValue(3,6), randomIntegerValue(2,4),\ ## pass accuracy, aggression
			position )				

def createDefensiveCenter(first_name, last_name):
	position = "c"
	## this should probably be skewed a bit at some point since the actual
	## distribution of wingers is weighted away from wingers playing their off
	## wings
	newPlayer = Skater(first_name, last_name, \ 
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,4), randomIntegerValue(3,5),\ ## agility, speed
			randomIntegerValue(1,4), randomIntegerValue(2,5),\ ## offense, defense
			randomIntegerValue(2,4), randomIntegerValue(3,6),\ ## shot_power, checking
			randomBoolean(), randomIntegerValue(3,4),\		   ## right handed, fighting
			randomIntegerValue(2,5), randomIntegerValue(1,4),\ ## stick handling, shot accuracy
			randomIntegerValue(3,6), randomIntegerValue(2,5),\ ## endurance, roughness
			randomIntegerValue(2,5), randomIntegerValue(3,5),\ ## pass accuracy, aggression
			position )	
			
def createDefensiveDefenseman(first_name, last_name):
	if(randomBoolean() == True):
		position = "ld"
	else:
		position = "rd"
	## this should probably be skewed a bit at some point since the actual
	## distribution of wingers is weighted away from wingers playing their off
	## wings
	newPlayer = Skater(first_name, last_name, \ 
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,4), randomIntegerValue(2,4),\ ## agility, speed
			randomIntegerValue(1,3), randomIntegerValue(2,6),\ ## offense, defense
			randomIntegerValue(1,6), randomIntegerValue(3,6),\ ## shot_power, checking
			randomBoolean(), randomIntegerValue(3,6),\		   ## right handed, fighting
			randomIntegerValue(1,4), randomIntegerValue(1,3),\ ## stick handling, shot accuracy
			randomIntegerValue(3,6), randomIntegerValue(2,6),\ ## endurance, roughness
			randomIntegerValue(1,4), randomIntegerValue(3,6),\ ## pass accuracy, aggression
			position )	
			
def createOffensiveDefenseman(first_name, last_name):
	if(randomBoolean() == True):
		position = "ld"
	else:
		position = "rd"
	## this should probably be skewed a bit at some point since the actual
	## distribution of wingers is weighted away from wingers playing their off
	## wings
	newPlayer = Skater(first_name, last_name, \ 
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,6), randomIntegerValue(3,5),\ ## agility, speed
			randomIntegerValue(2,6), randomIntegerValue(1,4),\ ## offense, defense
			randomIntegerValue(3,5), randomIntegerValue(1,4),\ ## shot_power, checking
			randomBoolean(), randomIntegerValue(2,4),\		   ## right handed, fighting
			randomIntegerValue(2,5), randomIntegerValue(2,5),\ ## stick handling, shot accuracy
			randomIntegerValue(3,6), randomIntegerValue(2,5),\ ## endurance, roughness
			randomIntegerValue(3,5), randomIntegerValue(2,5),\ ## pass accuracy, aggression
			position )		
			
def createGoaltender(first_name, last_name):
	newPlayer = Goaltender(first_name, last_name, \ 
			generateRandomJerseyNumber([1, 31, 32, 33, 34, 35,36,37,38,39]), \
			randomIntegerValue(1,6), randomIntegerValue(1,4),\ ## agility, speed
			randomIntegerValue(1,4), randomIntegerValue(1,5),\ ## offense, defense
			randomIntegerValue(1,5), randomBoolean(),\ ## puck control, right handed
			randomIntegerValue(1,5), randomIntegerValue(1,5),\		   ## stick right, stick left
			randomIntegerValue(1,5), randomIntegerValue(1,5),\ ## glove right, glove left	


def createRandomPlayer(first_name, last_name):
	rand = randomIntegerValue(foo, bar)
	
	return playah
	
	
	
	
	
	
	
	
	
	
	
	
	
	
