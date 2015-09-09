## player.py ###################################################################
## generic player class based off of nhl 94 stats to interface with nhl 94  ####
## bin files ###################################################################
################################################################################
from name_generator import *

def generateRandomJerseyNumber(bad_numbers, depth=0):
	""" Generate some random jersey number between 0 and 99 with the exception
	of any numbers in a list called bad_numbers, so we can avoid skaters with
	number 1 or 31 or whatever""" 
	new_number = -1
	while(True):
		new_number = int(random.random()*99)+1
		for number in bad_numbers:
			if(new_number == number):
				##print "%d is a bad number" % new_number
				return generateRandomJerseyNumber(bad_numbers, depth+1)
				## this is horrifying
				## what is wrong with me
		##if(depth > 5):
		##	print (">"*depth), new_number
		return new_number

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


class Player:
	def __init__(self, first_name, last_name, jersey_number):
		self.firstName = first_name
		self.lastName = last_name
		self.jerseyNumber = jersey_number

	def generateOverallRating(self):
		##overallRating = fooooo
		##return overallRating
		return -1
		
	def getFullName(self):
		fullName = self.firstName + self.lastName
		return fullName
		
	def getFirstName(self):
		return self.firstName
		
	def getLastName(self):
		return self.lastName
		
	def getJerseyNumber(self):
		return self.jerseyNumber

class Skater(Player):
	def __init__(self, first_name, last_name, jersey_number,\
				agility, speed, offense, defense, shot_power, checking,\
				right_handed, fighting, stick_handling, shot_accuracy, endurance,\
				roughness, pass_accuracy, aggression, position, overall_rating=-1):
		super(Skater, self).__init__(first_name, last_name, jersey_number)
		self.Agility = agility
		self.Speed = speed
		self.Offense = offense
		self.Defense = defense
		self.shotPower = shot_power
		self.Checking = checking
		self.isRightHanded = right_handed
		## we get snarky and avoid defining custom types by using a bool
		self.Fighting = fighting
		self.stickHandling = stick_handling
		self.shotAccuracy = shot_accuracy
		self.Endurance = endurance
		self.Roughness = roughness
		self.passAccuracy = pass_accuracy
		self.Aggression = aggression
		self.Position = position
		if(overall_rating == -1):
			## we didnt get a rating, so we are going to calculate a new one
			## based on the rest of the stats
			self.overallRating = self.generateOverallRating()
		else:
			self.overallRating = overall_rating
			## otherwise we manually set the player rating to whatever we were
			## passed in the constructor
			
	def generateOverallRating(self):
		Rating = (((7/6)*self.Agility)+((7/6)*self.Speed)+((7/6)*self.Offense) )
		Rating += ( ((7/6)*self.Defense)+((7/6)*self.Checking)+((7/6)*self.stickHandling) ) 
		Rating += ( ((7/6)*self.shotAccuracy)+((7/6)*self.Endurance)+((2/6)*self.Roughness) )		
		Rating += ( ((3/6)*self.Aggression)+((7/6)*self.Agility)+((7/6)*self.passAccuracy) )
		return Rating
		
	def getAgility(self):
		return self.Agility
		
	def getSpeed(self):
		return self.Speed
	
	def getOffense(self):
		return self.Offense
		
	def getDefense(self):
		return self.Defense
		
	def getShotPower(self):
		return self.shotPower
		
	def getChecking(self):
		return self.Checking
		
	def getIsRightHanded(self):
		return self.isRightHanded
		
	def getFighting(self):
		return self.Fighting
		
	def getStickHandling(self):
		return self.stickHandling
		
	def getShotAccuracy(self):
		return self.shotAccuracy
		
	def getEndurance(self):
		return self.Endurance
		
	def getRoughness(self):
		return self.Roughness
		
	def getPassAccuracy(self):
		return self.passAccuracy
		
	def getAggression(self):
		return self.Aggression
		
	def getOveralRating(self):
		return self.overallRating

	def getPosition(self):
		return self.Position
		# convention here is based off of the functions defined below
		
def caseInsensitiveMatch(str1, str2):
	if(str1.lower() == str2.lower()):
		return True;
	else:
		return False;		
		
def isLeftWing(i):
	if(caseInsensitiveMatch(i, "lw")):
		return True
	else:
		return False

def isRightWing(i):
	if(caseInsensitiveMatch(i, "rw")):
		return True
	else:
		return False		

def isCenter(i):
	if(caseInsensitiveMatch(i, "c")):
		return True
	else:
		return False			
	
def isRightDefense(i):
	if(caseInsensitiveMatch(i, "rd")):
		return True
	else:
		return False			
		
def isLeftDefense(i):
	if(caseInsensitiveMatch(i, "ld")):
		return True
	else:
		return False							

def randomValue(floor, ceiling):
	value = floor + (random.random()*(ceiling - floor))
	return value
	
def randomIntegerValue(floor, ceiling):
	return int(randomValue(floor, ceiling+1))	

def randomBoolean():
	value = int(random.random()*2)
	if(val == 1):
		return True
	else:
		return False

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
			randomIntegerValue(1,4), randomIntegerValue(3,4),\ ## agility, speed
			randomIntegerValue(3,5), randomIntegerValue(2,4),\ ## offense, defense
			randomIntegerValue(3,6), randomIntegerValue(2,4),\ ## shot_power, checking
			randomBoolean(), randomIntegerValue(1,4),\		   ## right handed, fighting
			randomIntegerValue(2,5), randomIntegerValue(3,6),\ ## stick handling, shot accuracy
			randomIntegerValue(2,4), randomIntegerValue(2,4),\ ## endurance, roughness
			randomIntegerValue(3,4), randomIntegerValue(2,4),\ ## pass accuracy, aggression
			position )	

#Goaltenders:
#	Jersey Number
#	Overall rating
#	Weight (see above)
#	Agility (see above)
#	Speed (see above)
#	Offense Awareness (see above)
#	Defensive Awareness (see above)
#	Puck Control (Roy 6)
#	Glove Hand (Roy 0?, commonly 0 or 1)
#	Stick right (Roy 5)
#	Stick left (Roy 5, commonly the same on both sides
#	Glove Right (Roy 3)
#	Glove Left (Roy 3, commonly same both sides)

class Goaltender(Player):
	def __init__(self, first_name, last_name, jersey_number, \
				agility, speed, offense, defense, puck_control,	is_right_handed, \
				 stick_right, stick_left, glove_right, glove_left, overall_rating=-1):
		super(Goaltender, self).__init__(first_name, last_name, jersey_number)
		self.Agility = agility
		self.Speed = speed
		self.Offense = offense
		self.Defense = defense
		self.puckControl = puck_control
		self.isRightHanded = is_right_handed
		self.stickRight = stick_right
		self.stickLeft = stick_left
		self.gloveRight = glove_right
		self.gloveLeft = glove_left
		
		if(overall_rating == -1):
			## we didnt get a rating, so we are going to calculate a new one
			## based on the rest of the stats
			self.overallRating = self.generateOverallRating()
		else:
			self.overallRating = overall_rating
			## otherwise we manually set the player rating to whatever we were
			## passed in the constructor

	def generateOverallRating(self):
		Rating = (((12/6)*self.Agility)+((12/6)*self.Speed)+((10/6)*self.Offense) )
		Rating += ( ((10/6)*self.Defense)+((12/6)*self.puckControl)+((11/6)*self.stickRight) ) 
		Rating += ( ((11/6)*self.stickLeft)+((12/6)*self.gloveLeft)+((12/6)*self.gloveRight) )		
		return Rating
		
	def getAgility(self):
		return self.Agility
		
	def getSpeed(self):
		return self.Speed
	
	def getOffense(self):
		return self.Offense
		
	def getDefense(self):
		return self.Defense
		
	def getIsRightHanded(self):
		return self.isRightHanded
		
	def getPuckControl(self):
		return self.puckControl
		
	def getStickRight(self):
		return self.stickRight
		
	def getStickLeft(self):
		return self.stickLeft
	
	def getGloveRight(self):	
		return self.gloveRight
		
	def getGloveRight(self):
		return self.gloveLeft	
		
	def getOveralRating(self):
		return self.overallRating
		
if(__name__=="__main__"):
	for i in range(0, 200):
		print generateRandomJerseyNumber([1, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]),
		## some people have this stupid thing about 'goalie numbers' and 
		## 'skater numbers'
	for i in range(0, 200):
		print randomIntegerValue(1,6)
