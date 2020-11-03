from os import *
from time import sleep

# Main
print("If you run setup.py then the directory will change name from setup-xrdp to setup beacause the easier access to the directory, it will also delete setup.py for cleanliness.")
inputed = input("Are you sure you want to do this? (y/n): ")
if inputed == "y" or inputed == "Y":
	system("cd ..")
	sleep(0,5)
	system("mv setup-xrdp setup")
	sleep(0,5)
	system("cd setup")
	sleep(0,5)
	system("rm -rf setup.py *")
else:
	print("""Acceptable have a great day 
	-meme""")
