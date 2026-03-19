#Valid String in Python

"""

str1 = "This is a string." #more appropriate
str2 = 'This is a string.\n' #\n" new line create kore
print(str1, str2, str3)

"""
#str3 = """This is a string."""


#string concatenation

"""

str1 = "hello"
str2 = "world"
str4 = str1 + str2
print(str4)

"""

#string length "len()"

"""

str1 = "Legendary"
len1 = len(str1)
print(len1)

str2 = "Ninja"
len2 = len(str2)
print(len2)

str3 = "Alex"
len3 = len(str3)
print(len3)

final_str = str1 + " " + str2 + " " + str3 #" " free space also be calculated in string length
print(final_str)
print(len(final_str))

"""

#indexing

"""

str = "random people"
# print(str[1]) #direct output
ch = str[1]
print(ch)

# string indexing e amra just string er character ke access korte parbo but new kono character diye replace korte parbo na
# str[4] = "m"
# print(str)

"""

# *Slicing* ==>> Positive index <<==

#structure: str[starting_indx : ending_indx] ==> ending index is not include

"""
str = "apna college"
print(str[5 : 12]) 
print(len(str[5 : 12]))
print(str[5 : len(str)]) #len() => string length ber korar jonno

"""

# *Slicing* ==>> Negative index <<==

# *Negative index e numbering ta right side theke (-1) theke suru hoy and right theke left e (-1) kore barte thake

str = "Apple"
print(str[-5 : -2]) # App
