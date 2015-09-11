## league.py ###################################################################
## the thing that has the teams ################################################
## FUUUUUUUUUUUUUUU Bettman ####################################################
################################################################################
from team import *


class division:
	def __init__(self, *teams):
		self.Teams = []
		for newTeam in teams:
			self.Teams.insert(0, newTeam)

class conference:
	def __init__(self, playoff_format, *divisions):
		self.Divisions = []
		for newDivision in divisions:
			self.Divisions.insert(0, newDivision)		

class league(object):
	def __init__(self, name, region, save_file):
		self.Name = name
		self.Region = region
			
		
		self.Conferences = []
		
