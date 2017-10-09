import random
import time
import csv
import sys

def box_my_text(the_input_text):
	str(the_input_text)
	
	# calculate string length
	input_length = len(the_input_text)
	
	# build header_footer and blank_line
	header_footer = '+--' + ('-' * input_length) + '--+'
	blank_line = '|  ' + (' ' * input_length) + '  |'
	
	# print to screen
	print('')
	print(header_footer)
	print(blank_line)
	print('|  ' + the_input_text + '  |')
	print(blank_line)
	print(header_footer)
	print('')

def main():
	sys.argv
	
	numberOfWords = int(sys.argv[1])
	
	#numberOfWords = int(numberOfWords)
	
	currentTime = int(time.time())
	randomInt = random.randint(1,1000000)
	
	myHash = currentTime * randomInt
	
	random.seed(myHash)
	finalPassphrase = ""
	
	
	for z in range(numberOfWords):
		finalCode = ""
		finalCode = str(finalCode)
		
		for x in range(5):
			anInt = random.randint(1,6)
			anInt = str(anInt)
			finalCode = finalCode + anInt
	
		with open('dicewareList.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:
				newWord = ""
				idNumber = int(row["idNumber"])
				associatedWord = str(row["associatedWord"])
				
				if int(finalCode) == idNumber:
					newWord = associatedWord
					
					if z == 0:
						finalPassphrase = finalPassphrase + newWord
					else:
						finalPassphrase = finalPassphrase + " + " + newWord
	box_my_text(("Your New Passphrase:   " + finalPassphrase))

main()
