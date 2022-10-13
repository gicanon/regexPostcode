# regexPostcode

Python program to handle Postcode with regular expression

## Description

This Python program is used to demonstrate how to use regular expression by validating UK Postcodes

Testing Regex by using the UK Postcode Format

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

Regex command: 'r"^[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}$"'

## Getting Started

### Dependencies

This python project does not have any external libraries. However, starting this program will only require a Python 3 version.

### Installing

The latest version of python can be installed on the website: https://www.python.org/downloads/.

### Executing program

The program can be executed and tested at every Python IDE.

## Authors

Gianluca Cannone - https://github.com/gicanon

## License

Copyright (c) [2022] [Gianluca Cannone]

Permission is hereby granted, free of charge, to any person obtaining a copy of the project without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project, and to permit persons to whom the project is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of this project.

THE PROJECT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE PROJECT OR THE USE OR OTHER DEALINGS IN THE PROJECT.
