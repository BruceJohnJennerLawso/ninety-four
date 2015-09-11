## filewrapper.py ##############################################################
## classes to interact with txt files ##########################################
## in an object oriented interface #############################################
################################################################################

class textFile:
	def __init__(self, filename):
		self.Filename = filename
		
	def write(self, *input_lines):
		fileTarget = open(self.Filename, 'r')	
		fileContents = fileTarget.read()
		fileTarget.close()
	
		fileTarget = open(self.Filename, 'w')
		fileTarget.write(fileContents)
		for i in input_lines:
			fileTarget.write(i+"\n")
		fileTarget.close()
		
	def read(self, line_number):
		fileTarget = open(self.Filename, 'r')
		
		lineNumber = 0
		lastTell = -1
		while(lastTell != fileTarget.tell()):
			lastTell = fileTarget.tell()
			line = fileTarget.readline()
			if(lineNumber == line_number):
				input_file.close()
				return line
			lineNumber += 1	
		## should throw an exception here maybe so that we can signal if
		## something went wrong
		input_file.close()


if(__name__=="__main__"):
	script, filename = argv

	fileTarget = open(filename, 'r')	
	
	fileContents = fileTarget.read()
	
	fileTarget.close()
	
	fileTarget = open(filename, 'w')
	fileTarget.write(fileContents)
	for i in range(0, 20):
		fileTarget.write((" "*i)+str(i)+"\n")
	fileTarget.close()
		
	
