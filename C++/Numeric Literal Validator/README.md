### Write a program to identify all valid numerical literals.

In C++ progamming language. all the following expressions represent valid numerical "literals":

 - 3 
 - .328
 - 41.16
 - +4580
 - +0
 - -01
 - -14.4
 - 1e12
 - +1.4e6
 - -2.e+7
 - 01E-06
 - -.4E-7
 - 0030
 - +0e1
 - .2E-03

Literals consist of an integral part and an optional exponent part. Integral part consists of an optional sign ('+' or '-') and literal value. Literal value should consist of __at least one digit__ either before or after the decimal point. However, the decimal point is also optional. Exponent part (which is optional) starts with either 'e' or 'E', and if it appears, the number following it ('e' or 'E') must be an integer (with optional '+' or '-' sign). Assume that there are no limits on the number of consevutive digits in any part of the literal (but the lengtb of the string is limited to 50 digits/characters.)


Write a C++ program that reads in the filename, which is a text file of strings, one string on each line, and output the result to both the sceen AND a text file, each particular string whether each string is a valid numeric literal or not. __Your program should account for all possible user input.__

