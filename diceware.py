import random
import csv


class Diceware:

    """
    Diceware Implementation Experimentation
    """

    def __init__(self, csv_file):

        """
        Initialization of the class.

        :param csv_file:    Path to a diceware csv file.
        """

        self.csv_file = csv_file

        self.my_hash = random.randint(1, 1000000) * random.randint(1, 1000000) * random.randint(1, 1000000)
        random.seed(self.my_hash)

    def reseed_hash(self):

        """
        Reseeds the random number generator.
        """

        self.my_hash = random.randint(1, 1000000) * random.randint(1, 1000000) * random.randint(1, 1000000)
        random.seed(self.my_hash)

    def generate(self, passphrase_length=6):

        """
        Generates a diceware passphrase.

        :param passphrase_length:   Integer.  The number of words to include in the passphrase.

        :return: String.  The passphrase generated.
        """

        new_passphrase = ""

        for z in range(passphrase_length):
            final_code = ""

            for x in range(5):
                an_int = random.randint(1, 6)
                an_int = str(an_int)
                final_code += an_int

            with open(self.csv_file) as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    id_number = int(row["idNumber"])
                    associated_word = str(row["associatedWord"])

                    if int(final_code) == id_number:
                        new_word = associated_word

                        if z == 0:
                            new_passphrase += new_word
                        else:
                            new_passphrase = new_passphrase + " " + new_word

        return new_passphrase

    def generate_multiple(self, length_of_phrases=6, number_of_phrases=5):

        """
        Generates multiple passphrases.

        :param length_of_phrases:   The length each passphrase generated.
        :param number_of_phrases:   The number of passphrases to generate.

        :return:    List.  A list of the passphrases generated.
        """

        list_of_phrases = []

        count = 0
        while count < number_of_phrases:
            new_phrase = self.generate(passphrase_length=length_of_phrases)
            list_of_phrases.append(new_phrase)
            count += 1

        return list_of_phrases
