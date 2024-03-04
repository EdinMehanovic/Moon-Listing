from os import system, path, get_terminal_size
window_width = get_terminal_size().columns
#########################################################################################
from datetime import date
today = date.today().strftime("%B %d, %Y")
#########################################################################################
center_string = ""
count = 0
#########################################################################################
def header():
	system("cls||clear")
	print("\n\n"+"{0} {1}".format("Edin Mehanovic CIS125 Structure and Logic", today).center(window_width)+"\n\n")
#########################################################################################
def center(phrase):
	phrase = str(phrase)
	return ('%s'.center(get_terminal_size().columns-len(phrase))%phrase)
#########################################################################################
def input_center (phrase):
	return input("".ljust((window_width - len(phrase))//2)+ phrase)	
#########################################################################################
def read_file(my_file):
	global dictionary_moon, moon_list, number_list
	dictionary_moon = {}
	number_list = []
	file = open(my_file, "r")
	for line in file:
		line = line.strip()
		moon_list = line.split("\t")
		number_list += [moon_list[0],moon_list[1]]
		dictionary_moon[moon_list[0]] = moon_list[1], moon_list[2], moon_list[3], moon_list[4], moon_list[5], moon_list[6], moon_list[7]
#########################################################################################
def file_check(my_file):
	if path.isfile(my_file):
		read_file(my_file)
	else:
		print((my_file +" does not exist!!!").center(window_width))
#########################################################################################
def columns (phrase,col,remaining=False):
	global center_string,count
	if remaining:
		while count %col !=0:
			center_string+=" {0:>15} ".format("")
			count += 1
		print(center(center_string))
		center_string = ""
	else:
		center_string += " {0:>15} ".format(phrase)
		count+=1
		if count %col ==0:
			print(center(center_string))
			center_string = ""
#########################################################################################			
menu_equals_border = "="*140
star_border = "*"*109
equals_border = "="*105
half_equals_border = "="*49

def menu():
	print(center("Moons of the Solar System"))
	print("\n\n")
	print(center(menu_equals_border))
	for i in range(len(dictionary_moon)-1):
		columns("{0:3} {1:21}".format(number_list[(i+1)*2],number_list[(i*2)+3]), 5 )
	columns("",5,True)	
	print(center(menu_equals_border))
	

def input_moon():
	global moon_input
	moon_input = input(center("Enter in the number of the moon you wish to see "))
	if moon_input in dictionary_moon:
		header()
		process()
		output_moon()
	else:
		print(center(moon_input+" is an invalid entry..."))
		input_moon()


	# print(dictionary_moon)
def process():
	global planet_list, year_found
	planet_list = []
	planet_list = dictionary_moon[moon_input]
	year_found = 2023 - int(planet_list[2])
	year_found = str(year_found)	

def output_moon():
	print(center(star_border))
	print(center("* {0:^107} *".format("Moon")))
	print(center("* {0:^107} *".format(planet_list[0])))
	print(center("* {0:^107} *".format(equals_border)))
	print(center("* | {0:^50} | {1:^50} | *".format("Orbits Planet", "Year Discovered")))
	print(center("* | {0:^50} | {1:^50} | *".format(planet_list[1], planet_list[2])))
	print(center("* | {0:^50} | {1:^50} | *".format(half_equals_border, half_equals_border)))
	print(center("* | {0:^50} | {1:^50} | *".format("Discovrer By", "Distance from Planet (km)")))
	print(center("* | {0:^50} | {1:^50,.0f} | *".format(planet_list[3], int(planet_list[4]))))
	print(center("* | {0:^50} | {1:^50} | *".format(half_equals_border, half_equals_border)))
	print(center("* | {0:^50} | {1:^50} | *".format("Moon's Diameter (km)", "Orbital period (Days)")))
	print(center("* | {0:^50} | {1:^50} | *".format(planet_list[5],(planet_list[6]))))
	print(center("* | {0:^50} | {1:^50} | *".format(half_equals_border, half_equals_border)))
	print(center("* {0:^107} *".format("This moon was found " +year_found +" years ago")))
	print(center("* {0:^107} *".format('')))

	print(center(star_border))


def main_bus(repeat = 'y'):
	if repeat == 'n' or repeat == 'N':
		print("\n\n\n")
		print(center('''"Have a nice day!"\n'''))
		input_center("Press <Enter> to continue... ")
		return
	elif repeat == 'y' or repeat == 'Y':
		read_file("Moons.txt")	
		header()
		menu()
		input_moon()
		repeat = input_center("Would you like to run the program again (Y/N): ")
		main_bus(repeat)
	else:
		print("\n\n")
		print(center(repeat+" is an invalid entry\n\n"))
		repeat = input_center("Would you like to run the program again (Y/N): ")
		main_bus(repeat)

main_bus()
