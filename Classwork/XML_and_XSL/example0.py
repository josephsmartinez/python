#This lecture was developed by Dr Gregory Reis using the following sources:
#The Hitchhiker's Guide to Python (available at https://docs.python-guide.org/)
#XML, 2nd Edition. Kevin Howard Goldberg, PeachPit Press, 2009
#Dr Kip Irvine's class notes
#Python Foundation (available at https://docs.python.org/3/)
#October 2018

import xmltodict
from PIL import Image

#1) Open the xml file 'ancient_wonders.xml' using the xmltodict library:

#2) Print the type of ancient_wonders

#An OrderedDict is a subclass of dictionary that remembers
# the order in which its contents were added.
# It is important to highlight supporting the usual dict methods
# If a new entry overwrites an existing entry,
# the original insertion position is left unchanged.
# Deleting an entry and reinserting it will move it to the end. (docs.python.org)

#3) Print the keys of ancient_wonders

#4) Print the type of the data stored in the key you printed in question 3)

#5) Following question 4), print its keys:

#6) Print the type of the data stored in the key above:

#7) Loop over the data retrieved in question 6):

#8a) For the first item looped above, print the language attribute

#8b) Now print the text associated:

#9a) For the second item looped in question 7, print the language attribute

#9b) Now print the text associated:

#10) For the first item, assign the file attribute associated with the main_image to a variable
#called 'colossus_img'

#11) Use the method Image.open() to and save the output into variable called 'colossus_img2'

#12) Show the image with the method .show()

