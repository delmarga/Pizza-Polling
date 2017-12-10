# Polling for Pizza

import time

hungry = True;

while(hungry):
	print('Opening the front door.')
	front_door = open('front_door.txt', 'r')

# Type "Pizza Guy" in the text file (front_door.txt) and save
# This will make the condition True, and stop the program.

	if "Pizza Guy" in front_door:
		print("Pizza's here!")
		hungry = False;
	else:
		print("Not yet...")

	print('Closing the front door.')
	front_door.close()

	time.sleep(1)