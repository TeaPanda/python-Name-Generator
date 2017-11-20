import random
import string

string.ascii_uppercase
string.ascii_lowercase
name = ""

while True:
	x = int(input("How many letters do you want in your name?"))
	if x > 15:
		print("Pretty long name, hey? Put something more reasonable please")
	else:
		break

while x > 0:
	name += random.choice(string.ascii_lowercase)
	x = x - 1


print("Your name is " + name.capitalize())

