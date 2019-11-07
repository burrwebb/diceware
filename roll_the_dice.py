#!/usr/bin/python3
""" ===================================================================================================================
|
|   Name        :   roll_the_dice.py
|   Project     :   diceware
|   Copyright   :   burrwebb
|   License     :   Apache-2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)
|   Description :   
|   
=================================================================================================================== """

import argparse
from diceware import Diceware


def main():

    diceware = Diceware()

    parser = argparse.ArgumentParser(description='Generate passphrases with Diceware!')

    parser.add_argument('-l', '--length', help='Desired length of passphrase', default=6, type=int)
    parser.add_argument('-n', '--num_phrases', help='Number of passphrases', default=1, type=int)

    args = parser.parse_args()

    length = args.length
    num_phrases = args.num_phrases

    list_of_phrases = diceware.generate_multiple(length_of_phrases=length, number_of_phrases=num_phrases)

    print()
    print("Your new passphrase(s):")
    print("----------------------------")

    for phrase in list_of_phrases:
        print(phrase)

    print()


# execute the script
if __name__ == "__main__":
    main()


"""
    Copyright 2019 burrwebb

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


