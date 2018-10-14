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

	number_of_words = int(sys.argv[1])

	current_time = int(time.time())
	random_int = random.randint(1, 1000000)
	
	my_hash = current_time * random_int
	
	random.seed(my_hash)
	final_passphrase = ""

	for z in range(number_of_words):
		final_code = ""
		
		for x in range(5):
			an_int = random.randint(1, 6)
			an_int = str(an_int)
			final_code += an_int
	
		with open('dicewareList.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:
				new_word = ""
				id_number = int(row["idNumber"])
				associated_word = str(row["associatedWord"])
				
				if int(final_code) == id_number:
					new_word = associated_word
					
					if z == 0:
						final_passphrase += new_word
					else:
						final_passphrase = final_passphrase + " " + new_word

	box_my_text("Your New Passphrase:   " final_passphrase)


##########################
#
#  Execute main()
#
##########################
main()
