#import the package form the internet using "pip3 import pyshorteners"
import pyshorteners 

#let user enter the URL
Link = input ("Enter your URL: ")

#make a class for cutting the link, don't forget to keet the "S" capital.
shortener = pyshorteners.Shortener()

#assigning the class to a variable 
x = shortener.tinyurl.short(Link)

#Printing the shorten URL
print ("Your new URL is: " + x)