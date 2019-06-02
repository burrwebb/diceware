# ideal-waffle

Version 0.4

Tinkering with a simple Diceware implementation class for Python.


## Installation
```python

python3 setup.py install

```



## Usage

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
