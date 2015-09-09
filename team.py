## team.py #####################################################################
## generic nhl94 team & franchise classes ######################################
################################################################################
from random_player import *

#Teams:
#	City
#	Name
#	Abbreviation
#	Jersey colours home/away
#	Lines
#	franchise style/strategy

class Line:
	def __init__(self, left_wing, center, right_wing, left_defense, right_defense, line_type):
		self.leftWing = left_wing
		self.Center = center
		self.rightWing = right_wing
		self.leftDefense = left_defense
		self.rightDefense = right_defense
		
		self.lineType = line_type
		
	def getLeftWinger(self):
		return self.leftWing
		
	def getCenter(self):
		return self.Center
		
	def getRightWinger(self):
		return self.rightWing
		
	def getLeftDefense(self):
		return self.leftDefense
		
	def getRightDefense(self):
		return self.rightDefense
		
	def getLineType(self):
		return self.lineType


class Goaltending:
	def __init__(self, starter, backup, third_string):
		self.startingGoaltender = starter
		self.backupGoaltender = backup
		self.thirdGoaltender = third_string
		## 3d goaltender can be a optional argument to the function whenever
		## I figure out what python null is
		
		self.currentGoaltender = self.startingGoaltender
		## and we hope it stays that way...
		
	def getCurrentGoaltender(self):
		return self.currentGoaltender

class Team:
	def __init__(self, country, city_name, team_name, abbreviation, *team_priorities):
		self.Country = country
		self.City = city_name
		self.teamName = team_name
		self.Abbreviation = abbreviation
		self.teamPriorities = []
		for priority in team_priorities:
			self.teamPriorities.insert(0, priority)
		self.Lines = []
		self.Players = []
		## and insert some lines into the array, or maybe we do it with fixed list
		## of lines instead. we'll see
	
	def getCountry(self):
		return self.Country
		
	def getCity(self):
		return self.City
		
	def getTeamName(self):
		return self.teamName
		
	def getAbbreviation(self):
		return self.Abbreviation
		
		
if(__name__ == "__main__"):
	canuckistanFirstNames = nameList("cdnFirst.txt")
	canuckistanLastNames = nameList("cdnLast.txt")	
	
	for i in range(0,30):
		newPlayer = createRandomPlayer(canuckistanFirstNames.randomName(), canuckistanLastNames.randomName())
		newPlayer.Description()
		
