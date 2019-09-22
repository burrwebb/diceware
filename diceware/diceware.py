""" ===================================================================================================================
|
|   Name      :  diceware.py
|   Module    :  ideal_waffle
|   Copyright :  2019 Burr Webb
|   License   :  MIT  (https://opensource.org/licenses/MIT)
|
=================================================================================================================== """

import random
import csv


class Diceware:

    """
    Diceware Implementation
    """

    def __init__(self, csv_file):

        """
        Initialization of the class.

        :param csv_file:    Path to a diceware csv file.
        :type  csv_file:    str
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

        :param passphrase_length:   The number of words to include in the passphrase.
        :type  passphrase_length:   int

        :return:    The passphrase generated.
        :rtype:     str
        """

        new_passphrase = ""

        for num in range(passphrase_length):
            final_code = ""

            for code_num in range(5):
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

                        if num == 0:
                            new_passphrase += new_word
                        else:
                            new_passphrase = new_passphrase + " " + new_word

        return new_passphrase

    def generate_multiple(self, length_of_phrases=6, number_of_phrases=5):

        """
        Generates multiple passphrases.

        :param length_of_phrases:   The length each passphrase generated.
        :type  length_of_phrases:   int

        :param number_of_phrases:   The number of passphrases to generate.
        :type  number_of_phrases:   int

        :return:    A list of the passphrases generated.
        :rtype:     list
        """

        list_of_phrases = []

        count = 0
        while count < number_of_phrases:
            new_phrase = self.generate(passphrase_length=length_of_phrases)
            list_of_phrases.append(new_phrase)
            count += 1

        return list_of_phrases


"""
Copyright 2019 Burr Webb

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
