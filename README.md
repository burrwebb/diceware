# diceware

Version 0.4.1

Tinkering with a simple Diceware implementation class for Python.

## Requirements
```commandline

pip3 install -r requirements.txt

```

## Installation
```python

python3 setup.py install

```

## Module Usage

#### Generate a Single Passphrase
```python
import diceware

csv_file_location = 'dicewareList.csv'
diceware_instance = diceware.Diceware(csv_file_location)
my_passphrase = diceware_instance.generate()

```

#### Generate Multiple Passphrases
```python

import diceware

csv_file_location = 'dicewareList.csv'
diceware_instance = diceware.Diceware(csv_file_location)
my_passphrase = diceware_instance.generate_multiple()
```

## roll_the_dice.py Script Usage
```commandline
python3 roll_the_dice.py -h

usage: roll_the_dice.py [-h] [-l LENGTH] [-n NUM_PHRASES]

Generate passphrases with Diceware!

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Desired length of passphrase
  -n NUM_PHRASES, --num_phrases NUM_PHRASES
                        Number of passphrases
```

##### Default Behavior
```commandline
python3 roll_the_dice.py

Your new passphrase(s):
----------------------------
onus gx moyer gus alden ed
```

##### Custom passphrase length, and number of passphrases
```commandline
python3 roll_the_dice.py -l 4 -n 3      

Your new passphrase(s):
----------------------------
lz 46th sudan bake
lunge sleet winch piggy
beep sweaty heal serge
```