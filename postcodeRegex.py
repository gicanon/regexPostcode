"""Testing Regex by using the UK Postcode Format

Example: SW1A 2AA
Outcode: SW1A
Incode: 2AA

Definitions:

Outward Code
The outward code is the first half of a postcode (before the space). 
Some are non-geographic, i.e. does not divulge the location.

Distinguishing features include:

- 2-4 characters long
- Always begins with a letter
- May end with a number or letter

Examples of outward codes include:
L1
W1A
RH1
RH10
SE1P


Inward Code
The inward code is the second half of a postcode (before the space). 
The inward code assists in the delivery of post within a postal district.

Its distinguishing features are:

- Exactly 3 characters long
- Always begins with a number

Examples of inward codes:
0NY
7GZ
7HF
8JQ

"""

import re # importing regex module


# Create a python program that implements a regex that complies with the rules provided above – 
# test it against the examples provided.
# Examples:
# M1 1AA
# M60 1NW
# CR2 6XH
# DN55 1PT
# W1A 1HQ
# EC1A 1BB

def regexTest(txt):
    x = re.findall(r"^[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}$", txt)
    if x:
        print("Potscode is right", txt)
    else:
        print("Postcode is wrong", txt)

regexTest('M1 1AA')
regexTest('M60 1NW')
regexTest('CR2 6XH')
regexTest('DN55 1PT')
regexTest('W1A 1HQ')
regexTest('EC1A 1BB')



