#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("object-oriented programming"):].split()[0]+" " + str[\
str.find('with'):].split()[0] + " " +str[str.find('Python'):].split()[0]
print(str)
