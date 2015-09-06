## name_generator.py ###########################################################
## randomly generate names of hockey players ###################################
## or just name everybody <first name> Sutter ##################################
## it'll be that way someday anyways ###########################################
################################################################################
import random

class playerName:
	def __init__(self, first, last):
		self.First = first
		self.Last = last
		
	def getFirstName(self):
		return self.First
		
	def getLastName(self):
		return self.Last
		
		
		
class nameList:
	def __init__(self, names_file):
		self.Names = []
		self.Names.insert(0, "Jebediah")
		self.Names.insert(0, "Bob")
		self.Names.insert(0, "Bill")
		#
		input_file = open(names_file)
		lastTell = -1
		while(lastTell != input_file.tell()):
			lastTell = input_file.tell()
			name_text = input_file.readline()
			if(name_text != ''):
				self.Names.insert(0, name_text)
			print "lastTell %d, name_text %s" % (lastTell, name_text)
		input_file.close()
		## load all of the names from the names_file text file passed as an
		## argument and place them in the list of names
	
	def randomName(self):
		listLen = len(self.Names)
		if(listLen > 0):
			nameIndex = int(random.random()*listLen)
			return self.Names[nameIndex]
		else:
			return
			## probably a type error	
	
class countryNames:
	def __init__(self, first_name_file, last_name_file):
		self.firstNames = nameList(first_name_file)
		self.lastNames = nameList(last_name_file)
		
	def getRandomFirstName(self):
		return self.firstNames.randomName()

	def getRandomLastName(self):
		return self.lastNames.randomName()
	
class nameDatabase:
	def __init__(self, canadian_first, canadian_last, american_first, american_last, \
					swedish_first, swedish_last, finnish_first, finnish_last, \
					russian_first, russian_last):
		self.canadianNames = countryNames(canadian_first, canadian_last)
		self.americanNames = countryNames(american_first, american_last)
		self.swedishNames = countryNames(swedish_first, swedish_last)
		self.finnishNames = countryNames(finnish_first, finnish_last)
		self.russianNames = countryNames(russian_first, russian_last)
		
	def generateCanadianName(self):
		return playerName(self.canadianNames.getRandomFirstName(), self.canadianNames.getRandomLastName())
	
	def generateAmericanName(self):
		return playerName(self.americanNames.getRandomFirstName(), self.americanNames.getRandomLastName())
		
	def generateSwedishName(self):
		return playerName(self.swedishNames.getRandomFirstName(), self.swedishNames.getRandomLastName())
		
	def generateFinnishName(self):
		return playerName(self.finnishNames.getRandomFirstName(), self.finnishNames.getRandomLastName())
		
	def generateRussianName(self):
		return playerName(self.russianNames.getRandomFirstName(), self.russianNames.getRandomLastName())						



if(__name__ == "__main__"):
	canuckistanNames = nameList("names.txt")
	for i in range(0, 20):
		print canuckistanNames.randomName()
	print canuckistanNames.Names






